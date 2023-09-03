# const priority for operators
# operators in 1st sublist is executed first, then 2nd, etc.
OPERATOR_PRIORITY = [['!', 'L', '√'], # prioritize one-operand operators
                     ['&','|'], ['<','>'], ['P','C'],
                     ['^', '%'], ['×', '÷'], ['+', '-']]
# a list of operators that operate on 1 operand only
SINGLE_OPERAND = ['!', 'L', '-', '√']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9','.']