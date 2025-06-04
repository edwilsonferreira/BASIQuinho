# geracao_llvm.py
import logging
from erro import Erro

class GeracaoLLVM:
    def __init__(self, erro_handler: Erro):
        self.erro_handler = erro_handler
        self.logger = logging.getLogger(self.__class__.__name__)
        self.codigo_llvm_linhas = []
        self.reg_count = 0 # Contador para registradores virtuais LLVM (%0, %1, ...)
        self.var_map = {}  # Mapeia nomes de variáveis BASIQuinho para seus ponteiros na stack LLVM
        self.global_str_count = 0 # Contador para strings globais (para PRINT)

    def _nova_reg(self) -> str:
        reg = f"%r{self.reg_count}"
        self.reg_count += 1
        return reg

    def _nova_label_str(self, text_content: str) -> str:
        label = f"@.str.{self.global_str_count}"
        self.global_str_count += 1
        # Escapa caracteres especiais para strings LLVM se necessário
        # Conteúdo C string (com null terminator): "conteudo\00"
        # Tamanho: len(text_content) + 1
        # Ex: @.str.0 = private unnamed_addr constant [14 x i8] c"Hello, World!\0A\00"
        # Por simplicidade, vamos assumir que o TAC nos dá strings "limpas"
        llvm_str_decl = f"{label} = private unnamed_addr constant [{len(text_content) + 1} x i8] c\"{text_content}\\00\""
        # Adiciona no início do código LLVM (depois de outros globals)
        # Encontra o final das declarações globais e insere antes do primeiro 'define'
        insert_pos = 0
        for i, line in enumerate(self.codigo_llvm_linhas):
            if line.strip().startswith("define i32 @main()"):
                insert_pos = i
                break
        if insert_pos == 0 and len(self.codigo_llvm_linhas) > 0 : insert_pos = len(self.codigo_llvm_linhas) # Adiciona no fim se main não achado
        elif insert_pos == 0 and len(self.codigo_llvm_linhas) == 0: self.codigo_llvm_linhas.append(llvm_str_decl) # Primeiro item
        else: self.codigo_llvm_linhas.insert(insert_pos, llvm_str_decl)

        return label


    def _get_var_ptr(self, var_name: str) -> str:
        if var_name not in self.var_map:
            # Aloca na entrada da função main
            # A inserção deve ser cuidadosa para ser no local correto (entry block)
            ptr_reg = f"%ptr.{var_name.replace('t', 'tmp')}" # Evita conflito com nomes de registradores temporários tX
            self.var_map[var_name] = ptr_reg
            
            # Adiciona a instrução alloca no início do bloco 'entry:'
            entry_block_start_idx = -1
            for idx, line in enumerate(self.codigo_llvm_linhas):
                if line.strip() == "entry:":
                    entry_block_start_idx = idx + 1
                    break
            
            if entry_block_start_idx != -1:
                # Assume i32 para todos por simplicidade. BASIQuinho pode precisar de float (double) e strings.
                self.codigo_llvm_linhas.insert(entry_block_start_idx, f"  {ptr_reg} = alloca i32, align 4 ; Var {var_name}")
            else:
                # Fallback se 'entry:' não for encontrado (improvável para main bem formada)
                self.erro_handler.registrar_erro("Gerador LLVM",0,0,f"Bloco 'entry:' não encontrado para alocar variável '{var_name}'.","LLVM")

        return self.var_map[var_name]


    def _load_operand(self, operand_tac: str) -> str:
        """ Carrega um operando TAC para um registrador LLVM, retornando o nome do registrador."""
        reg_val = self._nova_reg()
        if operand_tac.isdigit() or (operand_tac.startswith('-') and operand_tac[1:].isdigit()): # É uma literal numérica
            # LLVM usa o valor diretamente em muitas instruções, não precisa de load para i32 literal.
            return operand_tac # Retorna a própria literal
        elif operand_tac.startswith("t"): # É uma temporária do TAC (que já deve conter um valor, não um ponteiro)
            # Assumindo que temporárias do TAC (t0, t1) já são valores (registradores virtuais)
            # e não endereços de memória. Se tX representa um valor em um registrador LLVM %tX:
            return f"%{operand_tac}" # ex: %t0 (se TAC t0 -> LLVM %t0)
        else: # É uma variável de usuário
            var_ptr = self._get_var_ptr(operand_tac)
            self.codigo_llvm_linhas.append(f"  {reg_val} = load i32, ptr {var_ptr}, align 4")
            return reg_val


    def gerarCodigoLLVM(self, codigo_tac: list):
        self.logger.info("Iniciando geração de Código LLVM IR...")
        if not codigo_tac or self.erro_handler.houve_erro_fatal():
            self.logger.error("Código TAC não fornecido ou erros anteriores impedem geração LLVM.")
            return None

        self.codigo_llvm_linhas = [
            "; Modulo BASIQuinho LLVM IR",
            "target triple = \"x86_64-pc-linux-gnu\" ; Exemplo",
            "",
            "; Declaracoes de funcoes C externas para I/O",
            "@.str.print.num.fmt = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"", # Formato para PRINT numero
            "@.str.print.str.fmt = private unnamed_addr constant [4 x i8] c\"%s\\0A\\00\"", # Formato para PRINT string
            "@.str.scan.num.fmt = private unnamed_addr constant [3 x i8] c\"%d\\00\"",   # Formato para INPUT numero
            "declare i32 @printf(ptr nocapture readonly, ...) nounwind",
            "declare i32 @scanf(ptr nocapture readonly, ...) nounwind",
            "",
            "define i32 @main() {",
            "entry:"
            # As alocações de variáveis (alloca) serão inseridas aqui pelo _get_var_ptr
        ]
        self.reg_count = 0
        self.var_map = {}
        self.global_str_count = 0

        try:
            for instrucao_tac in codigo_tac:
                self.logger.debug(f"Processando TAC para LLVM: {instrucao_tac}")
                partes = instrucao_tac.split(' ')
                comando_ou_destino = partes[0]

                if comando_ou_destino == "INPUT": # INPUT var
                    var_nome = partes[1]
                    var_ptr = self._get_var_ptr(var_nome)
                    self.codigo_llvm_linhas.append(f"  ; TAC: INPUT {var_nome}")
                    scan_reg = self._nova_reg()
                    self.codigo_llvm_linhas.append(f"  {scan_reg} = call i32 (ptr, ...) @scanf(ptr @.str.scan.num.fmt, ptr {var_ptr})")

                elif comando_ou_destino == "PRINT": # PRINT val
                    val_tac = partes[1]
                    self.codigo_llvm_linhas.append(f"  ; TAC: PRINT {val_tac}")
                    
                    if val_tac.startswith('"') and val_tac.endswith('"'): # É uma string literal
                        str_content = val_tac[1:-1] # Remove aspas
                        # \n, \t etc. dentro da string BASIQuinho precisariam ser traduzidos para sequências de escape LLVM/C
                        str_label = self._nova_label_str(str_content + "\\0A") # Adiciona newline para PRINT
                        # Precisa de GEP (GetElementPtr) para passar o ponteiro para array de char
                        # Ex: %ptr_str = getelementptr inbounds [Tamanho x i8], [Tamanho x i8]* @.str.X, i64 0, i64 0
                        # Tamanho = len(str_content) + 1 (para \0A) + 1 (para \00 final do C string)
                        # Por simplicidade, se @printf aceita ptr para const char*, o label da string é suficiente
                        # Mas o tipo de @.str.X precisa ser ptr
                        # Vamos usar um formato de string para printf:
                        gep_reg = self._nova_reg()
                        self.codigo_llvm_linhas.append(f"  {gep_reg} = getelementptr inbounds [{len(str_content)+2} x i8], ptr {str_label}, i32 0, i32 0")
                        print_reg = self._nova_reg()
                        self.codigo_llvm_linhas.append(f"  {print_reg} = call i32 (ptr, ...) @printf(ptr @.str.print.str.fmt, ptr {gep_reg})")

                    else: # É uma variável, temporária ou literal numérica
                        val_llvm = self._load_operand(val_tac) # Se for literal, retorna a própria literal. Se var/temp, carrega.
                        print_reg = self._nova_reg()
                        self.codigo_llvm_linhas.append(f"  {print_reg} = call i32 (ptr, ...) @printf(ptr @.str.print.num.fmt, i32 {val_llvm})")


                elif len(partes) > 1 and partes[1] == ":=": # Atribuição: dest := ...
                    destino_tac = comando_ou_destino
                    destino_ptr_llvm = self._get_var_ptr(destino_tac)
                    self.codigo_llvm_linhas.append(f"  ; TAC: {instrucao_tac}")

                    if len(partes) == 3: # Atribuição simples: dest := fonte
                        fonte_tac = partes[2]
                        fonte_llvm_val = self._load_operand(fonte_tac) # Se for literal, retorna a própria literal
                        self.codigo_llvm_linhas.append(f"  store i32 {fonte_llvm_val}, ptr {destino_ptr_llvm}, align 4")

                    elif len(partes) == 5: # Operação: dest := op1 op_tac op2
                        op1_tac, op_tac, op2_tac = partes[2], partes[3], partes[4]
                        op1_llvm = self._load_operand(op1_tac)
                        op2_llvm = self._load_operand(op2_tac)
                        
                        llvm_op_str = ""
                        if op_tac == '+': llvm_op_str = "add nsw"
                        elif op_tac == '-': llvm_op_str = "sub nsw"
                        elif op_tac == '*': llvm_op_str = "mul nsw"
                        elif op_tac == '/': llvm_op_str = "sdiv" # Divisão de inteiros com sinal
                        else:
                            self.erro_handler.registrar_erro("Gerador LLVM", 0, 0, f"Operador TAC '{op_tac}' não suportado.", "LLVM")
                            continue
                        
                        res_op_reg = self._nova_reg()
                        self.codigo_llvm_linhas.append(f"  {res_op_reg} = {llvm_op_str} i32 {op1_llvm}, {op2_llvm}")
                        self.codigo_llvm_linhas.append(f"  store i32 {res_op_reg}, ptr {destino_ptr_llvm}, align 4")
                else:
                    self.logger.warning(f"Instrução TAC não reconhecida para LLVM: '{instrucao_tac}'")

        except Exception as e:
            self.erro_handler.registrar_erro("Gerador LLVM", 0, 0, f"Erro inesperado na geração LLVM: {e}", "LLVM")
            return None

        self.codigo_llvm_linhas.append("  ret i32 0")
        self.codigo_llvm_linhas.append("}")
        self.codigo_llvm_linhas.append("")

        if not self.erro_handler.tem_erros_llvm:
            self.logger.info("Geração de Código LLVM IR concluída.")
            final_code = "\n".join(self.codigo_llvm_linhas)
            self.logger.info("--- Código LLVM IR Gerado ---")
            # self.logger.info(final_code) # Pode ser muito verboso para o log INFO
            self.logger.info("---------------------------")
            return final_code
        else:
            self.logger.error("Geração de LLVM IR encontrou erros.")
            return None