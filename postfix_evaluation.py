# postfix expression evaluation using stacks 

def post_evaluation(expression):
    stack = []

# Split expression into operands/operators
    tokens = expression.split()
    
    for ch in tokens:
        if ch.isdigit():  # Operand
            stack.append(int(ch))
        else:  # Operator
            b = stack.pop()
            a = stack.pop()
            
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
    
    return stack.pop()


# taking the input of the expression

expression = input("Enter postfix expression : ")
print("Evaluated answer to the expression : ", post_evaluation(expression))