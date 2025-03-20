import ply.yacc as yacc
import lex_bla
import sys

from lex_bla import tokens

def p_program(p):
    '''Program : Program Statement
               | Statement'''
    if len(p) == 3:
        p[0] = ('Program',) + p[1][1:] + (p[2],) 
    else:
        p[0] = ('Program', p[1])

def p_statement(p):
    'Statement : ID EQUALS Expression'
    p[0] = ('=', p[1], p[3]) 

def p_expression_binop(p):
    '''Expression : Expression A Term
                  | Expression S Term'''
    p[0] = (p[2], p[1], p[3])  


def p_expression_term(p):
    'Expression : Term'
    p[0] = p[1]  

def p_term_binop(p):
    '''Term : Term M Factor
            | Term D Factor'''
    p[0] = (p[2], p[1], p[3])  


def p_term_factor(p):
    'Term : Factor'
    p[0] = p[1]  


def p_factor_paren(p):
    'Factor : LEFT_BRACKET Expression RIGHT_BRACKET'
    p[0] = (p[2])  


def p_factor_binary(p):
    'Factor : BINARY_LITERAL'
    p[0] = ( p[1])  


def p_factor_id(p):
    'Factor : ID'
    p[0] = (p[1])  


def p_empty(p):
    'empty :'
    p[0] = None

def p_error(p):
    pass

# Build parser
parser = yacc.yacc()

# Test input
s = ''' 
calc1=10A01
calc2=111S100D10
calc3=1000M10S(1111D11)A1000
'''





def format_program(program):
    output = []
    for line in program:
        if isinstance(line, str):
            output.append(line)
        elif isinstance(line, tuple):
            output.append("    =")
            output.append("        " + line[1])
            format_expression(line[2], output, 3)
    return "\n".join(output)

def format_expression(expression, output, indent):
    if isinstance(expression, str):
        output.append("    " * indent + expression)
    elif isinstance(expression, tuple):
        output.append("    " * indent + expression[0])
        for child in expression[1:]:
            format_expression(child, output, indent + 1)





fileName = sys.argv[1]
blaFile = open(f"{fileName}", "r")
data = blaFile.read()

#create or write to file
fileName = fileName.removesuffix(".bla")
astFile = open(f"{fileName}.ast","w")

result = parser.parse(data, lexer=lex_bla.lexer)
formatted_output = format_program(result)
astFile.write(formatted_output)

print(formatted_output)

