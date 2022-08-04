class CharStream:
    
    def __init__(self, string):
        self.string = string+""# TODO: properly fix this stupid hack, I think it's fixed now
        self.pos, self.row, self.col = 0, 0, 0

    def next(self):
        self.pos+=1
        
        try:
            c = self.peek()
            if c == "\n":
                self.row+=1
                self.col = 0
            else:
                self.col+=1
        except:
            pass
        


    def peek(self)->'str':
        try:
            return self.string[   self.pos  ] 
        except:
            pass
    
    def croak(self, msg):
        raise Exception(f"{msg} at row: {self.row}, col: {self.col}")

    def eof(self):
        return self.pos == len(self.string)    

# s = CharStream("hello world!")
# # while not s.eof():
# #     print(s.peek())
# #     s.next()

# s.next()
# s.croak("error: ")
