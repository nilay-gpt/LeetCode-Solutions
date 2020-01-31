

def match_paranthesis(expr):
    stack = []
    open_brackets_list = ['[', '(', '{']
    close_brackets_list = [']', ')', '}']
    brackets_relation_dict = {"}": "{", "]": "[", ")": "("}

    if len(expr)%2 != 0:
        return "false"
    if expr[0] in close_brackets_list or expr[-1] in open_brackets_list:
        return "false"

    for i in expr:
        if i in open_brackets_list:
            stack.append(i)
        elif i in close_brackets_list:
            open_value_of_i = brackets_relation_dict[i]
            if open_value_of_i == stack[-1]:
                stack.pop()
    if stack == []:
        return "true"
    else:
        return "false"



if __name__ == "__main__":
    # expr = "[()]{}{[()()]()}"
    expr = "(]"
    value = match_paranthesis(expr)
    print value
