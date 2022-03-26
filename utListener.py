# Generated from ut.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .utParser import utParser
else:
    from utParser import utParser

from functools import reduce

# This class defines a complete listener for a parse tree produced by utParser.
class utListener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.tree = {}
        self.stack = []

    # Enter a parse tree produced by utParser#parse.
    def enterParse(self, ctx:utParser.ParseContext):
        pass

    # Exit a parse tree produced by utParser#parse.
    def exitParse(self, ctx:utParser.ParseContext):
        pass

    # Enter a parse tree produced by utParser#expression.
    def enterExpression(self, ctx:utParser.ExpressionContext):
        pass

    # Exit a parse tree produced by utParser#expression.
    def exitExpression(self, ctx:utParser.ExpressionContext):
        pass

    # Enter a parse tree produced by utParser#clist.
    def enterClist(self, ctx:utParser.ClistContext):
        # major = reduce(lambda a, b: f"{a} {b}", [x.getText() for x in ctx.major().children])
        # if major not in self.tree:
        #     self.tree[major] = []
        pass
        
    # Exit a parse tree produced by utParser#clist.
    def exitClist(self, ctx:utParser.ClistContext):
        major = reduce(lambda a, b: f"{a} {b}", [x.getText() for x in ctx.major().children])
        condKey = {"or": "ANY", "and": "ALL"}
        if major not in self.tree:
            self.tree[major] = []
        
        courseCtx = ctx.courses()
        courses = [x.getText() for x in courseCtx.COURSE()]
        
        if courseCtx.CONDITIONAL():
            cond = courseCtx.CONDITIONAL().getText()
            for dCourses in courseCtx.courses():
                if dCourses.CONDITIONAL():
                    dCond = dCourses.CONDITIONAL().getText()
                    courses += [{condKey[dCond]: [x.getText() for x in dCourses.COURSE()]}]
                else:
                    courses += [x.getText() for x in dCourses.COURSE()]
            if cond == "or":
                courses = {condKey[cond]: courses}
            else:
                courses = {condKey[cond]: courses}

        rule = {}
        if ctx.CONDITIONAL():
            cond = ctx.CONDITIONAL().getText()
            if ctx.clist():
                if cond == "or":
                    rule["ANY"] = [self.tree[major], courses] if len(self.tree[major]) > 0 else courses
                elif cond == "and":
                    rule["ALL"] = [self.tree[major], courses] if len(self.tree[major]) > 0 else courses
        else:
            rule = {"ALL": courses}

        self.tree[major] = rule


    # Enter a parse tree produced by utParser#courses.
    def enterCourses(self, ctx:utParser.CoursesContext):
        pass

    # Exit a parse tree produced by utParser#courses.
    def exitCourses(self, ctx:utParser.CoursesContext):
        pass

    # Enter a parse tree produced by utParser#major.
    def enterMajor(self, ctx:utParser.MajorContext):
        pass

    # Exit a parse tree produced by utParser#major.
    def exitMajor(self, ctx:utParser.MajorContext):
        pass

del utParser