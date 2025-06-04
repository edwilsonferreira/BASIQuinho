# Generated from ./BASIQuinho.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,78,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,5,5,48,8,5,10,5,12,5,51,9,5,1,6,1,6,1,6,5,6,56,8,
        6,10,6,12,6,59,9,6,1,7,1,7,1,7,5,7,64,8,7,10,7,12,7,67,9,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,76,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,
        0,2,1,0,3,4,1,0,5,6,77,0,19,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,
        34,1,0,0,0,8,38,1,0,0,0,10,44,1,0,0,0,12,52,1,0,0,0,14,60,1,0,0,
        0,16,75,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,
        29,3,4,2,0,26,29,3,6,3,0,27,29,3,8,4,0,28,25,1,0,0,0,28,26,1,0,0,
        0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,9,0,0,31,32,5,12,0,0,32,33,
        5,15,0,0,33,5,1,0,0,0,34,35,5,10,0,0,35,36,3,10,5,0,36,37,5,15,0,
        0,37,7,1,0,0,0,38,39,5,11,0,0,39,40,5,12,0,0,40,41,5,1,0,0,41,42,
        3,12,6,0,42,43,5,15,0,0,43,9,1,0,0,0,44,49,3,12,6,0,45,46,5,2,0,
        0,46,48,3,12,6,0,47,45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,11,1,0,0,0,51,49,1,0,0,0,52,57,3,14,7,0,53,54,7,0,0,0,
        54,56,3,14,7,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,
        0,0,0,58,13,1,0,0,0,59,57,1,0,0,0,60,65,3,16,8,0,61,62,7,1,0,0,62,
        64,3,16,8,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,
        0,0,66,15,1,0,0,0,67,65,1,0,0,0,68,76,5,13,0,0,69,76,5,14,0,0,70,
        76,5,12,0,0,71,72,5,7,0,0,72,73,3,12,6,0,73,74,5,8,0,0,74,76,1,0,
        0,0,75,68,1,0,0,0,75,69,1,0,0,0,75,70,1,0,0,0,75,71,1,0,0,0,76,17,
        1,0,0,0,6,21,28,49,57,65,75
    ]

class BASIQuinhoParser ( Parser ):

    grammarFileName = "BASIQuinho.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "','", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "'INPUT'", "'PRINT'", "'LET'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INPUT", "PRINT", "LET", "ID", "NUMBER", 
                      "STRING", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_inputStmt = 2
    RULE_printStmt = 3
    RULE_letStmt = 4
    RULE_exprList = 5
    RULE_expr = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "prog", "stmt", "inputStmt", "printStmt", "letStmt", 
                   "exprList", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INPUT=9
    PRINT=10
    LET=11
    ID=12
    NUMBER=13
    STRING=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BASIQuinhoParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BASIQuinhoParser.StmtContext)
            else:
                return self.getTypedRuleContext(BASIQuinhoParser.StmtContext,i)


        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = BASIQuinhoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stmt()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    break

            self.state = 23
            self.match(BASIQuinhoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStmt(self):
            return self.getTypedRuleContext(BASIQuinhoParser.PrintStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)


    class InputStatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def inputStmt(self):
            return self.getTypedRuleContext(BASIQuinhoParser.InputStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)


    class LetStatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def letStmt(self):
            return self.getTypedRuleContext(BASIQuinhoParser.LetStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStatement" ):
                listener.enterLetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStatement" ):
                listener.exitLetStatement(self)



    def stmt(self):

        localctx = BASIQuinhoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = BASIQuinhoParser.InputStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.inputStmt()
                pass
            elif token in [10]:
                localctx = BASIQuinhoParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.printStmt()
                pass
            elif token in [11]:
                localctx = BASIQuinhoParser.LetStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.letStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(BASIQuinhoParser.INPUT, 0)

        def ID(self):
            return self.getToken(BASIQuinhoParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(BASIQuinhoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)




    def inputStmt(self):

        localctx = BASIQuinhoParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(BASIQuinhoParser.INPUT)
            self.state = 31
            self.match(BASIQuinhoParser.ID)
            self.state = 32
            self.match(BASIQuinhoParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BASIQuinhoParser.PRINT, 0)

        def exprList(self):
            return self.getTypedRuleContext(BASIQuinhoParser.ExprListContext,0)


        def NEWLINE(self):
            return self.getToken(BASIQuinhoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = BASIQuinhoParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(BASIQuinhoParser.PRINT)
            self.state = 35
            self.exprList()
            self.state = 36
            self.match(BASIQuinhoParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(BASIQuinhoParser.LET, 0)

        def ID(self):
            return self.getToken(BASIQuinhoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BASIQuinhoParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(BASIQuinhoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_letStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt" ):
                listener.enterLetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt" ):
                listener.exitLetStmt(self)




    def letStmt(self):

        localctx = BASIQuinhoParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_letStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(BASIQuinhoParser.LET)
            self.state = 39
            self.match(BASIQuinhoParser.ID)
            self.state = 40
            self.match(BASIQuinhoParser.T__0)
            self.state = 41
            self.expr()
            self.state = 42
            self.match(BASIQuinhoParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BASIQuinhoParser.ExprContext)
            else:
                return self.getTypedRuleContext(BASIQuinhoParser.ExprContext,i)


        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)




    def exprList(self):

        localctx = BASIQuinhoParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.expr()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 45
                self.match(BASIQuinhoParser.T__1)
                self.state = 46
                self.expr()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BASIQuinhoParser.TermContext)
            else:
                return self.getTypedRuleContext(BASIQuinhoParser.TermContext,i)


        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = BASIQuinhoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.term()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 53
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.term()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BASIQuinhoParser.FactorContext)
            else:
                return self.getTypedRuleContext(BASIQuinhoParser.FactorContext,i)


        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = BASIQuinhoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.factor()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 61
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self.factor()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BASIQuinhoParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BASIQuinhoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class NumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(BASIQuinhoParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)


    class StringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BASIQuinhoParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class ParenthesesContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BASIQuinhoParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BASIQuinhoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)



    def factor(self):

        localctx = BASIQuinhoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = BASIQuinhoParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(BASIQuinhoParser.NUMBER)
                pass
            elif token in [14]:
                localctx = BASIQuinhoParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(BASIQuinhoParser.STRING)
                pass
            elif token in [12]:
                localctx = BASIQuinhoParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(BASIQuinhoParser.ID)
                pass
            elif token in [7]:
                localctx = BASIQuinhoParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(BASIQuinhoParser.T__6)
                self.state = 72
                self.expr()
                self.state = 73
                self.match(BASIQuinhoParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





