# Generated from ./BASIQuinho.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BASIQuinhoParser import BASIQuinhoParser
else:
    from BASIQuinhoParser import BASIQuinhoParser

# This class defines a complete listener for a parse tree produced by BASIQuinhoParser.
class BASIQuinhoListener(ParseTreeListener):

    # Enter a parse tree produced by BASIQuinhoParser#prog.
    def enterProg(self, ctx:BASIQuinhoParser.ProgContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#prog.
    def exitProg(self, ctx:BASIQuinhoParser.ProgContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#InputStatement.
    def enterInputStatement(self, ctx:BASIQuinhoParser.InputStatementContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#InputStatement.
    def exitInputStatement(self, ctx:BASIQuinhoParser.InputStatementContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#PrintStatement.
    def enterPrintStatement(self, ctx:BASIQuinhoParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#PrintStatement.
    def exitPrintStatement(self, ctx:BASIQuinhoParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#LetStatement.
    def enterLetStatement(self, ctx:BASIQuinhoParser.LetStatementContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#LetStatement.
    def exitLetStatement(self, ctx:BASIQuinhoParser.LetStatementContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#inputStmt.
    def enterInputStmt(self, ctx:BASIQuinhoParser.InputStmtContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#inputStmt.
    def exitInputStmt(self, ctx:BASIQuinhoParser.InputStmtContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#printStmt.
    def enterPrintStmt(self, ctx:BASIQuinhoParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#printStmt.
    def exitPrintStmt(self, ctx:BASIQuinhoParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#letStmt.
    def enterLetStmt(self, ctx:BASIQuinhoParser.LetStmtContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#letStmt.
    def exitLetStmt(self, ctx:BASIQuinhoParser.LetStmtContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#exprList.
    def enterExprList(self, ctx:BASIQuinhoParser.ExprListContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#exprList.
    def exitExprList(self, ctx:BASIQuinhoParser.ExprListContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#expr.
    def enterExpr(self, ctx:BASIQuinhoParser.ExprContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#expr.
    def exitExpr(self, ctx:BASIQuinhoParser.ExprContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#term.
    def enterTerm(self, ctx:BASIQuinhoParser.TermContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#term.
    def exitTerm(self, ctx:BASIQuinhoParser.TermContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#Number.
    def enterNumber(self, ctx:BASIQuinhoParser.NumberContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#Number.
    def exitNumber(self, ctx:BASIQuinhoParser.NumberContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#String.
    def enterString(self, ctx:BASIQuinhoParser.StringContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#String.
    def exitString(self, ctx:BASIQuinhoParser.StringContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#Variable.
    def enterVariable(self, ctx:BASIQuinhoParser.VariableContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#Variable.
    def exitVariable(self, ctx:BASIQuinhoParser.VariableContext):
        pass


    # Enter a parse tree produced by BASIQuinhoParser#Parentheses.
    def enterParentheses(self, ctx:BASIQuinhoParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by BASIQuinhoParser#Parentheses.
    def exitParentheses(self, ctx:BASIQuinhoParser.ParenthesesContext):
        pass



del BASIQuinhoParser