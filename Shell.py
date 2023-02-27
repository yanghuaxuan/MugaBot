class _MugaTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self, newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def getKey(self):
        return self.key
    def setKey(self, obj):
        self.root = obj


class _AST(_MugaTree):
    def _infix_to_postfix(infix):
        op = []
        num = ""
        postfix = ""

        # Iterate through infix string
        for i in infix:
            # Extract the number
            if i.isdigit() or i == "." :
                num += i
            # After successfully extracting number, add to postfix
            elif len(num) > 0:
                postfix += (num + ' ')
                num = ""

            if i == '(':
                op.append('(')
            if i == ')':
                # Add operators in op stack to postfix
                while len(op) != 0 and op[-1] != '(':
                    postfix += (op.pop() + ' ')
                # Parantheses not needed for postfix
                if op[-1] == '(':
                    op.pop()

            if i in '+-*/^':
                # Pemdas implementation via dictionary
                pemdas = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4, ')': 4}
                # Add to stack if operator has higher precedence than the previous operator in the op stack
                if len(op) != 0 and pemdas[i] > pemdas[op[-1]]:
                    op.append(i)
                # Else, pop previous operator to postfix, then add new operator to the op stack
                else:
                    if len(op) != 0 and op[-1] != "(":
                        postfix += (op.pop())
                    op.append(i)
        # Add remaining operators and numbers
        postfix += (num)
        while len(op) != 0:
            postfix += " "
            postfix += op.pop()

        return postfix

    def process(cmd: str):
        stack = []
        operator = '+-/*^'

        cmd = cmd.replace(" ", "")

        num = ""

        postfix = _AST._infix_to_postfix(cmd) 

        for i in postfix:
            # Account for multi-digit and floating point number
            if i.isdigit() or i == '.':
                num += i
            elif num != "":
                # Add the finished num as a node to the stack
                stack.append(_AST(num))
                num = ""
            if i in operator: # Create operator node
                temp = _AST(i)
                temp.rightChild = stack.pop()
                temp.leftChild = stack.pop()
                stack.append(temp)

        return stack.pop()



class MugaShell():
    def __init__(self):
        history = []

    def eval(tree):
        operator = '+-/*^'
        # Do nothing if there's nothing
        if tree == None:
            return None
        else:
            if tree.getKey() not in operator:
                return float(tree.getKey())
            # Get our left and right values
            valL = MugaShell.eval(tree.getLeftChild())
            valR = MugaShell.eval(tree.getRightChild())

            # Calculate left and right values given operator
            valN = tree.getKey()
            if valN == "+":
                return valL + valR
            elif valN == "-":
                return valL - valR
            elif valN == "*":
                return valL * valR
            elif valN == "/":
                return valL / valR
            elif valN == "^":
                return valL ** valR

    def process_cmd(self, cmd: str):
        if cmd == "":
            return ""

        tree = _AST.process(cmd)
        return MugaShell.eval(tree)
            
