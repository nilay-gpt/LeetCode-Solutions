"""
2 3 1 * + 9 -
Let the given expression be “2 3 1 * + 9 -“. We scan all elements one by one.
1) Scan ‘2’, it’s a number, so push it to stack. Stack contains ‘2’
2) Scan ‘3’, again a number, push it to stack, stack now contains ‘2 3’ (from bottom to top)
3) Scan ‘1’, again a number, push it to stack, stack now contains ‘2 3 1’
4) Scan ‘*’, it’s an operator, pop two operands from stack, apply the * operator on operands, we get 3*1 which results in 3. We push the result ‘3’ to stack. Stack now becomes ‘2 3’.
5) Scan ‘+’, it’s an operator, pop two operands from stack, apply the + operator on operands, we get 3 + 2 which results in 5. We push the result ‘5’ to stack. Stack now becomes ‘5’.
6) Scan ‘9’, it’s a number, we push it to the stack. Stack now becomes ‘5 9’.
7) Scan ‘-‘, it’s an operator, pop two operands from stack, apply the – operator on operands, we get 5 – 9 which results in -4. We push the result ‘-4’ to stack. Stack now becomes ‘-4’.
8) There are no more elements to scan, we return the top element from stack (which is the only element left in stack).
"""


class PostfixEvaluate(object):
    def __init__(self, exp):
        self.exp = exp
        self.exp_len = len(exp)
        self.stack = []
        self.evaluate_postfix()

    def evaluate_postfix(self):
        for item in self.exp:
            if item.isdigit():
                self.stack.append(item)
            else:
                item1, item2, = self.pop_last_two_items()
                print item1, item2
                self.stack.append(self.do_operation(item1, item2, item))

        return self.stack

    def pop_last_two_items(self):
        item1 = self.stack.pop()
        item2 = self.stack.pop()
        return item1, item2

    def do_operation(self, item1, item2, item):
        return str(eval(item2 + item + item1))



if __name__ == "__main__":
    exp = "231*+9--"
    result = PostfixEvaluate(exp)
    print result
