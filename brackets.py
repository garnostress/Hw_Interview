from stack import Stack


def is_line_correct(line):
    bracket_pair = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<'
    }
    open_brackets = bracket_pair.values()
    closed_brackets = bracket_pair.keys()
    stack = Stack()

    for char in line:
        if char in open_brackets:
            stack.push(char)
        elif char in closed_brackets:
            try:
                top = stack.peek
            except IndexError:
                return False
            if bracket_pair[char] == top:
                stack.pop
            else:
                return False
    return stack.size == 0


if __name__ == "__main__":
    line = input('введите строку: ').strip()
    result = is_line_correct(line)
    if result:
        print('Сбалансировано')
    else:
        print('Несбалансировано')