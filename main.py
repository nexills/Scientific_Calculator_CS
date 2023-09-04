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
    para_stack = [] # stores unclosed brackets
    para_list = [] # stores index of '(' once it is closed

    # set up the gui elements and number buttons
    screen = tk.Label(gui, text='0', font=std_font, anchor="e", width=24)
    history = tk.Label(gui, text='', font=std_font, anchor="w", width=24, bg='lightgrey')
    b0 = tk.Button(gui, text='0', font=std_font, command=lambda: enter.enter(screen, '0')
                   , bg='black', fg='white', width=4)
    b1 = tk.Button(gui, text='1', font=std_font, command=lambda: enter.enter(screen, '1')
                   , bg='black', fg='white', width=4)
    b2 = tk.Button(gui, text='2', font=std_font, command=lambda: enter.enter(screen, '2')
                   , bg='black', fg='white', width=4)
    b3 = tk.Button(gui, text='3', font=std_font, command=lambda: enter.enter(screen, '3')
                   , bg='black', fg='white', width=4)
    b4 = tk.Button(gui, text='4', font=std_font, command=lambda: enter.enter(screen, '4')
                   , bg='black', fg='white', width=4)
    b5 = tk.Button(gui, text='5', font=std_font, command=lambda: enter.enter(screen, '5')
                   , bg='black', fg='white', width=4)
    b6 = tk.Button(gui, text='6', font=std_font, command=lambda: enter.enter(screen, '6')
                   , bg='black', fg='white', width=4)
    b7 = tk.Button(gui, text='7', font=std_font, command=lambda: enter.enter(screen, '7')
                   , bg='black', fg='white', width=4)
    b8 = tk.Button(gui, text='8', font=std_font, command=lambda: enter.enter(screen, '8')
                   , bg='black', fg='white', width=4)
    b9 = tk.Button(gui, text='9', font=std_font, command=lambda: enter.enter(screen, '9')
                   , bg='black', fg='white', width=4)
    bpt = tk.Button(gui, text='.', font=std_font, command=lambda: enter.enter(screen, '.')
                   , bg='black', fg='white', width=4)
    screen.grid(row=2, column=3,columnspan=5)
    history.grid(row=1, column=3,columnspan=5)
    b0.grid(row=8,column=4, sticky="nswe")
    b1.grid(row=5,column=3, sticky="nswe")
    b2.grid(row=5,column=4, sticky="nswe")
    b3.grid(row=5,column=5, sticky="nswe")
    b4.grid(row=6,column=3, sticky="nswe")
    b5.grid(row=6,column=4, sticky="nswe")
    b6.grid(row=6,column=5, sticky="nswe")
    b7.grid(row=7,column=3, sticky="nswe")
    b8.grid(row=7,column=4, sticky="nswe")
    b9.grid(row=7,column=5, sticky="nswe")
    bpt.grid(row=8,column=5, sticky="nswe")
    # set up the basic buttons
    add = tk.Button(gui, text='+', font=std_font, command=lambda: enter.enter(screen, '+')
                   , bg='black', fg='white')
    min = tk.Button(gui, text='-', font=std_font, command=lambda: enter.enter(screen, '-')
                   , bg='black', fg='white')
    mul = tk.Button(gui, text='×', font=std_font, command=lambda: enter.enter(screen, '×')
                   , bg='black', fg='white')
    div = tk.Button(gui, text='÷', font=std_font, command=lambda: enter.enter(screen, '÷')
                   , bg='black', fg='white')
    exe = tk.Button(gui, text='=', font=std_font, command=lambda: operate.exe(screen, 
                    history, para_list, para_stack), bg='darkorange', fg='white')
    clear = tk.Button(gui, text='Clr', font=std_font, command=lambda: enter.clear(screen, history
                    , para_list, para_stack), bg='black', fg='red', width=4)
    delete = tk.Button(gui, text='Del', font=std_font, command=lambda: enter.delete(screen
                    , para_list, para_stack), bg='black', fg='grey', width=4)
    add.grid(row=7,column=6, sticky="nswe")
    min.grid(row=7,column=7, sticky="nswe")
    mul.grid(row=6,column=6, sticky="nswe")
    div.grid(row=6,column=7, sticky="nswe")
    exe.grid(row=8,column=7, sticky="nswe")
    clear.grid(row=5,column=7, sticky="nswe")
    delete.grid(row=5,column=6, sticky="nswe")

    # setup extra buttons
    # brackets
    leftb = tk.Button(gui, text='(', font=std_font, command=lambda: enter.enter_para(screen, 
                    '(', para_stack, para_list), bg='black', fg='white', width=4)
    leftb.grid(row=3,column=3, sticky="nswe")
    rightb = tk.Button(gui, text=')', font=std_font, command=lambda: enter.enter_para(screen, 
                    ')', para_stack, para_list) , bg='black', fg='white', width=4)
    rightb.grid(row=3,column=4, sticky="nswe")

    # scientific buttons
    pow = tk.Button(gui, text='^', font=std_font, command=lambda: enter.enter(screen, '^')
                   , bg='black', fg='white', width=4)
    pow.grid(row=8,column=6, sticky="nswe")
    mod = tk.Button(gui, text='%', font=std_font, command=lambda: enter.enter(screen, '%')
                   , bg='black', fg='white', width=4)
    mod.grid(row=8,column=3, sticky="nswe")
    log = tk.Button(gui, text='log₂', font=std_font, command=lambda: enter.enter_single(screen,
          'L', para_stack, para_list), bg='black', fg='white', width=4)
    log.grid(row=4,column=3, sticky="nswe")
    sqrt = tk.Button(gui, text='√', font=std_font, command=lambda: enter.enter_single(screen,
          '√', para_stack, para_list), bg='black', fg='white', width=4)
    sqrt.grid(row=9,column=3, sticky="nswe")
     
    # probability: permutation and combination
    perm = tk.Button(gui, text='nPr', font=std_font, command=lambda: enter.enter(screen, 'P')
                   , bg='black', fg='white', width=4)
    perm.grid(row=4,column=4, sticky="nswe")
    comb = tk.Button(gui, text='nCr', font=std_font, command=lambda: enter.enter(screen, 'C')
                   , bg='black', fg='white', width=4)
    comb.grid(row=4,column=5, sticky="nswe")

    # shift left and shift right
    sll = tk.Button(gui, text='<<', font=std_font, command=lambda: enter.enter(screen, '<')
                   , bg='black', fg='white', width=4)
    srl = tk.Button(gui, text='>>', font=std_font, command=lambda: enter.enter(screen, '>')
                   , bg='black', fg='white')
    sll.grid(row=4,column=6, sticky="nswe")
    srl.grid(row=4,column=7, sticky="nswe")

    # bitwise and, or, not
    band = tk.Button(gui, text='&', font=std_font, command=lambda: enter.enter(screen, '&')
                   , bg='black', fg='white')
    bor = tk.Button(gui, text='|', font=std_font, command=lambda: enter.enter(screen, '|')
                   , bg='black', fg='white')
    bnot = tk.Button(gui, text='!', font=std_font, command=lambda: enter.enter_single(screen, '!',
                      para_stack, para_list), bg='black', fg='white')
    band.grid(row=3,column=5, sticky="nswe")
    bor.grid(row=3,column=6, sticky="nswe")
    bnot.grid(row=3,column=7, sticky="nswe")


    gui.mainloop()

    
