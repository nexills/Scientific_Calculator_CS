# const priority for operators
# operators in 1st sublist is executed first, then 2nd, etc.
OPERATOR_PRIORITY = [['I', 'Q', 'B', 'E'],
                     ['!', 'L', '√', 's', 'c', 't', 'X'], # prioritize one-operand operators
                     ['&', '|', 'D'], ['<', '>'], ['P', 'C', 'S'],
                     ['^', '%'], ['×', '÷'], ['+', '-']]
# a list of operators that are unary (before a number)
SINGLE_OPERAND = ['!', 'L', '-', '√', 's', 'c', 't', 'X']
# often used for syntax checking
NUMBERS = ['0','1','2','3','4','5','6','7','8','9','.']
INTS = ['0','1','2','3','4','5','6','7','8','9']
# a list of operators that modify a number (added after a number)
MODS = ['I', 'Q', 'B', 'E']
# a list of operators that have different symbols on display screen vs expression
# in the expression, all operator are stored with as 1 letter only
# on screen, some may not be, eg. log
SYMBOL_DICT = {'L': 'log₂', '<': '<<', '>': '>>',
               's': 'sin', 'c': 'cos', 't': 'tan',
               'S': 'ˣ√', 'X': '2ˣ', 'I': '⁻¹',
               'Q': '²', 'B': '³', '!': '!ᵇᶦⁿ', # '!' must go before 'E'
               'E': '!ᶠᵃᶜ','^': '^ᵉˣᵖ', 'D': '^ˣᵒʳ'}