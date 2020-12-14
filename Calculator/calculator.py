class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class Stack:
    def __init__(self):
        self.top = None
        self.count=0

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False


    def __len__(self):
        return self.count

    def push(self,value):
        new_node = Node(value)

        if self.isEmpty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.count += 1
        return


    def pop(self):
        if self.isEmpty():
            return
        elif self.__len__() == 1:
            pop_val = self.top
            self.top == None
            self.count -= 1
            return pop_val.value
        else:
            pop_val = self.top
            new_top = self.top.next
            self.top = new_top
            self.count -= 1
            return pop_val.value

    def peek(self):
        if self.top == None:
            return
        else:
            return self.top.value

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except:
            return False
        if txt.isspace() == True:
            return False

    def _getPostfix(self,txt):
            if not isinstance(txt,str) or len(txt.strip())==0:
                print("Argument error in _getPostfix")
                return None

            postfix_Stack=Stack()
            op_lst = ['+', '-', '*', '^', '/']
            num_lst = ['1','2','3','4','5','6','7','8','9','0','.']

            for i in txt: #checks for invalid char like $
                if i not in ['+', '-', '*', '^', '/','1','2','3','4','5','6','7','8','9','0','.','(', ')', ' ']:
                    return None

            if self.isNumber(txt) == True: #if there is only one number, it returns a float
                return str(float(txt))
            elif txt[-1] in op_lst: # checks if last char is an operator
                return None

            txt_lst = []  #creates a lst that strips txt of spaces and converts numbers to floats
            current = 0
            for i in range(len(txt)):
                if txt[i] in op_lst or txt[i] in ['(',')']:
                    num = txt[current:i].strip()
                    if num != '' and self.isNumber(num) == True:
                        txt_lst.append(float(num))
                    elif num != '' and self.isNumber(num) == False:
                        return None
                    txt_lst.append(txt[i])
                    current = i + 1
            if txt[current:len(txt)+1].isspace() == True:
                pass
            elif txt[-1] != ')':
                if self.isNumber(txt[current:len(txt)+1]) == True:
                    txt_lst.append(float(txt[current:len(txt)+1]))

            if len(txt_lst) == 0:
                return None
            elif txt_lst[0] in op_lst: #checks if first char is an operator
                return None

            i = 0  #checks for consecutive operations
            while i < len(txt_lst):
                if txt_lst[i] in op_lst and txt_lst[i+1] in ['+', '-', '*', '^', '/', ')']:
                    return None
                i += 1

            parenthesis = []  #checks for balanced parenthesis
            for i in txt:
                if i == '(':
                    parenthesis.append(i)
                elif i == ')':
                    if len(parenthesis) == 0:
                        return None
                    elif parenthesis[-1] == '(':
                        parenthesis.pop()
            if len(parenthesis) != 0:
                    return None

            if '+' not in txt and '-' not in txt and '*' not in txt and '/' not in txt and '^' not in txt:  #if there is a num in parenthesis, it returns float of num
                leftpar = [txt.index(i) for i in txt if i == '(']
                rightpar = [txt.index(i) for i in txt if i == ')']
                if ' ' in txt:
                    return None
                elif self.isNumber(txt[len(leftpar) : rightpar[0]]) == True:
                    return str(float(txt[len(leftpar) : rightpar[0]]))
                else:
                    return None

            prec = {'+':1, '-':1, '*': 2, '/':2, '^':3, '(': 0 , ')': 0}
            res = []

            for i in txt_lst: #postfix conversion
                if type(i) == float:
                    res.append(i)
                elif i == '(':
                    postfix_Stack.push(i)
                elif i == ')':
                    while postfix_Stack.isEmpty() == False and postfix_Stack.peek() != '(':
                        pop = postfix_Stack.pop()
                        res.append(pop)
                    if postfix_Stack.isEmpty() == False and postfix_Stack.peek() != '(':
                        return None
                    else:
                        postfix_Stack.pop()
                else:
                    if postfix_Stack.isEmpty() or prec[i] > prec[postfix_Stack.peek()]:
                        postfix_Stack.push(i)
                    elif prec[i] <= prec[postfix_Stack.peek()]:
                        while postfix_Stack.__len__() > 0 and prec[i] <= prec[postfix_Stack.peek()]:
                            res.append(postfix_Stack.peek())
                            postfix_Stack.pop()
                        postfix_Stack.push(i)


            while postfix_Stack.isEmpty() == False:
                res.append(postfix_Stack.peek())
                postfix_Stack.pop()

            str_res = []
            for i in res:
                if type(i) != str:
                    str_res.append(str(i))
                else:
                    str_res.append(i)

            return ' '.join(str_res)


    @property
    def calculate(self):
        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculator_Stack=Stack()
        postfix = self._getPostfix(self.__expr)

        if postfix == None: #if postfix is not possible, it returns None
            return None

        postfix_lst = postfix.split() #splits postfix from get postfix into a lst based on spaces


        for i in postfix_lst:  #calculates the postfix if possible
            if self.isNumber(i) == True:
                calculator_Stack.push(i)
            else:
                num1 = float(calculator_Stack.pop())
                num2 = float(calculator_Stack.pop())
                if i == '+':
                    res = num2 + num1
                    calculator_Stack.push(res)
                elif i == '-':
                    res = num2 - num1
                    calculator_Stack.push(res)
                elif i == '*':
                    res = num2 * num1
                    calculator_Stack.push(res)
                elif i == '/':
                    res = num2 / num1
                    calculator_Stack.push(res)
                elif i == '^':
                    res = num2 ** num1
                    calculator_Stack.push(res)
        return calculator_Stack.peek()
