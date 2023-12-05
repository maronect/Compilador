from ply import lex

# Lista de tokens
tokens = (
'TIPO',
'NUM_INT',
'NUM_DEC',
'ID',
'TEXTO',
'EQUALS',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'MOD',
'AND',
'OR',
'NOT',
'GREATER',
'GREATEREQUAL',
'LESSER',
'LESSEREQUAL',
'NOTEQUAL',
'EQUALTO',
'PLUSEQUAL',
'MINUSEQUAL',
'TIMESEQUAL',
'DIVEQUAL',
'ANDANDEQUAL',
'OROREQUAL',
'MODEQUAL',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'LCURLY',
'RCURLY',
'COMMA',
'SEMICOLLON',
'COMMENTLINE',
'ARROW',
'DOT',
'EXPRESSAOLISTA',
'ELLIPSIS', # 3 pontos
)

# Regras para cada token
t_GREATEREQUAL = r'>='
t_LESSEREQUAL = r'<='
t_NOTEQUAL = r'!='
t_EQUALTO = r'=='
t_AND = r'&&'
t_OR = r'\|\|'
# Regras para token operador unico
t_EQUALS = r'='
t_MOD = r'%'
t_NOT = r'!'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_ANDANDEQUAL = r'&&='
t_OROREQUAL = r'\|\|='
t_GREATER = r'>'
t_LESSER = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COMMA = r','
t_SEMICOLLON = r';'
t_ELLIPSIS = r'\.\.\.'
t_DOT = r'.'
t_ARROW = r'->'


def t_TIPO(t):
    r'int|String|double|float|char|boolean'
    t.value = str(t.value)
    return t

def t_TEXTO(t):
    r'\"[^\"]*\"'
    return t

def t_ID(t):
    r'[a-zA-Zà-úÀ-Ú][a-zA-Z_0-9]*'
    t.value = str(t.value)
    return t

# Regra para ignorar comentario linha
def t_COMMENTLINE(t):
    r'//.*'
    return t

def t_NUM_DEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Regra para números inteiros
def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Ignorar caracteres em branco
t_ignore = ' \t\n'

# Manipulador de erros
def t_error(t):
    print(f"Caractere inesperado: {t.value[0]}")
    t.lexer.skip(1)


# Criar o analisador léxico
lexer = lex.lex()
