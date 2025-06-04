grammar BASIQuinho;

// Ponto de entrada da gramática
// Permite NEWLINEs opcionais no início, entre statements, e no final.
// Requer pelo menos um statement real devido ao '+' em (NEWLINE* stmt)+.
prog: (NEWLINE* stmt)+ NEWLINE* EOF;

// Declarações (comandos)
stmt: inputStmt  # InputStatement
    | printStmt  # PrintStatement
    | letStmt    # LetStatement
    ;

// Comando INPUT (Simplificado)
// Ex: INPUT idadeVar
inputStmt: INPUT ID NEWLINE;

// Comando PRINT
// Ex: PRINT "Olá, ", nomeVar, "!"
// Ex: PRINT "O resultado é:", resultado
// Ex: PRINT valor
printStmt: PRINT exprList NEWLINE;

// Comando LET (atribuição)
// Ex: LET a = 10
// Ex: LET nome = "Fulano"
// Ex: LET resultado = a + b * 2
letStmt: LET ID '=' expr NEWLINE;

// Lista de expressões para o PRINT
exprList: expr (',' expr)*;

// Expressões (sem labels problemáticas como #AddSub ou #JustTerm aqui)
expr: term (('+' | '-') term)* ;

// Termos (sem labels problemáticas como #MulDiv ou #JustFactor aqui)
term: factor (('*' | '/') factor)* ;

// Fatores (Labels aqui estão OK e são a melhor prática para alternativas)
factor: NUMBER                     # Number
      | STRING                     # String
      | ID                         # Variable
      | '(' expr ')'               # Parentheses
      ;

// Tokens (Lexer)
INPUT: 'INPUT';
PRINT: 'PRINT';
LET: 'LET';

ID: [a-zA-Z_] [a-zA-Z0-9_]*; // Identificador de variável
NUMBER: [0-9]+ ('.' [0-9]+)?; // Números inteiros ou de ponto flutuante simples
STRING: '"' (~["\r\n])*? '"'; // Strings delimitadas por aspas duplas

NEWLINE: '\r'? '\n' | ';'; // Fim de linha ou ponto e vírgula como terminador de comando
WS: [ \t]+ -> skip; // Espaços em branco e tabulações são ignorados
