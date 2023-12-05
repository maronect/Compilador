from AnalisadorLexico import lexer
data = '''// Este é um comentário de linha.
    String teste = "tatu";
    int dobrar(int x) {
    return x * 2;
    }'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)