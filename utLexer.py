# Generated from ut.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("%\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\35\n\4\3\5\6\5 \n\5\r\5\16\5!\3\5\3\5\2\2")
        buf.write("\6\3\3\5\4\7\5\t\6\3\2\6\3\2C\\\3\2c|\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\2(\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\3\13\3\2\2\2\5\21\3\2\2\2\7\34\3\2\2\2\t\37\3")
        buf.write("\2\2\2\13\r\t\2\2\2\f\16\t\3\2\2\r\f\3\2\2\2\16\17\3\2")
        buf.write("\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\4\3\2\2\2\21\22\t\4")
        buf.write("\2\2\22\23\t\4\2\2\23\25\t\4\2\2\24\26\t\2\2\2\25\24\3")
        buf.write("\2\2\2\25\26\3\2\2\2\26\6\3\2\2\2\27\30\7c\2\2\30\31\7")
        buf.write("p\2\2\31\35\7f\2\2\32\33\7q\2\2\33\35\7t\2\2\34\27\3\2")
        buf.write("\2\2\34\32\3\2\2\2\35\b\3\2\2\2\36 \t\5\2\2\37\36\3\2")
        buf.write("\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\b\5")
        buf.write("\2\2$\n\3\2\2\2\7\2\17\25\34!\3\b\2\2")
        return buf.getvalue()


class utLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NOUN = 1
    COURSE = 2
    CONDITIONAL = 3
    SPACE = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NOUN", "COURSE", "CONDITIONAL", "SPACE" ]

    ruleNames = [ "NOUN", "COURSE", "CONDITIONAL", "SPACE" ]

    grammarFileName = "ut.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


