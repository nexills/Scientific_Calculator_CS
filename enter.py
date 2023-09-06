
from data import NUMBERS
from data import SINGLE_OPERAND
from data import SYMBOL_DICT
from data import INTS
from data import MODS

# this file contains all the functions called when a button is pressed,
# with the exception of '='

def sync(screen, expr):
    # this function sync the screen to the new expression
    screen['text'] = expr['text']
    for each_exp in SYMBOL_DICT:
        screen['text'] = screen['text'].replace(each_exp, SYMBOL_DICT[each_exp])

def enter(screen, expr, text):
    # enter text to the screen
    # text must be neither a unary op nor bracket
    if expr['text'] == '0':
        # replace the initial '0' on screen with text
        # but do so only if text is not an operator
        # also do so when text is '-' because negative numbers
        if text in NUMBERS:
            expr['text'] = text
        else:
            # text is non-int
            if text == '-':
                # negative numbers
                expr['text'] = text
            else:
                return
    else:
        if text in NUMBERS:
            # a number or a decimal point
            if text == '.':
                if expr['text'][-1] in INTS:
                    # a decimal point can only be added to numbers
                    expr['text'] = expr['text'] + text
            elif expr['text'][-1] in MODS:
                # add a 'x' before
                expr['text'] = expr['text'] + '×' + text
            elif expr['text'][-1] == ')':
                # add a 'x' before
                expr['text'] = expr['text'] + '×' + text
            else:
                expr['text'] = expr['text'] + text
        else:
            # an operator
            if expr['text'][-1] not in INTS:
                # entering two operators in a row is not allowed, in general
                # exception 1: when entering 2 '-', treat it as positive
                if text == '-' and expr['text'][-1] == '-':
                    expr['text'] = expr['text'][:-1]
                # exception 2: when following a close bracket
                elif expr['text'][-1] == ')':
                    expr['text'] = expr['text'] + text
                # exception 3: '-' follows '('
                elif expr['text'][-1] == '(' and text == '-':
                    expr['text'] = expr['text'] + text
                # exception 4: following a MODS
                elif expr['text'][-1] in MODS:
                    expr['text'] = expr['text'] + text
                else: 
                    return
            else:
                expr['text'] = expr['text'] + text
    sync(screen, expr)

def enter_single(screen, expr, text, para_stack, para_list):
    # enter text to the screen
    # text must be an unary op
    if expr['text'] == '0':
        # remove the initial '0' on screen
        expr['text'] = text
        # add a open bracket after
        enter_para(screen, expr, '(', para_stack, para_list)
    else:
        if expr['text'][-1] not in INTS:
            # entering two operators in a row is allowed
            # the only exception is '.' before
            if expr['text'][-1] == '.':
                return
            # when following a close bracket
            elif expr['text'][-1] == ')':
                # add 'x' before a 1-operand op
                expr['text'] = expr['text'] + '×' + text
                enter_para(screen, expr, '(', para_stack, para_list)
            elif expr['text'][-1] in MODS:
                expr['text'] = expr['text'] + '×' + text
                enter_para(screen, expr, '(', para_stack, para_list)
            # otherwise simply add
            else:
                expr['text'] = expr['text'] + text
                enter_para(screen, expr, '(', para_stack, para_list)
        # if an unary operator follow a number, auto add a '×' before it
        elif (text != '-' and text in SINGLE_OPERAND):
            expr['text'] = expr['text'] + '×' + text
            enter_para(screen, expr, '(', para_stack, para_list)
    sync(screen, expr)

def enter_sup(screen, expr, text):
    # enter a superscript, such as powers
    if expr['text'] == '0':
        return
    else:
        if expr['text'][-1] in INTS or expr['text'][-1] == ')':
            expr['text'] = expr['text'] + text
        else:
            return
    sync(screen, expr)

def enter_para(screen, expr, text, para_stack, para_list):
    # enter either '(' or ')' to the screen
    if expr['text'] != '0' and expr['text'][-1] == '.':
        # bracket must not follow a '.'
        return
    if text == '(':
        if expr['text'] == '0':
            # then set to the bracket
            expr['text'] = text
        else:
            if expr['text'][-1] in INTS:
                # add 'x' before if it follows a int
                expr['text'] = expr['text'] + '×' + text
            else:
                expr['text'] = expr['text'] + text
        # append the index to the stack
        para_stack.append(len(expr['text'])-1)
    else:
        if len(para_stack) <= 0:
            # if no '(', do nothing
            return
        if expr['text'][-1] in INTS or expr['text'][-1] == ')' or \
        expr['text'][-1] in MODS:
            # can only add if it follows a int or ')' or a MODS
            expr['text'] = expr['text'] + text
            # update the stack and list
            para_list.append(para_stack[-1])
            para_stack.pop()
    sync(screen, expr)

def enter_ans(screen, expr, answer):
    # enter the result of the previous expression to the screen
    if len(expr['text']) != 0:
        if expr['text'][-1] == '.':
            return
        elif expr['text'][-1] in NUMBERS and expr['text'][-1] != '0':
            # insert a '×' if previous char is a number
            expr['text'] = expr['text'] + '×'
    # insert the previous result
    for each_number in answer[0]:
        enter(screen, expr, each_number)

def clear(screen, expr, history, para_list, para_stack):
    # this function resets the calculator, but does not clear out answer
    screen['text'] = '0'
    history['text'] = ''
    expr['text'] = '0'
    para_stack.clear()
    para_list.clear()
    sync(screen, expr)

def delete(screen, expr, para_list, para_stack, answer):
    # delete the latest char from the expression
    if len(expr['text']) > 1:
        if expr['text'][-1] == '(':
            # if open brackets are deleted, delete its entry in the stack
            para_stack.pop()
        elif expr['text'][-1] == ')':
            # if close brackets are deleted, delete its entry in the list
            # add the open brackets back to the stack
            para_stack.append(para_list[-1])
            para_list.pop()
            pass
        expr['text'] = expr['text'][:-1]
    else:
        # if there is only 1 char, replace with '0'
        expr['text'] = '0'
        para_stack.clear()
        para_list.clear()
    sync(screen, expr)




