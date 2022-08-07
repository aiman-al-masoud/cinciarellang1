from char_stream import CharStream


class Token(dict):
    
    def __init__(self, _type:str, val:str):
        self.type = _type
        self.val = val
        self['type'] = _type
        self['val'] = val

class TokenStream:

    def __init__(self, cs: CharStream):
        self.cs = cs
        self.current:'{}' = None 
        self.next() # get initial token 

    def next(self):

        self.skip_whitespace()

        c = self.cs.peek()

        if c is None:
            return 

        if TokenStream.is_comment_start(c):
            self.skip_comment()
            self.next()
            return 

        if c.isnumeric():
            s = self.read_while(lambda c : c.isnumeric())
            self.current  = {'type':'num', 'val': s}
            return 
        
        if TokenStream.is_id_start(c):
            s = self.read_while(lambda c : TokenStream.is_id(c))
            self.current =  {'type': 'kw' if TokenStream.is_kw(s) else 'id', 'val':s}
            return 

        if TokenStream.is_op(c):
            s = self.read_while(lambda c : TokenStream.is_op(c))
            self.current = {'type':'op', 'val':s}
            return 

        if TokenStream.is_punc(c):
            self.current = {'type':'punc', 'val': c}
            self.cs.next()
            return 

        if TokenStream.is_str_delim(c):
            self.cs.next() # eat "
            s = self.read_while(lambda c: not TokenStream.is_str_delim(c))
            print("read str:", s)
            self.current = {'type' : 'str', 'val' : s}
            print("char after:", self.cs.peek())
            self.cs.next() # eat "
            print("char after eating end quote:", self.cs.peek())
            return 


        self.croak("Unexpected char")

    @property
    def peek(self)->Token:
        return Token(self.current['type'], self.current['val'])

    def croak(self, msg):
        self.cs.croak(msg)

    def eof(self):
        return self.cs.eof() # TODO: maybe problematic


    @staticmethod
    def is_id_start(c:'str'):
        return c.isalpha() or (c in '_')

    @staticmethod
    def is_id(c:'str'):
        return TokenStream.is_id_start(c) or c.isnumeric()

    @staticmethod
    def is_op(c:'str'):
        return c in '+-*/=!<>|&'
    
    @staticmethod
    def is_punc(c:'str'):
        return c in '(){},;'
    
    @staticmethod
    def is_comment_start(c:'str')->'bool':
        return c=="#"

    @staticmethod
    def is_kw(s:'str'):
        return s in ['true', 'false', 'if', 'else', 'fun']
    
    @staticmethod
    def is_str_delim(c:'str')->'bool':
        return c=='"'


    def read_while(self, predicate)->'str':

        s = ""
        while not self.cs.eof() and predicate(self.cs.peek()):
            s+=self.cs.peek()
            
            try:
                self.cs.next()
            except IndexError as e:
                pass

        return s

    def skip_comment(self):
        self.read_while(lambda c : c != '\n')
        self.cs.next() # skip the newline

    def skip_whitespace(self):
        self.read_while(lambda c : c in ' \n\t')
    



# source = "#ciao\n#ciao\na+2+34*(4*1)"
# source = "1+1"

# source = """
#          f = fun(){
#             y = 1;
#          }

#          f(1)*8;
#          """

# ts = TokenStream(CharStream(source))


# print(ts.peek) # initial token
# # ts.next()

# while not ts.eof():
#     print(ts.peek)
#     ts.next()



