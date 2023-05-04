
# Algorithm

# 1: Evaluate for each character in postfix expressiion
# 2: If Operands is encountered, push into stack.
# 3: If operator is encountered, pop 2 characters from stack which were already filled in stack.
#         first =top element from stack.
#         second=second element from stack
# 4: Check for operator & push into stack after operation
#          second operator first
# 5: return top element from stack


def postfix_eval(arr):
    stack = []
    operator = ["+", "-", "*", "/", "%"]

    for item in arr:
        if item not in operator:
            stack.append((item))
        else:
            first = int(stack.pop())
            second = int(stack.pop())

            if item == "+":
                stack.append(second+first)
            if item == "-":
                stack.append(second-first)
            if item == "*":
                stack.append(second*first)
            if item == "/":
                stack.append(second/first)
            if item == "%":
                stack.append(second % first)
    return stack[-1]


A = ["2", "1", "+", "3", "*"]

print("The Value:", postfix_eval(A))
