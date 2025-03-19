
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A BINARY_LITERAL COMMENT D EQUALS ID LEFT_BRACKET M RIGHT_BRACKET S WHITESPACEProgram : Statement Program\n| Statement\nStatement : ID EQUALS ExpressionExpression : Expression A Term\n| Expression S Term\nExpression : Term\n    \nTerm : Term M Factor\n    | Term D Factor\nTerm : Factor\n    \nFactor : LEFT_BRACKET Expression RIGHT_BRACKET\n\nFactor : BINARY_LITERAL\nFactor : ID\n    '
    
_lr_action_items = {'ID':([0,2,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,],[3,3,6,-12,-3,-6,-9,6,-11,6,6,6,6,-4,-5,-7,-8,-10,]),'$end':([1,2,4,6,7,8,9,11,17,18,19,20,21,],[0,-2,-1,-12,-3,-6,-9,-11,-4,-5,-7,-8,-10,]),'EQUALS':([3,],[5,]),'LEFT_BRACKET':([5,10,12,13,14,15,],[10,10,10,10,10,10,]),'BINARY_LITERAL':([5,10,12,13,14,15,],[11,11,11,11,11,11,]),'M':([6,8,9,11,17,18,19,20,21,],[-12,14,-9,-11,14,14,-7,-8,-10,]),'D':([6,8,9,11,17,18,19,20,21,],[-12,15,-9,-11,15,15,-7,-8,-10,]),'A':([6,7,8,9,11,16,17,18,19,20,21,],[-12,12,-6,-9,-11,12,-4,-5,-7,-8,-10,]),'S':([6,7,8,9,11,16,17,18,19,20,21,],[-12,13,-6,-9,-11,13,-4,-5,-7,-8,-10,]),'RIGHT_BRACKET':([6,8,9,11,16,17,18,19,20,21,],[-12,-6,-9,-11,21,-4,-5,-7,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,2,],[1,4,]),'Statement':([0,2,],[2,2,]),'Expression':([5,10,],[7,16,]),'Term':([5,10,12,13,],[8,8,17,18,]),'Factor':([5,10,12,13,14,15,],[9,9,9,9,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Statement Program','Program',2,'p_program','parse_bla.py',8),
  ('Program -> Statement','Program',1,'p_program','parse_bla.py',9),
  ('Statement -> ID EQUALS Expression','Statement',3,'p_statement','parse_bla.py',16),
  ('Expression -> Expression A Term','Expression',3,'p_expression','parse_bla.py',20),
  ('Expression -> Expression S Term','Expression',3,'p_expression','parse_bla.py',21),
  ('Expression -> Term','Expression',1,'p_expression_term','parse_bla.py',26),
  ('Term -> Term M Factor','Term',3,'p_term','parse_bla.py',32),
  ('Term -> Term D Factor','Term',3,'p_term','parse_bla.py',33),
  ('Term -> Factor','Term',1,'p_term_factor','parse_bla.py',38),
  ('Factor -> LEFT_BRACKET Expression RIGHT_BRACKET','Factor',3,'p_factor','parse_bla.py',44),
  ('Factor -> BINARY_LITERAL','Factor',1,'p_factor_binary','parse_bla.py',50),
  ('Factor -> ID','Factor',1,'p_factor_id','parse_bla.py',55),
]
