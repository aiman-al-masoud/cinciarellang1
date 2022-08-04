from token_stream import TokenStream

class Parser:
    
    def __init__(self, ts:TokenStream):
        self.ts = ts

    def parse(self):
        return self.parse_statement()
    
    # S -> ES|SS|CS
    def parse_stmt(self):
        pass

    def parse_sel_stmt(self):
        pass

    def parse_comp_stmt(self):
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


    








    