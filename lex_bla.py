import ply.lex as lex
import sys

tokens = (
    'ID',
    'BINARY_LITERAL',
    'EQUALS',
    'WHITESPACE',
    'COMMENT',
    'A',
    'S',
    'M',
    'D',
    'LEFT_BRACKET',
    'RIGHT_BRACKET'
)

def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    t.value = "ID," + t.value
    return t

def t_BINARY_LITERAL(t):
    r'[+-]*[01]+'
    t.value = "BINARY_LITERAL," + t.value
    return t

def t_EQUALS(t):
    r'='
    t.value = "="
    return t

def t_WHITESPACE(t):
    r'\s+'
    t.value = "WHITESPACE"
    return t

def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    t.value = "COMMENT" + t.value
    return t

def t_A(t):
    r'A'
    return t

def t_S(t):
    r'S'
    return t

def t_M(t):
    r'M'
    return t

def t_D(t):
    r'D'
    return t


def t_LEFT_BRACKET(t):
    r'\('
    return t

def t_RIGHT_BRACKET(t):
    r'\)'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    #t.value = "ILLEGAL, " + t.value
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

#read in file
fileName = sys.argv[1]
blaFile = open(f"{fileName}", "r")
data = blaFile.read()


#lex
lexer.input(data)
for tok in lexer:
    print(tok.value)
    #tknFile.write(tok.value + "\n")

blaFile.close()