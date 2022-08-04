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

            self.ts.next() # eat 'if'
            a = self.parse_sel_stmt()

        elif self.ts.peek.val == '{':

            self.ts.next() # eat '{'
            a = self.parse_comp_stmt()
            self.ts.next() # eat '}'
        
        else:
            self.parse_exp_stmt()




    def parse_sel_stmt(self):
        
        a = self.parse_exp()
        




    def parse_comp_stmt(self): # compound statement
        pass

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

















    