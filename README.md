# Software_Engineers'_Calculator

So, there are plenty of calculators - scientific, graphing, financial, and so on. What would happen if there is a calculator designed for software engineer?

This is a full-on, GUI scientific calculator, complete with all the functions a software engineer would find useful. It supports entering multiple commands at once.

# Progress
The current calculator is fully functional. Currently supported operations:
- basic arithmetic (int and float)
- multiple brackets/parentheses
- left/right shift
- bitwise and, or, not
- exponetial, square root
- log base 2
- permutation/combination (x factorial can be entered as xPx)
- mod

# Operator Priority
The expressed is executed in the following order:
1. parentheses
2. bitwise not, log base 2 and square root
3. bitwise and, bitwise or
4. left and right shift
5. combination and permutation
6. exponetial and mod
7. multiplication and division
8. addition and subtraction

# Planned Features
- inverse
- sin, cos, tan