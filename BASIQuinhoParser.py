# Generated from BASIQuinho.g4 by ANTLR 4.13.2
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
        4,1,17,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,4,0,26,8,0,
        11,0,12,0,27,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,1,1,1,1,
        3,1,41,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,6,1,6,1,6,5,6,68,8,6,
        10,6,12,6,71,9,6,1,7,1,7,1,7,5,7,76,8,7,10,7,12,7,79,9,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,88,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,
        2,1,0,3,4,1,0,5,6,91,0,25,1,0,0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,46,
        1,0,0,0,8,50,1,0,0,0,10,56,1,0,0,0,12,64,1,0,0,0,14,72,1,0,0,0,16,
        87,1,0,0,0,18,20,5,17,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,
        0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,26,3,2,1,0,25,21,
        1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,32,1,0,0,0,
        29,31,5,17,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,
        0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,
        41,3,4,2,0,38,41,3,6,3,0,39,41,3,8,4,0,40,37,1,0,0,0,40,38,1,0,0,
        0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,11,0,0,43,44,5,14,0,0,44,45,
        5,17,0,0,45,5,1,0,0,0,46,47,5,12,0,0,47,48,3,10,5,0,48,49,5,17,0,
        0,49,7,1,0,0,0,50,51,5,13,0,0,51,52,5,14,0,0,52,53,5,1,0,0,53,54,
        3,12,6,0,54,55,5,17,0,0,55,9,1,0,0,0,56,61,3,12,6,0,57,58,5,2,0,
        0,58,60,3,12,6,0,59,57,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,
        1,0,0,0,62,11,1,0,0,0,63,61,1,0,0,0,64,69,3,14,7,0,65,66,7,0,0,0,
        66,68,3,14,7,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,
        0,0,0,70,13,1,0,0,0,71,69,1,0,0,0,72,77,3,16,8,0,73,74,7,1,0,0,74,
        76,3,16,8,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,
        0,0,78,15,1,0,0,0,79,77,1,0,0,0,80,88,5,15,0,0,81,88,5,16,0,0,82,
        88,5,14,0,0,83,84,5,7,0,0,84,85,3,12,6,0,85,86,5,8,0,0,86,88,1,0,
        0,0,87,80,1,0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,88,17,
        1,0,0,0,8,21,27,32,40,61,69,77,87
    ]

class BASIQuinhoParser ( Parser ):

    grammarFileName = "BASIQuinho.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "','", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'INPUT'", 
                     "'PRINT'", "'LET'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "LINE_COMMENT", "INPUT", "PRINT", 
                      "LET", "ID", "NUMBER", "STRING", "NEWLINE" ]

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
    WS=9
    LINE_COMMENT=10
    INPUT=11
    PRINT=12
    LET=13
    ID=14
    NUMBER=15
    STRING=16
    NEWLINE=17

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BASIQuinhoParser.NEWLINE)
            else:
                return self.getToken(BASIQuinhoParser.NEWLINE, i)

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
            self.state = 25 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==17:
                        self.state = 18
                        self.match(BASIQuinhoParser.NEWLINE)
                        self.state = 23
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 24
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 27 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 29
                self.match(BASIQuinhoParser.NEWLINE)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = BASIQuinhoParser.InputStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.inputStmt()
                pass
            elif token in [12]:
                localctx = BASIQuinhoParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.printStmt()
                pass
            elif token in [13]:
                localctx = BASIQuinhoParser.LetStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
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
            self.state = 42
            self.match(BASIQuinhoParser.INPUT)
            self.state = 43
            self.match(BASIQuinhoParser.ID)
            self.state = 44
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
            self.state = 46
            self.match(BASIQuinhoParser.PRINT)
            self.state = 47
            self.exprList()
            self.state = 48
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
            self.state = 50
            self.match(BASIQuinhoParser.LET)
            self.state = 51
            self.match(BASIQuinhoParser.ID)
            self.state = 52
            self.match(BASIQuinhoParser.T__0)
            self.state = 53
            self.expr()
            self.state = 54
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
            self.state = 56
            self.expr()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 57
                self.match(BASIQuinhoParser.T__1)
                self.state = 58
                self.expr()
                self.state = 63
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
            self.state = 64
            self.term()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 65
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.term()
                self.state = 71
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
            self.state = 72
            self.factor()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 73
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 74
                self.factor()
                self.state = 79
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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = BASIQuinhoParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(BASIQuinhoParser.NUMBER)
                pass
            elif token in [16]:
                localctx = BASIQuinhoParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(BASIQuinhoParser.STRING)
                pass
            elif token in [14]:
                localctx = BASIQuinhoParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(BASIQuinhoParser.ID)
                pass
            elif token in [7]:
                localctx = BASIQuinhoParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.match(BASIQuinhoParser.T__6)
                self.state = 84
                self.expr()
                self.state = 85
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





