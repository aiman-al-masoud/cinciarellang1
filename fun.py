from enviro import Enviro

class Fun:

    def __init__(self, params, body, env:Enviro, _eval):
        self.env = env
        self.params = params
        self.body = body
        self.eval = _eval

    def bind_args(self, args):
        for i, arg in enumerate(args):
            self.env.set(self.params[i], self.eval(arg))

    def run (self, args):
        
        return self.eval(self.body)
