from stack import Stack

class InfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = Stack()
        output = ''

        for c in expr:
            if self.isOperand(c):
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()              
                else:
                    while (not self.stack.isEmpty()) and self.hasLessOrEqualPriority(c,self.stack.peek()):
                        output += self.stack.pop()
                    self.stack.push(c)

        while (not self.stack.isEmpty()):
            output += self.stack.pop()
        return output
