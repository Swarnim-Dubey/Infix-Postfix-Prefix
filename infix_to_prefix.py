def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0

def infix_to_prefix(expression):

    expression = expression[::-1]

    expression = list(expression)
    for i in range(len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('
    expression = "".join(expression)

    stack = []
    result = []

    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) > precedence(char):
                result.append(stack.pop())
            if char == '^' and stack and precedence(stack[-1]) == precedence(char):
                pass
            else:
                while stack and precedence(stack[-1]) >= precedence(char):
                    result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
        return "".join(result[::-1])
    
# input for the expression

expression = input("Enter the infix expression : ")

print(f"Infix Expression : {expression}")
print(f"Prefix Expression : {infix_to_prefix(expression)}")
