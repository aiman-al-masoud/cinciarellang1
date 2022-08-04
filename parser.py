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
            self.parse_exp_stmt()




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
        pass

    def parse_func(self):
        pass

    def parse_exp(self):
        pass

    def parse_asgn_exp(self):
        pass

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

















    