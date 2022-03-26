# Generated from ut.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\4\3\4\5\4\35\n\4\3\4\3\4\3\4\3\4\3\4\5\4$\n\4\5\4&\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62\13")
        buf.write("\5\5\5\64\n\5\3\5\3\5\3\5\7\59\n\5\f\5\16\5<\13\5\3\6")
        buf.write("\3\6\3\6\7\6A\n\6\f\6\16\6D\13\6\5\6F\n\6\3\6\2\4\4\b")
        buf.write("\7\2\4\6\b\n\2\2\2L\2\f\3\2\2\2\4\17\3\2\2\2\6%\3\2\2")
        buf.write("\2\b\63\3\2\2\2\nE\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16")
        buf.write("\3\3\2\2\2\17\20\b\3\1\2\20\21\5\6\4\2\21\27\3\2\2\2\22")
        buf.write("\23\f\3\2\2\23\24\7\5\2\2\24\26\5\4\3\4\25\22\3\2\2\2")
        buf.write("\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\5\3\2\2")
        buf.write("\2\31\27\3\2\2\2\32\34\5\n\6\2\33\35\5\b\5\2\34\33\3\2")
        buf.write("\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36\37\7\5\2\2\37 \5\6")
        buf.write("\4\2 &\3\2\2\2!#\5\n\6\2\"$\5\b\5\2#\"\3\2\2\2#$\3\2\2")
        buf.write("\2$&\3\2\2\2%\32\3\2\2\2%!\3\2\2\2&\7\3\2\2\2\'(\b\5\1")
        buf.write("\2()\7\4\2\2)*\7\5\2\2*\64\7\4\2\2+\64\7\4\2\2,\60\7\4")
        buf.write("\2\2-/\7\4\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61")
        buf.write("\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\63\'\3\2\2\2\63+")
        buf.write("\3\2\2\2\63,\3\2\2\2\64:\3\2\2\2\65\66\f\6\2\2\66\67\7")
        buf.write("\5\2\2\679\5\b\5\78\65\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3")
        buf.write("\2\2\2;\t\3\2\2\2<:\3\2\2\2=F\7\3\2\2>B\7\3\2\2?A\7\3")
        buf.write("\2\2@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CF\3\2\2\2")
        buf.write("DB\3\2\2\2E=\3\2\2\2E>\3\2\2\2F\13\3\2\2\2\13\27\34#%")
        buf.write("\60\63:BE")
        return buf.getvalue()


class utParser ( Parser ):

    grammarFileName = "ut.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NOUN", "COURSE", "CONDITIONAL", "SPACE" ]

    RULE_parse = 0
    RULE_expression = 1
    RULE_clist = 2
    RULE_courses = 3
    RULE_major = 4

    ruleNames =  [ "parse", "expression", "clist", "courses", "major" ]

    EOF = Token.EOF
    NOUN=1
    COURSE=2
    CONDITIONAL=3
    SPACE=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(utParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(utParser.EOF, 0)

        def getRuleIndex(self):
            return utParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = utParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression(0)
            self.state = 11
            self.match(utParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clist(self):
            return self.getTypedRuleContext(utParser.ClistContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(utParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(utParser.ExpressionContext,i)


        def CONDITIONAL(self):
            return self.getToken(utParser.CONDITIONAL, 0)

        def getRuleIndex(self):
            return utParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = utParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.clist()
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = utParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 16
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 17
                    self.match(utParser.CONDITIONAL)
                    self.state = 18
                    self.expression(2) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ClistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def major(self):
            return self.getTypedRuleContext(utParser.MajorContext,0)


        def CONDITIONAL(self):
            return self.getToken(utParser.CONDITIONAL, 0)

        def clist(self):
            return self.getTypedRuleContext(utParser.ClistContext,0)


        def courses(self):
            return self.getTypedRuleContext(utParser.CoursesContext,0)


        def getRuleIndex(self):
            return utParser.RULE_clist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClist" ):
                listener.enterClist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClist" ):
                listener.exitClist(self)




    def clist(self):

        localctx = utParser.ClistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_clist)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.major()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==utParser.COURSE:
                    self.state = 25
                    self.courses(0)


                self.state = 28
                self.match(utParser.CONDITIONAL)
                self.state = 29
                self.clist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.major()
                self.state = 33
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.courses(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoursesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COURSE(self, i:int=None):
            if i is None:
                return self.getTokens(utParser.COURSE)
            else:
                return self.getToken(utParser.COURSE, i)

        def CONDITIONAL(self):
            return self.getToken(utParser.CONDITIONAL, 0)

        def courses(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(utParser.CoursesContext)
            else:
                return self.getTypedRuleContext(utParser.CoursesContext,i)


        def getRuleIndex(self):
            return utParser.RULE_courses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourses" ):
                listener.enterCourses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourses" ):
                listener.exitCourses(self)



    def courses(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = utParser.CoursesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_courses, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(utParser.COURSE)
                self.state = 39
                self.match(utParser.CONDITIONAL)
                self.state = 40
                self.match(utParser.COURSE)
                pass

            elif la_ == 2:
                self.state = 41
                self.match(utParser.COURSE)
                pass

            elif la_ == 3:
                self.state = 42
                self.match(utParser.COURSE)
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 43
                        self.match(utParser.COURSE) 
                    self.state = 48
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = utParser.CoursesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_courses)
                    self.state = 51
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 52
                    self.match(utParser.CONDITIONAL)
                    self.state = 53
                    self.courses(5) 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MajorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self, i:int=None):
            if i is None:
                return self.getTokens(utParser.NOUN)
            else:
                return self.getToken(utParser.NOUN, i)

        def getRuleIndex(self):
            return utParser.RULE_major

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMajor" ):
                listener.enterMajor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMajor" ):
                listener.exitMajor(self)




    def major(self):

        localctx = utParser.MajorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_major)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(utParser.NOUN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(utParser.NOUN)
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 61
                        self.match(utParser.NOUN) 
                    self.state = 66
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        self._predicates[3] = self.courses_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def courses_sempred(self, localctx:CoursesContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




