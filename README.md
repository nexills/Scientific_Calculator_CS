# CS_Scientific_Calculator

This is a GUI scientific calculator programmed in Python, complete with special functions a computing scientist or software engineer would find useful. This program allows for expression of unlimited size (limited only by the memory size of the operating PC).

# Progress
The current calculator is fully functional. Currently supports:
- basic arithmetic (int and float)
- multiple brackets/parentheses
- saving and using the previous result
- left/right shift
- bitwise and, or, not
- exponetial, square root
- log base 2
- permutation/combination (x factorial can be entered as xPx)
- mod
- sin, cos, tan

# Operator Priority
The expressions are executed in the following order:
1. parentheses
2. bitwise not, log₂, sqrt, sin, cos, tan
3. bitwise and, bitwise or
4. left and right shift
5. combination and permutation
6. exponetial and mod
7. multiplication and division
8. addition and subtraction

# Planned Features
- inverse
