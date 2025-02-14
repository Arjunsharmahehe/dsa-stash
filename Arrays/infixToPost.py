def infixToPost(string: str):
    top = -1
    stack = []
    postfix = ''
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for char in string:
        print(f"{"Stack:"}{stack}{'\t\tPostfix:'}{postfix}")
        if char.isalpha():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[top] != '(':
                postfix += stack.pop()
            stack.pop()
        elif char in precedence:
            while stack[top] != '(' and stack and precedence[stack[top]] >= precedence[char]:
                postfix += stack.pop()
            stack.append(char)
    print("Postfix Expression: ", postfix)

def main():
    string = input('Enter the infix expression: ')
    infixToPost(string)

if __name__ == '__main__':
    main()

