from enviro import Enviro

class Fun:

    def __init__(self, params, body, env:Enviro, _eval):
        self.env = env.new_child()
        # print("fun's env:", self.env)
        self.params = params
        self.body = body
        self.eval = _eval

    def bind_args(self, args):
        for i, arg in enumerate(args):
            self.env.set(self.params[i]['val'], self.eval(arg))

    
    def run (self, args):
        # global x 
        print("call with args:", args)
        # if x > 10:
            # exit()
        # x +=1
        self.bind_args(args)
        return self.eval(self.body)

# x = 1


# new env should be created from parent env at function's runtime,
# or else recursive calls to the function will have trouble reaching the 
# base case.
#