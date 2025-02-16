from infixToPost import infixToPost

def reverse(string):
    res = ""
    for i in string[::-1]:
        if i == '(':
            res += ')'
        elif i == ')':
            res += '('
        else:
            res += i
    return res

def infixToPost(string: str):
    top = -1
    stack = []
    postfix = ''
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for char in string:
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
    return postfix

def main():
    string = input("Enter the expression in brackets: ")
    string = reverse(string)
    result = infixToPost(string)
    print(result[::-1])

if __name__ == "__main__":
    main()
