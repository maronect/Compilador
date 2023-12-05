from ply import yacc
from AnalisadorLexico import tokens

def p_Programa(p):
    '''
    Programa : Declaracao
                | Declaracao Programa
    '''
# Declaracao
def p_Declaracao(p):
    '''
    Declaracao : DeclaracaoVariavel
            | DeclaracaoFuncao
            | DeclaracaoEstrutura
            | COMMENTLINE
    '''

def p_Declaracao_Variavel(p):
    '''
    DeclaracaoVariavel : TIPO ID SEMICOLLON
                        | TIPO ID EQUALS Expressao SEMICOLLON
    '''

def p_DeclaracaoFuncao(p):
    'DeclaracaoFuncao : TIPO ID LPAREN Parametros RPAREN Bloco'

def p_Bloco(p):
    '''
        Bloco : LBRACKET Declaracao RBRACKET

    '''

def p_Parametros(p):
    '''
    Parametros : Parametro
            | Parametro COMMA Parametros
    '''

def p_Parametro(p):
    '''Parametro : TIPO ID
                | TIPO ID LBRACKET RBRACKET
                | TIPO ID ELLIPSIS ID
                '''

def p_DeclaracaoEstrutura(p):

    '''
        DeclaracaoEstrutura : LBRACKET DeclaracaoVariavel RBRACKET SEMICOLLON

    '''

def p_Declaracao_Variavel(p):
    '''
    DeclaracaoVariavel : TIPO ID SEMICOLLON
                        | TIPO ID EQUALS Expressao SEMICOLLON
    '''

def p_Expressao(p):
    '''
        Expressao : ExpressaoLogica
                    | Atribuicao
    '''

def p_Atribuicao(p):
    '''

        Atribuicao : ID EQUALS Expressao
                    | ID PLUSEQUAL Expressao
                    | ID MINUSEQUAL Expressao
                    | ID TIMESEQUAL Expressao
                    | ID DIVEQUAL Expressao
                    | ID MODEQUAL Expressao
                    | ID ANDANDEQUAL Expressao
                    | ID OROREQUAL Expressao

    '''

def p_ExpressaoLogica(p):

    '''
    ExpressaoLogica : ExpressaoRelacional
                    | ExpressaoLogica OR ExpressaoRelacional
                    | ExpressaoLogica AND ExpressaoRelacional
                    | NOT ExpressaoRelacional
    '''

def p_ExpressaoRelacional(p):
    '''
    ExpressaoRelacional : ExpressaoAritmetica
                        | ExpressaoAritmetica GREATER ExpressaoAritmetica
                        | ExpressaoAritmetica LESSER ExpressaoAritmetica
                        | ExpressaoAritmetica GREATEREQUAL ExpressaoAritmetica
                        | ExpressaoAritmetica LESSEREQUAL ExpressaoAritmetica
                        | ExpressaoAritmetica NOTEQUAL ExpressaoAritmetica
                        | ExpressaoAritmetica EQUALTO ExpressaoAritmetica

    '''

def p_ExpressaoAritmetica(p):

    '''
    ExpressaoAritmetica : ExpressaoMultiplicativa
                        | ExpressaoAritmetica PLUS ExpressaoMultiplicativa
                        | ExpressaoAritmetica MINUS ExpressaoMultiplicativa
    '''

def p_ExpressaoMultiplicativa(p):
    '''
    ExpressaoMultiplicativa : ExpressaoUnaria
                             | ExpressaoMultiplicativa TIMES ExpressaoUnaria
                             | ExpressaoMultiplicativa DIVIDE ExpressaoUnaria
                             | ExpressaoMultiplicativa MOD ExpressaoUnaria

    '''

def p_ExpressaoUnaria(p):
    '''
    ExpressaoUnaria : ExpressaoPostfix
                    | MINUS ExpressaoPostfix
                    | PLUS PLUS ExpressaoPostfix
                    | MINUS MINUS ExpressaoPostfix
    '''

def p_ExpressaoPostfix(p):
    '''
    ExpressaoPostfix : Primaria
                    | Primaria LBRACKET Expressao RBRACKET
                    | Primaria LPAREN Argumentos RPAREN
                    | Primaria DOT ID
                    | Primaria ARROW ID
    '''

def p_Primaria(p):
   '''
   Primaria : ID
            | NUM_INT
            | NUM_DEC
            | TEXTO
            | LPAREN Expressao LPAREN
   '''

def p_Argumentos(p):
    '''
        Argumentos :
    '''

# Manipulador de erros
def p_error(p):
    print("Erro de sintaxe")

# Criar o analisador sintático
parser = yacc.yacc()
