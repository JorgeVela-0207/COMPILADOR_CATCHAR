from Lexer import lexer
from Sintactico import parser

temp_count = 0
label_count = 0

def new_temp():
    global temp_count
    name = f"t{temp_count}"
    temp_count += 1
    return name

def new_label():
    global label_count
    name = f"L{label_count}"
    label_count += 1
    return name

def generate_code(node):
    if isinstance(node, tuple):
        op = node[0]
        if op == 'ASSIGN':
            value = generate_code(node[2])
            print(f"{node[1]} = {value}")
        elif op == 'BINOP':
            left = generate_code(node[2])
            right = generate_code(node[3])
            temp = new_temp()
            print(f"{temp} = {left} {node[1]} {right}")
            return temp
        elif op == 'IF':
            cond = generate_code(node[1])
            true_label = new_label()
            end_label = new_label()
            print(f"if {cond}: goto {true_label}")
            print(f"goto {end_label}")
            print(f"{true_label}:")
            generate_code(node[2]) 
            print(f"{end_label}:")
        elif op == 'WHILE':
            start_label = new_label()
            cond_label = new_label()
            print(f"goto {cond_label}")
            print(f"{start_label}:")
            generate_code(node[2])  
            print(f"{cond_label}:")
            cond = generate_code(node[1])
            print(f"while {cond}: goto {start_label}")
        elif op == 'NUM':
            return node[1]
    else:
        return node
data = '''
a = 3;
b = 5;
if (a < b) {
    a = a + 1;
} else {
    b = b - 1;
}
while (a < b) {
    a = a + 1;
}
'''

ast = parser.parse(data)

generate_code(ast)