# a test file

import tkinter as tk
import enter
import operate
import math

# initial setups
std_font = ('calibre',18,'normal')
para_stack = [] # stores unclosed brackets
para_list = [] # stores index of '(' once it is closed
gui = tk.Tk()
expression = tk.Label(gui, text='0')
screen = tk.Label(gui, text='0', font=std_font, anchor="e", width=28)
history = tk.Label(gui, text='', font=std_font, anchor="w", width=28, bg='lightgrey')
answer = ['0']

def basicTest():
    # a collection of basic test testing the general functionalities
    for i in "1+2+3-6-9":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - -9) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "2×6×7+1÷3":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 84.33333) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

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

def functionTest():
    # test each function available
    # test: left, right shift
    for i in "156>2+8<1":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 55) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "-156>2+8<1":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - -23) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # test: bitwise and, or, xor
    for i in "7&2+101|332":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 367) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "-31&11":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 1) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
    
    for i in "-9|11D18":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - -19) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # xth root, perm, comb, mod
    for i in "4S256":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 4) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "7P5+12C2":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 2586) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
    
    for i in "103%7":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 5) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)


def unaryTest():
    # test for unary operators √ and sin
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

    # test ! (E), log, cos, tan, 2^x
    enter.enter(screen, expression, '5')
    enter.enter_sup(screen, expression, 'E')
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 120) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    enter.enter_single(screen, expression, 'L', para_stack, para_list)
    enter.enter(screen, expression, '1')
    enter.enter(screen, expression, '8')
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 4.16993) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    enter.enter_single(screen, expression, 'c', para_stack, para_list)
    enter.enter(screen, expression, '1')
    enter.enter(screen, expression, '1')
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 0.004426) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
    
    enter.enter_single(screen, expression, 't', para_stack, para_list)
    enter.enter(screen, expression, '7')
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 0.871448) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
    
    enter.enter_single(screen, expression, 'X', para_stack, para_list)
    enter.enter(screen, expression, '5')
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 32) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

def bracketTest():
    # test bracket
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
    
    # tests for bracket "36÷(-5&11|(71×(9+1)))"
    for i in "36÷":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "-5&11|":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "71×":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "9+1":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 0.0500695) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

def superscriptTest():
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

    for i in "36":
        enter.enter(screen, expression, i)
    enter.enter_sup(screen, expression, 'Q')
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 1296) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "36":
        enter.enter(screen, expression, i)
    enter.enter_sup(screen, expression, 'I')
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 0.0277778) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
    
    for i in "36":
        enter.enter(screen, expression, i)
    enter.enter_sup(screen, expression, 'B')
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 46656) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

def otherTest():
    # test delete function
    for i in "36+71":
        enter.enter(screen, expression, i)
    enter.delete(screen, expression, para_list, para_stack)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 43) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # "36÷(-5&12|(71×2))" -> 36÷(-5&12)
    for i in "36÷":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "-5&12|":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    for i in "71×2":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    for i in range(8):
        enter.delete(screen, expression, para_list, para_stack)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 4.5) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # test answer function
    enter.enter_ans(screen, expression, answer)
    for i in "×3.2":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 14.4) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)

    # test illegal entry
    for i in "67×+-":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert("ERROR" in screen['text'])
    enter.clear(screen, expression, history, para_list, para_stack)

    for i in "6×..8":
        enter.enter(screen, expression, i)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert(math.fabs(float(screen['text']) - 48) < 0.001)
    enter.clear(screen, expression, history, para_list, para_stack)
    
    for i in "6×.":
        enter.enter(screen, expression, i)
    enter.enter_para(screen,expression, '(', para_stack, para_list)
    enter.enter_para(screen,expression, ')', para_stack, para_list)
    print(screen['text'], end = ' = ')
    operate.exe(screen, expression, history, para_list, para_stack, answer)
    print(screen["text"], "passed!")
    assert("ERROR" in screen['text'])
    enter.clear(screen, expression, history, para_list, para_stack)


if __name__ == '__main__':

    basicTest()
    functionTest()
    unaryTest()
    bracketTest()
    superscriptTest()
    otherTest()

