import ply.yacc as yacc
import ply.lex as lex
from Lexer import *

def p_statement_assign(p):
    'statement : CAT_ID PURR expression FUR'
    p[0] = ('ASSIGN', p[1], p[3])
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
    p[0] = ('BINOP', p[2], p[1], p[3])
def p_expression_group(p):
    'expression : PAW expression HISS'
    p[0] = p[2]
def p_expression_number(p):
    '''expression : CAT_INT
                  | FELINE
                  | CAT_ID'''
    p[0] = ('NUM', p[1])
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

def generate_code(node):
    global temp_count
    global label_count
    if isinstance(node, tuple):
        op = node[0]
        if op == 'ASSIGN':
            print(f"{node[3]} = {generate_code(node[1])}")
        elif op in ['MEOW', 'CLAW', 'WHISKER', 'FURBALL', 'CAT_LT', 'PURRER', 'CLAWED', 'CAT_GE', 'CAT_EQ', 'CATLIKE']:
            left = generate_code(node[1])
            right = generate_code(node[2])
            t3 = f"t{temp_count}"
            print(f"{t3} = {left} {op} {right}")
            temp_count += 1
            return t3
        elif op == 'IF':
            cond_code = generate_code(node[1])
            label1 = f"L{label_count}"
            print(f"if {cond_code} goto {label1}")
            label_count += 1
            print(f"{label1}:")
            generate_code(node[2])
        elif op == 'IFELSE':
            true_label = f"L{label_count}"
            label_count += 1
            false_label = f"L{label_count}"
            label_count += 1
            else_label = f"L{label_count}"
            label_count += 1
            cond_code = generate_code(node[1])
            print(f"if {cond_code} goto {true_label}")
            print(f"goto {false_label}")
            print(f"{true_label}:")
            generate_code(node[2])
            print(f"goto {else_label}")
            print(f"{false_label}:")
            generate_code(node[3])
            print(f"{else_label}:")
        elif op == 'WHILE':
            start_label = f"L{label_count}"
            label_count += 1
            end_label = f"L{label_count}"
            label_count += 1
            print(f"{start_label}:")
            cond_code = generate_code(node[1])
            print(f"ifFalse {cond_code} goto {end_label}")
            generate_code(node[2])
            print(f"goto {start_label}")
            print(f"{end_label}:")
        elif op == 'PRINT':
            print(f"print {generate_code(node[1])}")
        else:
            raise Exception(f"Unrecognized operation: {op}")
    else:
        return node

parser = yacc.yacc()
lexer = lex.lex()

if __name__ == "__main__":
    print("Enter your code (type 'end' on a new line to finish):")
    user_input_lines = []
    while True:
        line = input()
        if line == "end":  
            break
        user_input_lines.append(line)
    user_input_code = '\n'.join(user_input_lines)

    lexer.input(user_input_code)

    while True:
        tok = lexer.token()
        if not tok:
            break 
        print("Token[", tok.type, "]        [", tok.value, "]")