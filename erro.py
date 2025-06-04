# erro.py
import logging
from antlr4.error.ErrorListener import ErrorListener as ANTLRErrorListener

logger = logging.getLogger(__name__) # Logger específico para este módulo

class Erro:
    def __init__(self):
        self.tem_erros_lexicos = False
        self.tem_erros_sintaticos = False
        self.tem_erros_semanticos = False
        self.tem_erros_tac = False
        self.tem_erros_llvm = False

    def registrar_erro(self, modulo: str, linha: int, coluna: int, mensagem: str, tipo_erro: str = "GERAL"):
        # Usar o logger configurado para exibir o erro
        # Pode-se usar logger.error ou um logger específico da classe Erro
        log_msg = f"ERRO [{modulo}]: Linha {linha}, Coluna {coluna} - {mensagem}"
        logging.getLogger("ERRO_HANDLER").error(log_msg) # Usar um logger específico ou o logger do módulo

        if tipo_erro == "LEXICO":
            self.tem_erros_lexicos = True
        elif tipo_erro == "SINTATICO":
            self.tem_erros_sintaticos = True
        elif tipo_erro == "SEMANTICO":
            self.tem_erros_semanticos = True
        elif tipo_erro == "TAC":
            self.tem_erros_tac = True
        elif tipo_erro == "LLVM":
            self.tem_erros_llvm = True
        elif tipo_erro == "AVISO_SEMANTICO" or tipo_erro == "AVISO": # Não impede compilação
            logging.getLogger("ERRO_HANDLER").warning(log_msg.replace("ERRO", "AVISO"))
            return # Avisos não setam flags de erro fatal

    def houve_erro_fatal(self) -> bool:
        """ Verifica se ocorreu algum erro que impeça a continuação da compilação """
        return self.tem_erros_lexicos or self.tem_erros_sintaticos or self.tem_erros_semanticos

class CustomErrorListener(ANTLRErrorListener):
    def __init__(self, erro_handler: Erro, modulo: str):
        super().__init__()
        self.erro_handler = erro_handler
        self.modulo = modulo

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        tipo = "LEXICO" if "Lexer" in str(type(recognizer).__name__) else "SINTATICO"
        self.erro_handler.registrar_erro(self.modulo, line, column, msg, tipo_erro=tipo)