import ply.yacc as yacc
import sys

from lex_bla import tokens

def p_program(p):
    'Program : Statement'
    p[0] = ('program', p[1], p[2], p[3])

def p_statement(p):
    'Statement : Identifier EQUALS Expression'

def p_expression(p):
    '''Expression : Expression A Term
                | Expression S Term
                | Term
    
    '''

def p_term(p):
    '''
    Term : Term M Factor
        | Term D Factor
        | Factor
    '''

def p_factor(p):
    '''
    Factor : LEFT_BRACKET Expression RIGHT_BRACKET
            | Identifier
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       #s = raw_input('calc > ')
       pass
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
