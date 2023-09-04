
from data import NUMBERS
from data import SINGLE_OPERAND

# this file contains all the functions called when a numerical button
# is pressed, as well as other basic buttons

def enter(screen, text):
    # enter text to the screen
    # text must be neither a 1-operand op nor bracket
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
                return
        else:
            screen['text'] = text
    else:
        if text in NUMBERS:
            # a number or a decimal point
            if text == '.':
                if screen['text'][-1] in ['0','1','2','3','4','5','6','7','8','9']:
                    screen['text'] = screen['text'] + text
            else:
                screen['text'] = screen['text'] + text
        else:
            # an operator
            if screen['text'][-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                # entering two operators in a row is not allowed, in general
                # exception 1: when entering 2 '-', treat it as positive
                if text == '-' and screen['text'][-1] == '-':
                    screen['text'] = screen['text'][:-1]
                # exception 2: when following a close bracket
                elif screen['text'][-1] == ')':
                    screen['text'] = screen['text'] + text
                return
            else:
                screen['text'] = screen['text'] + text

def enter_single(screen, text, para_stack, para_list):
    # enter text to the screen
    # text must be a single operator
    if screen['text'] == '0':
        # remove the initial '0' on screen
        screen['text'] = text
        # add a open bracket after
        enter_para(screen, '(', para_stack, para_list)
    else:
        if screen['text'][-1] not in ['0','1','2','3','4','5','6','7','8','9']:
            # entering two operators in a row is allowed
            # when following a close bracket
            if screen['text'][-1] == ')':
                # add 'x' before a 1-operand op
                screen['text'] = screen['text'] + '×' + text
                enter_para(screen, '(', para_stack, para_list)
            # otherwise simply add
            else:
                screen['text'] = screen['text'] + text
                enter_para(screen, '(', para_stack, para_list)
        # if a 1-operand operator follow a number, auto add a '×' before it
        elif (text != '-' and text in SINGLE_OPERAND):
            screen['text'] = screen['text'] + '×' + text
            enter_para(screen, '(', para_stack, para_list)


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


def clear(screen, history, para_list, para_stack):
    screen['text'] = '0'
    history['text'] = ''
    para_stack.clear()
    para_list.clear()

def delete(screen, para_list, para_stack):
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




