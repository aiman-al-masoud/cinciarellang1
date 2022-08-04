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
 
        a = self.parse_exp()
        b = self.parse_comp_stmt()

        if self.ts.peek.val == 'else':
            self.ts.next() # eat 'else'
            c = self.parse_comp_stmt()
        
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
        self.ts.next() # eat ';'
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
        
        self.ts.peek
        

    def parse_cond_exp(self):
        pass

    def parse_or_exp(self):
        pass

    def parse_and_exp(self):
        pass

    def parse_eq_exp(self):
        pass

    def parse_add_exp(self):
        pass

    def parse_mul_exp(self):
        pass

    def parse_un_exp(self):
        pass

    def parse_un_op(self):
        pass# TODO: really?

    def parse_prim_exp(self):
        pass

    def parse_const(self): # AKA: literal
        pass

















    