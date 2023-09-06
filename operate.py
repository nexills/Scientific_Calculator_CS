
import math
from data import OPERATOR_PRIORITY
from data import NUMBERS
from data import SINGLE_OPERAND
from data import INTS
from enter import sync
from data import MODS

# this file contains the functions called when '=' is pressed

def single_operate(op2, operator):
    # execute unary operation
    temp = 0
    match operator:
        case '!':
            # bitwise not, not factorial !
            temp = ~int(op2)
        case 'L':
            temp = math.log(op2, 2)
        case '√':
            if op2 < 0:
                return "MATH ERROR"
            temp = math.sqrt(op2)
        case 's':
            temp = math.sin(op2)
        case 'c':
            temp = math.cos(op2)
        case 't':
            temp = math.cos(op2)
        case 'X':
            temp = 2 ** op2
    if int(temp) == temp:
        return int(temp)
    else:
        return temp

def operate_mod(op1, operator):
    # execute an operation that operates the number before
    temp = 0
    match operator:
        case 'I':
            temp = 1/op1
        case 'Q':
            temp = op1 * op1
        case 'B':
            temp = op1 ** 3
        case 'E':
            if op1 < 0:
                return "MATH ERROR"
            temp = math.factorial(int(op1))
    if int(temp) == temp:
        return int(temp)
    else:
        return temp

def operate(op1, op2, operator):
    # execute a individual operation, given the operands
    temp = 0
    match operator:
        # simple operations
        case '+':
            temp = op1 + op2
        case '-':
            temp = op1 - op2
        case '×':
            temp = op1 * op2
        case '÷':
            if op2 == 0:
                return "MATH ERROR"
            temp = op1 / op2
        # computing operations
        case '>':
            temp = int(op1) >> int(op2)
        case '<':
            temp = int(op1) << int(op2)
        case '&':
            temp = int(op1) & int(op2)
        case '|':
            temp = int(op1) | int(op2)
        case 'D':
            temp = int(op1) ^ int(op2)
        # scientific operations
        case '^':
            temp = op1 ** op2
        case '%':
            temp = op1 % op2
        case 'S':
            # xth root
            temp = op2 ** (1/op1)
        # probability operations
        # where op1 is n, op2 is r
        case 'P':
            if op2 > op1 or op2 < 0 or op1 < 0:
                return "MATH ERROR"
            temp = math.factorial(int(op1))/math.factorial(int(op1)-int(op2))
        case 'C':
            if op2 > op1 or op2 < 0 or op1 < 0:
                return "MATH ERROR"
            temp = math.comb(int(op1), int(op2))
    if int(temp) == temp:
        return int(temp)
    else:
        return temp

def exe_each(screen, begin):
    # execute each bracket
    for operators in OPERATOR_PRIORITY:
        # check from highest priority to lowest priority
        index = begin
        while index < len(screen['text']):
            if screen['text'][index] == ')':
                # the bracket has closed
                # go to next loop and do the next operators
                break
            if screen['text'][index] not in operators:
                index += 1
            else:
                # an operator is found; need to operate
                operator = screen['text'][index]
                # if an operator is found, get the two operands
                start = index
                end = index + 1
                # get operands 1
                for i in range(start-1, begin-1, -1):
                    if screen['text'][i] in NUMBERS:
                        start = i
                    elif screen['text'][i] == '-':
                        # special case when 1st operand is negative
                        # '-' is part of the number so long as no number is before it
                        # or '-' is at index 0
                        if i == 0 or screen['text'][i-1] not in NUMBERS:
                            start = i
                        else:
                            break
                    else:
                        break
                # get operands 2
                for i in range(end, len(screen['text'])):
                    if screen['text'][i] in NUMBERS:
                        end = i
                    elif end == i and screen['text'][i] == '-':
                        # special case when 2nd operand is negative
                        end = i
                    else:
                        break
                # calculating
                if start - index == 0:
                    if operator in SINGLE_OPERAND and operator != '-':
                        # handle unary operators
                        try:
                            operand2 = float(screen['text'][index+1:end+1])
                            result = single_operate(operand2, operator)
                        except:
                            result = "ERROR"
                    else:
                        # dealing with negative numbers at index 0
                        # as minus sign will call this part
                        index += 1
                        continue
                elif operator in MODS:
                    # dealing with operator that modifies on the number before
                    try:
                        operand1 = float(screen['text'][start:index])
                        result = operate_mod(operand1, operator)
                    except:
                        result = "ERROR"
                else:
                    # getting the two operands and operating
                    try:
                        operand1 = float(screen['text'][start:index])
                        operand2 = float(screen['text'][index+1:end+1])
                        result = operate(operand1, operand2, operator)
                    except:
                        # handles wrong input
                        result = "INPUT ERROR"
                if not isinstance(result, int) and not isinstance(result, float):
                    # handle math error, eg. divide by zero
                    screen['text'] = result
                    return
                # replace the expression with result
                screen['text'] = screen['text'][:start] + str(result
                                ) + screen['text'][end+1:]
                # reset index
                index = begin
                # check for cases where negative result follow a '-' operator
                if screen['text'][begin] == '-' and begin >= 1:
                    if screen['text'][begin-1] == '-':
                        screen['text'] = screen['text'].replace('--', '')
    if screen['text'][begin] == '(':
        # replacing the brackets after all operations are done
        screen['text'] = screen['text'][:begin] + screen['text'][begin+1:
        index] + screen['text'][index+1:]


def exe(screen, expr, history, para_list, para_stack, answer):
    # execute the expression
    # check if all brackets are closed and errors
    if len(para_stack) > 0:
        expr['text'] == "ERROR"
        para_stack.clear()
        return
    if expr['text'] == "ERROR":
        return
    history['text'] = screen['text']
    # sort the para_list and execute inside brackets first
    para_list.sort(reverse=True)
    for each in para_list:
        exe_each(expr, each)
    exe_each(expr, 0)
    para_list.clear()
    # save current answer and sync with the screen
    answer[0] = expr['text']
    sync(screen, expr)