grammar ut;

parse
    : expression EOF
    ;

expression
    : clist
    | expression CONDITIONAL expression
    ;

clist
    : major courses? CONDITIONAL clist
    | major courses?
    ;

courses
    : courses CONDITIONAL courses
    | COURSE CONDITIONAL COURSE
    | COURSE
    | COURSE(COURSE)*
    ;

major
    : NOUN
    | NOUN(NOUN)*
    ;

NOUN        : [A-Z][a-z]+;
COURSE      : [0-9][0-9][0-9][A-Z]?;
CONDITIONAL : 'and' | 'or';
SPACE       : [ \t\r\n]+ -> skip;
