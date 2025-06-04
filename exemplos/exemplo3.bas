REM BASIQuinho - Exemplo 3: Teste Completo de Recursos

PRINT "Bem-vindo ao Testador Completo do BASIQuinho!"
PRINT "============================================="
PRINT "" ; REM Imprime uma linha em branco
REM Linha acima usa ; como terminador. O REM subsequente é um comentário.
REM Ou podemos ter uma linha de comentário inteira como esta.

PRINT "Por favor, forneca dois numeros para os calculos."

PRINT "Digite o primeiro numero (X):"
INPUT X

PRINT "Digite o segundo numero (Y):"
INPUT Y

PRINT "" REM Outra linha em branco via PRINT

LET FATOR_EXTRA = 10
LET SOMA_XY = X + Y
LET DIFF_XY = X - Y
LET PRODUTO_XYF = X * Y * FATOR_EXTRA 
LET COMPLEXO_A = (X + FATOR_EXTRA) * (Y - 2) REM Testando precedencia e parenteses
LET COMPLEXO_B = PRODUTO_XYF / FATOR_EXTRA  REM Deve resultar em X * Y

PRINT "--- Valores de Entrada e Constante ---"
PRINT "X = ", X
PRINT "Y = ", Y
PRINT "FATOR_EXTRA = ", FATOR_EXTRA
PRINT ""

PRINT "--- Resultados dos Calculos ---"
PRINT "X + Y = ", SOMA_XY
PRINT "X - Y = ", DIFF_XY
PRINT "X * Y * FATOR_EXTRA = ", PRODUTO_XYF
PRINT "(X + FATOR_EXTRA) * (Y - 2) = ", COMPLEXO_A
PRINT "PRODUTO_XYF / FATOR_EXTRA (deve ser X*Y) = ", COMPLEXO_B
PRINT ""

LET MENSAGEM_FINAL = "Teste de todos os recursos concluido!"
PRINT MENSAGEM_FINAL

REM Fim do programa
