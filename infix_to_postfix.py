def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    # stack for operators
    stack = []

    # list for output
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)


expression = input("Enter Infix Expression : ")
postfix = infix_to_postfix(expression)

print("\nThe expression that is stored in the list is :-")
print(list(expression))

print("\nCOnverted Postfix Expression : ", postfix)




