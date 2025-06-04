grammar BASIQuinho;

// Ponto de entrada da gramática
prog: stmt+ EOF;

// Declarações (comandos)
stmt: inputStmt  # InputStatement
    | printStmt  # PrintStatement
    | letStmt    # LetStatement
    ;

// Comando INPUT (Simplificado)
inputStmt: INPUT ID NEWLINE;

// Comando PRINT
printStmt: PRINT exprList NEWLINE;

// Comando LET (atribuição)
letStmt: LET ID '=' expr NEWLINE;

// Lista de expressões para o PRINT
exprList: expr (',' expr)*;

// Expressões (SEM LABELS #AddSub, #JustTerm)
expr: term (('+' | '-') term)* ;

// Termos (SEM LABELS #MulDiv, #JustFactor)
term: factor (('*' | '/') factor)* ;

// Fatores (Labels aqui estão OK e são a melhor prática)
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