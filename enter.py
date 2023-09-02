
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
            if text == '-':
                # negative numbers
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
OPERATOR_PRIORITY = [['×', '÷'], ['+', '-']]

def operate(op1, op2, operator):
    # execute a individual operation, given the operands
    temp = 0
    match operator:
        case '+':
            temp = op1 + op2
        case '-':
            temp = op1 - op2
        case '×':
            temp = op1 * op2
        case '÷':
            temp = op1 / op2
    if int(temp) == temp:
        return int(temp)
    else:
        return temp

def exe(screen, history):
    # execute the operations
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
                for i in range(start-1, -1, -1):
                    if screen['text'][i] in ['0','1','2','3','4','5','6','7','8','9','.']:
                        start = i
                    elif screen['text'][i] == '-':
                        # special case when 1st operand is negative
                        # '-' is part of the number so long as no number is before it
                        # or '-' is at index 0
                        if i == 0 or screen['text'][i-1] not in ['0','1','2','3','4','5',
                                                               '6','7','8','9','.']:
                            start = i
                        else:
                            break
                    else:
                        break
                for i in range(end, len(screen['text'])):
                    if screen['text'][i] in ['0','1','2','3','4','5','6','7','8','9','.']:
                        end = i
                    elif end == i and screen['text'][i] == '-':
                        # special case when 2nd operand is negative
                        end = i
                    else:
                        break
                # dealing with negative numbers at index 0
                # as minus sign will call this part
                if start - index == 0:
                    index += 1
                    continue
                operand1 = float(screen['text'][start:index])
                operand2 = float(screen['text'][index+1:end+1])
                result = operate(operand1, operand2, operator)
                screen['text'] = screen['text'].replace(screen['text'][start:end+1], str(result))
                # reset index
                index = 0
                # check for cases where negative result follow a '-' operator
                if screen['text'][start] == '-' and start >= 1:
                    if screen['text'][start-1] == '-':
                        screen['text'] = screen['text'].replace(screen['text'][start-1:start+1], '')

