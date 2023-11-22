import ply.yacc as yacc
from Lexer import tokens

def p_statement_assign(p):
    'statement : CAT_ID PURR expression FUR'
    p[0] = ('ASSIGN', p[3], "to", p[1])
def p_expression_binop(p):
    '''expression : expression MEOW expression
                  | expression CLAW expression
                  | expression WHISKER expression
                  | expression FURBALL expression
                  | expression CAT_LT expression
                  | expression PURRER expression
                  | expression CLAWED expression
                  | expression CAT_GE expression
                  | expression CAT_EQ expression
                  | expression CATLIKE expression'''
    p[0] = (p[2], p[1], p[3])
def p_expression_group(p):
    'expression : PAW expression HISS'
    p[0] = p[2]
def p_expression_number(p):
    '''expression : CAT_INT
                  | FELINE
                  | CAT_ID'''
    p[0] = p[1]
def p_statement_if(p):
    'statement : CAT_IF expression PURRING statements SCRATCH'
    p[0] = ('IF', p[2], p[4])

def p_statement_else(p):
    'statement : CAT_IF expression PURRING statements SCRATCH CAT_ELSE PURRING statements SCRATCH'
    p[0] = ('IFELSE', p[2], p[4], p[8])
def p_statement_while(p):
    'statement : CAT_WHILE expression PURRING statements SCRATCH'
    p[0] = ('WHILE', p[2], p[4])
def p_statement_print(p):
    'statement : CAT_PRINT expression FUR'
    p[0] = ('PRINT', p[2])
def p_statements(p):
    '''statements : statement
                  | statements statement'''

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_program(p):
    'statement : statement statement'
    p[0] = (p[1], p[2])

def p_error(p):
    print(f"SyntaxError: Incorrect syntax. Missing token before '{p.value}' on line {p.lineno-1}")


def p_empty(p):
    'empty :'
    pass
parser = yacc.yacc()