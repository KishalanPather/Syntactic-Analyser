import ply.yacc as yacc
import sys
import lex_bla

from lex_bla import tokens

def p_program(p):
    '''Program : Statement Program
                | Statement
        '''
    p[0] = ('Program')
    for i in p:
        print(i)

def p_statement(p):
    'Statement : ID EQUALS Expression'
    p[0] = ('statement',p[1], p[2], p[3])

def p_expression(p):
    '''Expression : Expression A Term
                | Expression S Term
    '''
    p[0] = ('expression', p[1], p[2], p[3])

def p_expression_term(p):
    '''Expression : Term
    '''
    p[0] = ('expressionTerm', p[1])

def p_term(p):
    '''
    Term : Term M Factor
        | Term D Factor
    '''
    p[0] = ('term',p[1], p[2], p[3])

def p_term_factor(p):
    '''Term : Factor
    '''
    p[0] = ('TermFactor', p[1])

def p_factor(p):
    '''
    Factor : LEFT_BRACKET Expression RIGHT_BRACKET
    '''
    p[0] = ('factor', p[1], p[2], p[3])

def p_factor_binary(p):
    '''
    Factor : BINARY_LITERAL
    '''
    p[0] = ('factorBinary-literal', p[1])

def p_factor_id(p):
    '''Factor : ID
    '''
    p[0] = ('FactorID', p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

s = '''
/* doing some 
calculations */
val = 1100
result = val M (111000 S 110001) // answer

'''

result = parser.parse(s, lexer=lex_bla.lexer)
print("Result",result)


