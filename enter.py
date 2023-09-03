
import tkinter as tk
import math
from data import OPERATOR_PRIORITY
from data import NUMBERS
from data import SINGLE_OPERAND

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
            if text in SINGLE_OPERAND:
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
                # exception 2: when entering a 1-operand operator, it must follow
                # another operator except '.'
                elif screen['text'] != '.' and text in SINGLE_OPERAND:
                    screen['text'] = screen['text'] + text
                # exception 3: if text before is ')'
                elif screen['text'][-1] == ')':
                    screen['text'] = screen['text'] + text
                return
        # if a 1-operand operator follow a number, auto add a '×' before it
        if (text != '-' and text in SINGLE_OPERAND):
            screen['text'] = screen['text'] + '×' + text
        else:
            screen['text'] = screen['text'] + text

def enter_para(screen, text, para_stack, para_list):
    if text == '(':
        if screen['text'] == '0':
        # then set to the bracket
            screen['text'] = text
        else:
            if screen['text'][-1] in NUMBERS and screen['text'][-1] != '.':
                screen['text'] = screen['text'] + '×' + text
            else:
                screen['text'] = screen['text'] + text
        # append the index to the stack
        para_stack.append(len(screen['text'])-1)
    else:
        if len(para_stack) <= 0:
            # if no '(', do nothing
            return
        if (screen['text'][-1] in NUMBERS and screen['text'][-1] != '.'
            ) or screen['text'][-1] == ')':
            screen['text'] = screen['text'] + text
            para_list.append(para_stack[-1])
            para_stack.pop()


def clear(screen, history, para_stack, para_list):
    screen['text'] = '0'
    history['text'] = ''
    para_stack.clear()
    para_list.clear()

def delete(screen, para_stack, para_list):
    if len(screen['text']) > 1:
        if screen['text'][-1] == '(':
            # if open brackets are deleted, delete its entry in the stack
            para_stack.pop()
        elif screen['text'][-1] == ')':
            # if close brackets are deleted, delete its entry in the list
            # add the open brackets back to the stack
            para_stack.append(para_list[-1])
            para_list.pop()
            pass
        screen['text'] = screen['text'][:-1]
    else:
        screen['text'] = '0'
        para_stack.clear()
        para_list.clear()



def single_operate(op2, operator):
    # execute operation with only 1 operands
    temp = 0
    match operator:
        case '!':
            temp = ~int(op2)
        case 'L':
            temp = math.log(op2, 2)
        case '√':
            temp = math.sqrt(op2)
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
        # scientific operations
        case '^':
            temp = op1 ** op2
        case '%':
            temp = op1 % op2
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
                        # handle operator with only 1 operands
                        operand2 = float(screen['text'][index+1:end+1])
                        result = single_operate(operand2, operator)
                    else:
                        # dealing with negative numbers at index 0
                        # as minus sign will call this part
                        index += 1
                        continue
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
                    screen['text'] = "ERROR"
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


def exe(screen, history, para_list, para_stack):
    # execute the operations
    # check if all brackets are closed
    if len(para_stack) > 0:
        screen['text'] == "ERROR"
        para_stack.clear()
        return
    if screen['text'] == "ERROR":
        return
    history['text'] = screen['text']
    para_list.sort(reverse=True)
    for each in para_list:
        exe_each(screen, each)
    exe_each(screen, 0)
    para_list.clear()
