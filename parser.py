from token_stream import TokenStream

class Parser:
    
    def __init__(self, ts:TokenStream):
        self.ts = ts

    def parse(self):
        # return self.parse_statement()
        pass


    # S -> ES|SS|CS
    def parse_stmt(self):

        if self.ts.peek.val == 'if':
            
            a = self.parse_sel_stmt()

        elif self.ts.peek.val == '{':
            
            a = self.parse_comp_stmt()

        else:
            a = self.parse_exp_stmt()

        return a



    def parse_sel_stmt(self):

        self.ts.next() # eat 'if'
 
        a = self.parse_exp() # condition
        b = self.parse_comp_stmt() # then
        c = None # else (optional)

        if self.ts.peek.val == 'else':
            self.ts.next() # eat 'else'
            c = self.parse_comp_stmt() # else
        
        return {'type' : 'if', 'cond' : a, 'then' : b, 'else': c}



    def parse_comp_stmt(self): # compound statement
        
        self.ts.next() # eat '{'

        res = []

        while self.ts.peek.val != '}':
            a = self.parse_stmt()
            res.append(a)

        self.ts.next() # eat '}'
        
        return {'type':'block', 'val':res}


    def parse_exp_stmt(self):
        a  = self.parse_exp()
        self.ts.next() # eat ';' # TODO: check semicolon presence
        return a


    def parse_func(self):# TODO: add params later
        
        self.ts.next() # eat 'fun'
        self.ts.next() # eat '('
        self.ts.next() # eat ')'
        a = self.parse_comp_stmt()
        return a


    def parse_exp(self):
        return self.parse_asgn_exp()


    def parse_asgn_exp(self):
        
        if self.ts.peek.type == 'id':
            a = self.ts.peek
            self.ts.next() # eat 'id'

        while True:

            if self.ts.peek.val == '=':
                self.ts.next() # eat '='
                
                if self.ts.peek.val == 'fun':
                    b = self.parse_func()
                else:
                    b = self.parse_cond_exp()

                a = {'type' : 'asgn', 'left' : a, 'right' : b}
            else:
                return a


    def parse_cond_exp(self):
        return self.parse_or_exp()

    def parse_or_exp(self):
        
        a = self.parse_and_exp()

        while True:
            if self.ts.peek.val == '||':
                self.ts.next() # eat '||'
                b = self.parse_and_exp()
                a = {'type' : 'or', 'left' : a, 'right' : b}
            else:
                return a


    def parse_and_exp(self):

        a = self.parse_eq_exp()

        while True:
            if self.ts.peek.val == '&&':
                self.ts.next() # eat '&&'
                b = self.parse_eq_exp()
                a = {'type' : 'and', 'left' : a, 'right' : b}
            else:
                return a

            
        


    def parse_eq_exp(self):

        a = self.parse_add_exp()

        while True:
            if self.ts.peek.val in "== != > < >= <=":
                op = self.ts.peek.val
                self.ts.next() # eat op
                b = self.parse_add_exp()
                a = {'type': op, 'left': a, 'right': b}
            else:
                return a

    def parse_add_exp(self):

        a = self.parse_mul_exp()

        while True:
            if self.ts.peek.val == "+":
                self.ts.next() # eat '+'
                b = self.parse_mul_exp()
                a = {'type' : 'add', 'left' : a, 'right' : b}
            elif self.ts.peek.val == "-":
                self.ts.next() # eat '-'
                b = self.parse_mul_exp()
                a = {'type' : 'sub', 'left' : a, 'right' : b}
            else:
                return a

    def parse_mul_exp(self):
        
        a = self.parse_un_exp()

        while True:
            if self.ts.peek.val == "*":
                self.ts.next() # eat '*'
                b = self.parse_un_exp()
                a = {'type' : 'mul', 'left' : a, 'right' : b}
            elif self.ts.peek.val == "/":
                self.ts.next() # eat '/'
                b = self.parse_un_exp()
                a = {'type' : 'div', 'left' : a, 'right' : b}
            else:
                return a

    def parse_un_exp(self):
        
        if self.ts.peek.val not in '-!':
            a = self.parse_prim_exp()

            if self.ts.peek.val == '(':
                b = self.parse_fun_call_args()
                return {'type' : 'call', 'name' : a, 'args' : b}

            return a

        else:
            op = self.ts.peek.val
            self.ts.next() # eat op
            b = self.parse_un_exp()
            return {'type': op, 'arg' : b}


    def parse_fun_call_args(self): # TODO: multiple args
        self.ts.next() # eat '('
        a = self.parse_asgn_exp()
        self.ts.next() # eat ')'
        return [a]

    def parse_prim_exp(self):

        if self.ts.peek.type == 'id': # var 
            a = self.ts.peek
            self.ts.next() # eat 'id'
            return a
        elif self.ts.peek.val == '(': # it's a bracketed expression
            self.ts.next() # eat '('
            a = self.parse_exp()
            self.ts.next() # eat ')'
            return a
        else: # it's a literal
            return self.parse_const()



    def parse_const(self): # AKA: literal

        if self.ts.peek.type == 'num':
            f = float(self.ts.peek.val)
            self.ts.next()
            return f
        elif self.ts.peek.type == 'bool': # TODO: in tokenstream
            b = self.ts.peek.val == 'true'
            self.ts.next()
            return b

        # TODO: string in tokenstream






from char_stream import CharStream
s = "x = y = 2;"


p = Parser(TokenStream(CharStream(s)))


x = p.parse_stmt()

print(x)





    