# a calculator

import tkinter as tk
import enter
import operate

if __name__ == '__main__':
    gui = tk.Tk()
    # set up the window
    gui.title("Calculator")
    # define the font used
    std_font = ('calibre',18,'normal') # standard

    # brackets are traced with a stack and a list
    # open brackets are first stored in the stack
    # when a close bracket is found, move the top of the stack to the list
    # when executing, sort the stack in reverse (highest index comes first)
    # then execute expression inside each bracket, one-by-one
    # finally execute the entire expression once all brackets are sorted out
    # notes: the stack must be empty when executing, ie. balanced brackets
    para_stack = [] # stores unclosed brackets
    para_list = [] # stores index of '(' once it is closed

    # expression stores the actual expression when used to operate
    # uses label so its value can be changed in functions called
    expression = tk.Label(gui, text='0')

    # answer store the result of the previous calculation
    # stored with a list so its value can be changed in functions
    answer = ['0']

    # set up the gui elements and number buttons
    # screen is the display to the user
    # history stores the last executed expression
    screen = tk.Label(gui, text='0', font=std_font, anchor="e", width=24)
    history = tk.Label(gui, text='', font=std_font, anchor="w", width=24, bg='lightgrey')
    b0 = tk.Button(gui, text='0', font=std_font, command=lambda: enter.enter(screen, expression, '0')
                   , bg='black', fg='white', width=4)
    b1 = tk.Button(gui, text='1', font=std_font, command=lambda: enter.enter(screen, expression, '1')
                   , bg='black', fg='white', width=4)
    b2 = tk.Button(gui, text='2', font=std_font, command=lambda: enter.enter(screen, expression, '2')
                   , bg='black', fg='white', width=4)
    b3 = tk.Button(gui, text='3', font=std_font, command=lambda: enter.enter(screen, expression, '3')
                   , bg='black', fg='white', width=4)
    b4 = tk.Button(gui, text='4', font=std_font, command=lambda: enter.enter(screen, expression, '4')
                   , bg='black', fg='white', width=4)
    b5 = tk.Button(gui, text='5', font=std_font, command=lambda: enter.enter(screen, expression, '5')
                   , bg='black', fg='white', width=4)
    b6 = tk.Button(gui, text='6', font=std_font, command=lambda: enter.enter(screen, expression, '6')
                   , bg='black', fg='white', width=4)
    b7 = tk.Button(gui, text='7', font=std_font, command=lambda: enter.enter(screen, expression, '7')
                   , bg='black', fg='white', width=4)
    b8 = tk.Button(gui, text='8', font=std_font, command=lambda: enter.enter(screen, expression, '8')
                   , bg='black', fg='white', width=4)
    b9 = tk.Button(gui, text='9', font=std_font, command=lambda: enter.enter(screen, expression, '9')
                   , bg='black', fg='white', width=4)
    bpt = tk.Button(gui, text='.', font=std_font, command=lambda: enter.enter(screen, expression, '.')
                   , bg='black', fg='white', width=4)
    screen.grid(row=2, column=3,columnspan=5)
    history.grid(row=1, column=3,columnspan=5)
    b0.grid(row=9,column=4, sticky="nswe")
    b1.grid(row=6,column=3, sticky="nswe")
    b2.grid(row=6,column=4, sticky="nswe")
    b3.grid(row=6,column=5, sticky="nswe")
    b4.grid(row=7,column=3, sticky="nswe")
    b5.grid(row=7,column=4, sticky="nswe")
    b6.grid(row=7,column=5, sticky="nswe")
    b7.grid(row=8,column=3, sticky="nswe")
    b8.grid(row=8,column=4, sticky="nswe")
    b9.grid(row=8,column=5, sticky="nswe")
    bpt.grid(row=9,column=5, sticky="nswe")
    # set up the basic buttons
    add = tk.Button(gui, text='+', font=std_font, command=lambda: enter.enter(screen, expression, '+')
                   , bg='black', fg='white')
    min = tk.Button(gui, text='-', font=std_font, command=lambda: enter.enter(screen, expression, '-')
                   , bg='black', fg='white')
    mul = tk.Button(gui, text='×', font=std_font, command=lambda: enter.enter(screen, expression, '×')
                   , bg='black', fg='white')
    div = tk.Button(gui, text='÷', font=std_font, command=lambda: enter.enter(screen, expression, '÷')
                   , bg='black', fg='white')
    
    exe = tk.Button(gui, text='=', font=std_font, command=lambda: operate.exe(screen, expression, 
                    history, para_list, para_stack, answer), bg='darkorange', fg='white')
    clear = tk.Button(gui, text='Clr', font=std_font, command=lambda: enter.clear(screen, expression, history
                    , para_list, para_stack), bg='black', fg='red', width=4)
    delete = tk.Button(gui, text='Del', font=std_font, command=lambda: enter.delete(screen, expression
                    , para_list, para_stack, answer), bg='black', fg='grey', width=4)
    add.grid(row=8,column=6, sticky="nswe")
    min.grid(row=8,column=7, sticky="nswe")
    mul.grid(row=7,column=6, sticky="nswe")
    div.grid(row=7,column=7, sticky="nswe")
    exe.grid(row=9,column=7, sticky="nswe")
    clear.grid(row=6,column=7, sticky="nswe")
    delete.grid(row=6,column=6, sticky="nswe")

    # setup extra buttons
    # brackets
    leftb = tk.Button(gui, text='(', font=std_font, command=lambda: enter.enter_para(screen, expression, 
                    '(', para_stack, para_list), bg='black', fg='white', width=4)
    leftb.grid(row=3,column=3, sticky="nswe")
    rightb = tk.Button(gui, text=')', font=std_font, command=lambda: enter.enter_para(screen, expression, 
                    ')', para_stack, para_list) , bg='black', fg='white', width=4)
    rightb.grid(row=3,column=4, sticky="nswe")

    # scientific buttons
    pow = tk.Button(gui, text='^', font=std_font, command=lambda: enter.enter(screen, expression, '^')
                   , bg='black', fg='white', width=4)
    pow.grid(row=5,column=7, sticky="nswe")
    mod = tk.Button(gui, text='%', font=std_font, command=lambda: enter.enter(screen, expression, '%')
                   , bg='black', fg='white', width=4)
    mod.grid(row=9,column=3, sticky="nswe")
    log = tk.Button(gui, text='log₂', font=std_font, command=lambda: enter.enter_single(screen, expression,
          'L', para_stack, para_list), bg='black', fg='white', width=4)
    log.grid(row=4,column=3, sticky="nswe")
    sqrt = tk.Button(gui, text='√', font=std_font, command=lambda: enter.enter_single(screen, expression,
          '√', para_stack, para_list), bg='black', fg='white', width=4)
    sqrt.grid(row=5,column=3, sticky="nswe")
    sin = tk.Button(gui, text='sin', font=std_font, command=lambda: enter.enter_single(screen, expression,
          's', para_stack, para_list), bg='black', fg='white', width=4)
    sin.grid(row=5,column=4, sticky="nswe")
    cos = tk.Button(gui, text='cos', font=std_font, command=lambda: enter.enter_single(screen, expression,
          'c', para_stack, para_list), bg='black', fg='white', width=4)
    cos.grid(row=5,column=5, sticky="nswe")
    tan = tk.Button(gui, text='tan', font=std_font, command=lambda: enter.enter_single(screen, expression,
          't', para_stack, para_list), bg='black', fg='white', width=4)
    tan.grid(row=5,column=6, sticky="nswe")

    # Ans button: the value of Ans is set to the result of the previous operation
    ans = tk.Button(gui, text='Ans', font=std_font, command=lambda: enter.enter_ans(screen, expression,
          answer), bg='black', fg='white', width=4)
    ans.grid(row=9,column=6, sticky="nswe")
     
    # probability: permutation and combination
    perm = tk.Button(gui, text='nPr', font=std_font, command=lambda: enter.enter(screen, expression, 'P')
                   , bg='black', fg='white', width=4)
    perm.grid(row=4,column=4, sticky="nswe")
    comb = tk.Button(gui, text='nCr', font=std_font, command=lambda: enter.enter(screen, expression, 'C')
                   , bg='black', fg='white', width=4)
    comb.grid(row=4,column=5, sticky="nswe")

    # shift left and shift right
    sll = tk.Button(gui, text='<<', font=std_font, command=lambda: enter.enter(screen, expression, '<')
                   , bg='black', fg='white', width=4)
    srl = tk.Button(gui, text='>>', font=std_font, command=lambda: enter.enter(screen, expression, '>')
                   , bg='black', fg='white')
    sll.grid(row=4,column=6, sticky="nswe")
    srl.grid(row=4,column=7, sticky="nswe")

    # bitwise and, or, not
    band = tk.Button(gui, text='&', font=std_font, command=lambda: enter.enter(screen, expression, '&')
                   , bg='black', fg='white')
    bor = tk.Button(gui, text='|', font=std_font, command=lambda: enter.enter(screen, expression, '|')
                   , bg='black', fg='white')
    bnot = tk.Button(gui, text='!', font=std_font, command=lambda: enter.enter_single(screen, expression, '!',
                      para_stack, para_list), bg='black', fg='white')
    band.grid(row=3,column=5, sticky="nswe")
    bor.grid(row=3,column=6, sticky="nswe")
    bnot.grid(row=3,column=7, sticky="nswe")


    gui.mainloop()

    
