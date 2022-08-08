from enviro import Enviro

class Fun:

    def __init__(self, params, body, _eval):
        self.params = params
        self.body = body
        self.eval = _eval

    def bind_args(self, args, env:'Enviro'):
        for i, arg in enumerate(args):
            env.set(self.params[i]['val'], self.eval(arg))
    
    def run (self, args, env):
        self.bind_args(args, env)
        return self.eval(self.body)


# new env should be created from parent env at function's runtime,
# or else recursive calls to the function will have trouble reaching the 
# base case.
#