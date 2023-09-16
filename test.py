# a test file

import tkinter as tk
import enter
import operate
import math

if __name__ == '__main__':

    # initial setups
    std_font = ('calibre',18,'normal')
    para_stack = [] # stores unclosed brackets
    para_list = [] # stores index of '(' once it is closed
    gui = tk.Tk()
    expression = tk.Label(gui, text='0')
    screen = tk.Label(gui, text='0', font=std_font, anchor="e", width=28)
    history = tk.Label(gui, text='', font=std_font, anchor="w", width=28, bg='lightgrey')
    answer = ['0']

    # basic tests
    for i in "14987+12×618.35-781÷2.10":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 22035.29524) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "781+61<3-7&2>1+3044":
        enter.enter(screen, expression, i)
    for i in range(5):
        enter.delete(screen, expression, para_list, para_stack)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 1268) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "3S81-31|9D4+8P2+3C3":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 34.32675) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # tests for bracket "181×(21.2-6.5×(7+2)<<4)"
    for i in "181×":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "21.2-6.5×":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "7+2":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    for i in "<4":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - -165578.8) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # test for unary operators
    for i in "3.15+96":
        enter.enter(screen, expression, i)
    enter.enter_single(screen, expression,'√', para_stack, para_list)
    for i in "121":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    for i in "-7>1s3.14":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 1052.15) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # test for power
    enter.enter(screen, expression, "9")
    enter.enter_sup(screen, expression, 'I')
    for i in "121":
        enter.enter(screen, expression, i)
    enter.enter_sup(screen, expression, 'Q')
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 1626.77778) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
