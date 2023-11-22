# main.py
from Lexer import lexer, tokens
from Sintactico import parser
from AnalizadorSemantico import generate_code

def main():
    source_code = read_source_code()
    if source_code is not None:
        lexer.input(source_code)
        while True:
            tok = lexer.token()
            if not tok:
                break  
            print(tok)

        # Una vez que los tokens han sido generados, pasamos el código fuente al parser.
        result = parser.parse(source_code)
        print("Resultado del análisis sintáctico:", result)

        # Llamada al generador de código semántico
        generate_code(result)
    else:
        print("No se pudo leer el código fuente.")

def read_source_code():
    try:
        with open('source_code.txt', 'r') as file:
            source_code = file.read()
        return source_code
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

if __name__ == "__main__":
    main()

# La pausa para evitar que la consola se cierre inmediatamente.
input("Presiona Enter para salir...")
