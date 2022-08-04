from token_stream import TokenStream

class Parser:
    
    def __init__(self, ts:TokenStream):
        self.ts = ts

    def parse(self):
        return self.parse_statement()
    
    def parse_statement(self):
        pass

    




    