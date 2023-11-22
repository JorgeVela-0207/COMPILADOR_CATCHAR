import ply.lex as lex

keywords = {
    'if': 'CAT_IF',
    'else': 'CAT_ELSE',
    'while': 'CAT_WHILE',
    'print': 'CAT_PRINT'
}

tokens = [
             'PURR',
             'MEOW',
             'CLAW',
             'WHISKER',
             'FURBALL',
             'PAW',
             'HISS',
             'PURRING',
             'SCRATCH',
             'CAT_ID',
             'CAT_INT',
             'FELINE',
             'FUR',
             'CAT_LT',
             'PURRER',
             'CLAWED',
             'CAT_GE',
             'CAT_EQ',
             'CATLIKE',
             "NUMBER_LITERAL"
         ] + list(keywords.values())

t_PURR = r'\='
t_MEOW = r'\+'
t_CLAW = r'-'
t_WHISKER = r'\*'
t_FURBALL = r'\/'
t_PAW = r'\('
t_HISS = r'\)'
t_PURRING = r'\{'
t_SCRATCH = r'\}'
t_FELINE = r'\d+\.\d+'  
t_CAT_INT = r'\d+'  
t_FUR = r';'  
t_CAT_LT = r'<'  
t_PURRER = r'>'  
t_CLAWED = r'<\='  
t_CAT_GE = r'>\='  
t_CAT_EQ = r'=='  
t_CATLIKE = r'!='  
t_NUMBER_LITERAL = r"\b\d+\b"

def t_CAT_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'CAT_ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"SyntaxError: Invalid token '{t.value[0]}' at line {t.lineno - 1}")
    t.lexer.skip(1)

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