# geracao_llvm.py
import logging
from erro import Erro
import re
import datetime # Importação adicionada

class GeracaoLLVM:
    def __init__(self, erro_handler: Erro):
        self.erro_handler = erro_handler
        self.logger = logging.getLogger(self.__class__.__name__)
        self.codigo_llvm_linhas = []
        self.main_body_instructions = [] 
        self.global_definitions = []   
        self.reg_count = 0
        self.var_map = {}  
        self.global_str_count = 0

    # ... (métodos _nova_reg, _sanitize_llvm_name, _get_var_ptr, _nova_global_string_const, _load_operand como antes) ...
    def _nova_reg(self) -> str:
        reg = f"%r{self.reg_count}"
        self.reg_count += 1
        return reg

    def _sanitize_llvm_name(self, name: str) -> str:
        sanitized = re.sub(r'[^a-zA-Z0-9$._]', '_', name)
        if not sanitized or not (sanitized[0].isalpha() or sanitized[0] in ['$', '.', '_']):
            sanitized = "v_" + sanitized
        return sanitized

    def _get_var_ptr(self, var_name_basiquinho: str) -> str:
        if var_name_basiquinho not in self.var_map:
            llvm_var_name_clean = self._sanitize_llvm_name(var_name_basiquinho)
            ptr_reg = f"%ptr.{llvm_var_name_clean}"
            self.var_map[var_name_basiquinho] = ptr_reg
            self.main_body_instructions.insert(0, f"  {ptr_reg} = alloca i32, align 4 ; Var {var_name_basiquinho}")
        return self.var_map[var_name_basiquinho]

    def _nova_global_string_const(self, text_content: str) -> str:
        str_label = f"@.str.const.{self.global_str_count}"
        self.global_str_count += 1
        
        llvm_escaped_content = ""
        for char_code in text_content.encode('utf-8'):
            if 32 <= char_code <= 126 and chr(char_code) not in ['"', '\\']:
                llvm_escaped_content += chr(char_code)
            else: 
                llvm_escaped_content += f"\\{char_code:02X}"
        llvm_escaped_content += "\\00" 

        num_bytes = len(text_content.encode('utf-8')) + 1

        llvm_str_decl = f'{str_label} = private unnamed_addr constant [{num_bytes} x i8] c"{llvm_escaped_content}"'
        self.global_definitions.append(llvm_str_decl)
        return str_label

    def _load_operand(self, operand_tac: str) -> tuple[str, str]:
        if operand_tac.isdigit() or (operand_tac.startswith('-') and operand_tac[1:].isdigit()):
            return "i32", operand_tac
        
        elif operand_tac.startswith('"') and operand_tac.endswith('"'): 
            str_content = operand_tac[1:-1]
            global_str_label = self._nova_global_string_const(str_content)
            gep_reg = self._nova_reg()
            num_bytes = len(str_content.encode('utf-8')) + 1
            # Adiciona a instrução GEP ao corpo da main, pois ela gera um valor em tempo de execução (ponteiro)
            self.main_body_instructions.append(f"  {gep_reg} = getelementptr inbounds [{num_bytes} x i8], ptr {global_str_label}, i64 0, i64 0")
            return "ptr", gep_reg

        elif operand_tac.startswith("t"): 
            return "i32", f"%{operand_tac}" 
        
        else: 
            var_ptr = self._get_var_ptr(operand_tac) 
            loaded_val_reg = self._nova_reg()
            self.main_body_instructions.append(f"  {loaded_val_reg} = load i32, ptr {var_ptr}, align 4")
            return "i32", loaded_val_reg

    def gerarCodigoLLVM(self, codigo_tac: list):
        self.logger.info("Iniciando geração de Código LLVM IR...")
        if not codigo_tac and not self.erro_handler.houve_erro_fatal():
             self.logger.info("Código TAC vazio, Geração LLVM produzirá corpo de main vazio.")
        elif not codigo_tac and self.erro_handler.houve_erro_fatal(): 
            self.logger.error("Código TAC não fornecido devido a erros anteriores, Geração LLVM não pode prosseguir.")
            return None
        elif not codigo_tac : # Caso genérico de TAC vazio sem erro fatal prévio explícito (ex: programa fonte vazio)
             self.logger.info("Código TAC vazio (programa fonte pode ser vazio). Geração LLVM produzirá corpo de main mínimo.")


        self.main_body_instructions = []
        self.global_definitions = []
        self.reg_count = 0
        self.var_map = {}
        self.global_str_count = 0
        
        try:
            # Processamento do TAC (como na versão anterior)
            for instrucao_tac in codigo_tac:
                self.logger.debug(f"Processando TAC para LLVM: {instrucao_tac}")
                partes = []
                # Parse robusto da instrução TAC
                if instrucao_tac.startswith("PRINT "):
                    partes = ["PRINT", instrucao_tac[len("PRINT "):].strip()]
                elif " := " in instrucao_tac:
                    destino, expressao = instrucao_tac.split(" := ", 1)
                    partes = [destino.strip(), ":="] + [p.strip() for p in expressao.split(' ', 2)]
                elif instrucao_tac.startswith("INPUT "):
                    partes = ["INPUT", instrucao_tac[len("INPUT "):].strip()]
                else:
                    self.logger.error(f"Formato de instrução TAC não reconhecido: {instrucao_tac}")
                    self.erro_handler.registrar_erro("Gerador LLVM",0,0,f"Formato TAC irreconhecível: {instrucao_tac}", "LLVM")
                    continue
                
                comando_ou_destino = partes[0]

                if comando_ou_destino == "INPUT":
                    var_nome_basiquinho = partes[1]
                    var_ptr = self._get_var_ptr(var_nome_basiquinho)
                    self.main_body_instructions.append(f"  ; TAC: INPUT {var_nome_basiquinho}")
                    scan_call_reg = self._nova_reg()
                    self.main_body_instructions.append(f"  {scan_call_reg} = call i32 (ptr, ...) @scanf(ptr @.str.scan.num.fmt, ptr {var_ptr})")

                elif comando_ou_destino == "PRINT":
                    val_tac_print = partes[1]
                    self.main_body_instructions.append(f"  ; TAC: PRINT {val_tac_print}")
                    tipo_llvm_op, val_llvm_op = self._load_operand(val_tac_print)
                    if tipo_llvm_op == "ptr":
                        print_call_reg = self._nova_reg()
                        self.main_body_instructions.append(f"  {print_call_reg} = call i32 (ptr, ...) @printf(ptr @.str.print.str.fmt, ptr {val_llvm_op})")
                    elif tipo_llvm_op == "i32":
                        print_call_reg = self._nova_reg()
                        self.main_body_instructions.append(f"  {print_call_reg} = call i32 (ptr, ...) @printf(ptr @.str.print.num.fmt, i32 {val_llvm_op})")
                    else:
                        self.logger.error(f"Tipo de operando desconhecido para PRINT LLVM: {tipo_llvm_op} para valor '{val_tac_print}'")
                        self.erro_handler.registrar_erro("Gerador LLVM",0,0,f"Tipo inválido para PRINT: {tipo_llvm_op}", "LLVM")

                elif len(partes) > 1 and partes[1] == ":=": 
                    destino_tac = comando_ou_destino
                    self.main_body_instructions.append(f"  ; TAC: {instrucao_tac}")
                    if len(partes) == 3: 
                        fonte_tac = partes[2]
                        tipo_llvm_fonte, val_llvm_fonte = self._load_operand(fonte_tac)
                        if tipo_llvm_fonte != "i32":
                            self.logger.error(f"Atribuição de tipo não-i32 ({tipo_llvm_fonte}) para variável/temporária i32 não suportada: {instrucao_tac}")
                            self.erro_handler.registrar_erro("Gerador LLVM",0,0,f"Atribuição de tipo incompatível: {instrucao_tac}", "LLVM")
                            continue
                        if destino_tac.startswith("t"):
                            self.main_body_instructions.append(f"  %{destino_tac} = add i32 {val_llvm_fonte}, 0 ; Assign to temp {destino_tac}")
                        else: 
                            destino_ptr = self._get_var_ptr(destino_tac)
                            self.main_body_instructions.append(f"  store i32 {val_llvm_fonte}, ptr {destino_ptr}, align 4")
                    elif len(partes) == 5: 
                        op1_tac, op_str, op2_tac = partes[2], partes[3], partes[4]
                        tipo_op1, val_op1 = self._load_operand(op1_tac)
                        tipo_op2, val_op2 = self._load_operand(op2_tac)
                        if tipo_op1 != "i32" or tipo_op2 != "i32":
                            self.logger.error(f"Operação aritmética com tipos não-i32 ({tipo_op1}, {tipo_op2}) não suportada: {instrucao_tac}")
                            self.erro_handler.registrar_erro("Gerador LLVM",0,0,f"Operação com tipos incompatíveis: {instrucao_tac}", "LLVM")
                            continue
                        llvm_op_keyword = ""
                        if op_str == '+': llvm_op_keyword = "add nsw"
                        elif op_str == '-': llvm_op_keyword = "sub nsw"
                        elif op_str == '*': llvm_op_keyword = "mul nsw"
                        elif op_str == '/': llvm_op_keyword = "sdiv"
                        else:
                            self.erro_handler.registrar_erro("Gerador LLVM", 0,0, f"Operador TAC '{op_str}' não suportado para LLVM.", "LLVM"); continue
                        result_reg = f"%{destino_tac}" if destino_tac.startswith("t") else self._nova_reg()
                        self.main_body_instructions.append(f"  {result_reg} = {llvm_op_keyword} i32 {val_op1}, {val_op2}")
                        if not destino_tac.startswith("t"):
                            destino_ptr = self._get_var_ptr(destino_tac)
                            self.main_body_instructions.append(f"  store i32 {result_reg}, ptr {destino_ptr}, align 4")
                    else:
                        self.logger.error(f"Formato de atribuição TAC não reconhecido: {instrucao_tac}")
                        self.erro_handler.registrar_erro("Gerador LLVM",0,0,f"Formato de atribuição TAC irreconhecível: {instrucao_tac}", "LLVM")
                else:
                     self.logger.warning(f"Instrução TAC não reconhecida para LLVM: {instrucao_tac}")
        
        except Exception as e:
            self.erro_handler.registrar_erro("Gerador LLVM", 0, 0, f"Erro inesperado e crítico na geração LLVM: {e}", "LLVM")
            self.logger.exception("Detalhes da exceção crítica na geração LLVM:")
            return None

        # <<< INÍCIO DAS MODIFICAÇÕES DO CABEÇALHO >>>
        now = datetime.datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%H:%M")

        informational_header = [
            "; Generated by the BASIQuinho compiler",
            "; BASIQuinho Compiler: https://github.com/edwilsonferreira/BASIQuinho",
            f"; Generated on: {date_str} at {time_str}",
            ";",
            "; To compile this LLVM IR code to an executable:",
            "; 1. Ensure you have Clang installed (or an equivalent LLVM toolchain).",
            "; 2. Run the command:",
            ";    clang your_output_filename.ll -o your_executable_name",
            ";",
            "; Alternatively, using llc (LLVM static compiler) and a C linker (e.g., gcc or clang):",
            "; 1. Generate an object file from LLVM IR:",
            ";    llc -filetype=obj your_output_filename.ll -o your_output_filename.o",
            "; 2. Link the object file to create an executable:",
            ";    clang your_output_filename.o -o your_executable_name",
            ";    (or use gcc: gcc your_output_filename.o -o your_executable_name)",
            ";",
            ""
        ]
        
        # Configurações do módulo e declarações externas
        module_setup = [
            "target triple = \"x86_64-pc-linux-gnu\" ; Ajuste conforme sua plataforma alvo",
            "",
            "; Declaracoes de funcoes C externas para I/O",
            "@.str.print.num.fmt = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"", # %d\n\0
            "@.str.print.str.fmt = private unnamed_addr constant [4 x i8] c\"%s\\0A\\00\"", # %s\n\0
            "@.str.scan.num.fmt = private unnamed_addr constant [3 x i8] c\"%d\\00\"",   # %d\0
            "declare i32 @printf(ptr nocapture readonly, ...) nounwind",
            "declare i32 @scanf(ptr nocapture readonly, ...) nounwind",
            ""
        ]
        # <<< FIM DAS MODIFICAÇÕES DO CABEÇALHO >>>
        
        define_main = [
            "define i32 @main() {",
            "entry:"
        ]
        
        footer = [
            "  ret i32 0",
            "}",
            ""
        ]

        # Monta o código LLVM final com o novo cabeçalho
        self.codigo_llvm_linhas = (informational_header + 
                                   module_setup + 
                                   self.global_definitions + 
                                   [""] +  # Linha em branco antes de 'define main' se houver globals
                                   define_main + 
                                   self.main_body_instructions + 
                                   footer)
        
        if not self.erro_handler.tem_erros_llvm:
            self.logger.info("Geração de Código LLVM IR concluída.")
            final_code = "\n".join(self.codigo_llvm_linhas)
            self.logger.info("--- Código LLVM IR Gerado (trecho inicial) ---")
            for i, line_llvm in enumerate(self.codigo_llvm_linhas[:30]): # Loga as primeiras 30 linhas
                 self.logger.info(line_llvm)
            if len(self.codigo_llvm_linhas) > 30:
                 self.logger.info("   (...)")
            self.logger.info("------------------------------------------")
            return final_code
        else:
            self.logger.error("Geração de LLVM IR encontrou erros.")
            return None
