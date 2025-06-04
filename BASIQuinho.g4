grammar BASIQuinho;

// Ponto de entrada da gramática
prog: (NEWLINE* stmt)+ NEWLINE* EOF;

// Declarações (comandos)
stmt: inputStmt  # InputStatement
    | printStmt  # PrintStatement
    | letStmt    # LetStatement
    ;

// Comandos
inputStmt: INPUT ID NEWLINE;
printStmt: PRINT exprList NEWLINE;
letStmt: LET ID '=' expr NEWLINE;
exprList: expr (',' expr)*;
expr: term (('+' | '-') term)* ;
term: factor (('*' | '/') factor)* ;
factor: NUMBER                     # Number
      | STRING                     # String
      | ID                         # Variable
      | '(' expr ')'               # Parentheses
      ;

// Tokens (Lexer) - A ORDEM IMPORTA!
// Regras de Skip devem vir primeiro ou ter alta prioridade implícita.
WS: [ \t]+ -> skip;
LINE_COMMENT: 'REM' ~[\r\n]* -> skip; // << COMENTÁRIO REM IGNORADO

// Palavras-chave explícitas
INPUT: 'INPUT';
PRINT: 'PRINT';
LET: 'LET';
// Não precisamos de um token REM separado se ele só introduz comentários skippados

// Tokens gerais (ID deve vir depois de palavras-chave e padrões mais específicos)
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n"])*? '"';

NEWLINE: '\r'? '\n' | ';';
