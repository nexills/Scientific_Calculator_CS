# CS_Scientific_Calculator

This is a GUI scientific calculator programmed in Python, complete with special functions a computing scientist or software engineer would find useful. This program allows for expression of unlimited size (limited only by the memory size of the operating PC).

# Progress
The current calculator is fully functional. Currently supports 28 functions:
- basic arithmetic (+-×÷)
- brackets/parentheses
- saving and using the previous result
- left/right shift
- bitwise and, or, not, xor
- exponetial, square root, xth root
- log₂, 2ˣ
- inverse, square, cube
- permutation/combination/factorial
- mod
- sin, cos, tan

# Operator Priority
The expressions are executed in the following order:
1. parentheses
2. inverse, square, cube, factorial
3. bitwise not, log₂, sqrt, sin, cos, tan, 2ˣ
3. bitwise and, bitwise or, bitwise xor
4. left and right shift
5. combination, permutation and xth root
6. exponetial and mod
7. multiplication and division
8. addition and subtraction

# Background

# Build Instructions (Windows)
1. Install Python and Pip
2. In Command Prompt, enter py -m pip install pyinstaller
3. Change directory to the location where the repo is downloaded
4. Run py -m PyInstaller main.py
5. Go to ./dist/main/
6. Run main.exe