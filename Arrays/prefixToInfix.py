import sys

def preToIn(string):
    stack = []
    for i in range(1, len(string)+1):
        if string[-i] in "+-/*":
            a = stack.pop()
            b = stack.pop()
            stack.append("( %s %s %s )" %(a, string[-i], b))
        else:
            stack.append(string[-i])

    return stack.pop()

def main():
    args = sys.argv
    result = preToIn(args[1])
    print(result)


if __name__ == "__main__":
    main()
