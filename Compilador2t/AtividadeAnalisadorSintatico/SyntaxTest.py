from AnalisadorLexico import lexer
from AnalisadorSintatico import parser

def main():
    data = '''int A; 
            double nota = 10.00;
            String empenho = "total";
            // Trabalho muito bom. Inegavel!
            / Olha so como funciona
            int errando = 0
            String concluindo = "É 10";
            '''

    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    print(f"Resultado da expressão: {result}")
#dando erro c string
if __name__ == "__main__":
    main()
