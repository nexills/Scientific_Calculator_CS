
import tkinter as tk

# this file contains all the functions called when a numerical button
# is pressed, as well as other basic buttons

def enter(screen, text):
    # enter text to the screen
    if screen['text'] == '0':
        # remove the initial '0' on screen
        # but do so only if text is not an operator
        # also do so when text is '-' because negative numbers
        try:
            temp = int(text)
            if temp == 0:
                return
        except:
            # text is non-int
            if text == '-' or text == '!':
                # negative numbers or bitwise not
                screen['text'] = text
            else:
                screen['text'] = screen['text'] + text
        else:
            screen['text'] = text
    else:
        if text not in ['0','1','2','3','4','5','6','7','8','9']:
            if screen['text'][-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                # entering two operators in a row is not allowed, in general
                # exception 1: when entering 2 '-', treat it as positive
                if text == '-' and screen['text'][-1] == '-':
                    screen['text'] = screen['text'][:-1]
                # exception 2: when entering '-' following another operator
                elif text == '-' and screen['text'] != '.':
                    screen['text'] = screen['text'] + text
                # exception 3: bitwise not must follow an operator
                elif text == '!':
                    screen['text'] = screen['text'] + text
                return
        # special exception: bitwise not must follow an operator
        if text == '!':
            return
        screen['text'] = screen['text'] + text

def clear(screen, history):
    screen['text'] = '0'
    history['text'] = ''

def delete(screen):
    if len(screen['text']) > 1:
        screen['text'] = screen['text'][:-1]
    else:
        screen['text'] = '0'

# const priority for operators
# operators in 1st sublist is executed first, then 2nd, etc.
OPERATOR_PRIORITY = [['&','|','!'], ['<','>'], ['^', '%'], ['×', '÷'], ['+', '-']]
NUMBERS = ['0','1','2','3','4','5','6','7','8','9','.']

def single_operate(op2, operator):
    # execute operation with only 1 operands
    temp = 0
    match operator:
        case '!':
            temp = ~int(op2)
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
                return "ERROR"
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
        # scientific operations
        case '^':
            temp = op1 ** op2
        case '%':
            temp = op1 % op2
    if int(temp) == temp:
        return int(temp)
    else:
        return temp

def exe(screen, history):
    # execute the operations
    if screen['text'] == "ERROR":
        return
    history['text'] = screen['text']
    for operators in OPERATOR_PRIORITY:
        index = 0
        while index < len(screen['text']):
            if screen['text'][index] not in operators:
                index += 1
            else:
                # need to operate
                operator = screen['text'][index]
                # if an operator is found, get the two operands
                start = index
                end = index + 1
                # get operands 1
                for i in range(start-1, -1, -1):
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
                if start - index == 0:
                    if operator in ['!']:
                        # handle operator with only 1 operands
                        operand2 = float(screen['text'][index+1:end+1])
                        result = single_operate(operand2, operator)
                    else:
                        # dealing with negative numbers at index 0
                        # as minus sign will call this part
                        index += 1
                        continue
                else:
                    operand1 = float(screen['text'][start:index])
                    operand2 = float(screen['text'][index+1:end+1])
                    result = operate(operand1, operand2, operator)
                if not isinstance(result, int) and not isinstance(result, float):
                    screen['text'] = "ERROR"
                    return
                screen['text'] = screen['text'].replace(screen['text'][start:end+1], str(result))
                # reset index
                index = 0
                # check for cases where negative result follow a '-' operator
                if screen['text'][start] == '-' and start >= 1:
                    if screen['text'][start-1] == '-':
                        screen['text'] = screen['text'].replace(screen['text'][start-1:start+1], '')

