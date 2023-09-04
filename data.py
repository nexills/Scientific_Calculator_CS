# const priority for operators
# operators in 1st sublist is executed first, then 2nd, etc.
OPERATOR_PRIORITY = [['!', 'L', '√', 's', 'c', 't'], # prioritize one-operand operators
                     ['&','|'], ['<','>'], ['P','C'],
                     ['^', '%'], ['×', '÷'], ['+', '-']]
# a list of operators that operate on 1 operand only
SINGLE_OPERAND = ['!', 'L', '-', '√', 's', 'c', 't']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9','.']
INTS = ['0','1','2','3','4','5','6','7','8','9']
# a list of operators that have different symbols on display screen vs expression
# in the expression, all operator are stored with as 1 letter only
# on screen, some may not be, eg. log
SYMBOL_DICT = {'L': 'log₂', '<': '<<', '>': '>>',
               's': 'sin', 'c': 'cos', 't': 'tan'}