# Parentheses Validator
# This program checks whether a mathematical expression
# has balanced opening and closing parentheses.

expression = input('Enter a numerical expression: ')
stack = []
for symbol in expression:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break
if len(stack) == 0:
    print('Valid expression')
else:
    print('Invalid expression')
