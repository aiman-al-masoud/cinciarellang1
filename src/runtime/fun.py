try: from enviro import Enviro
except: from .enviro import Enviro


class Fun:

    def __init__(self, params, body, _eval):
        self.params = params
        self.body = body
        self.eval = _eval

    def bind_args(self, args, env:'Enviro'):
        for i, arg in enumerate(args):
            env.set(self.params[i]['val'], self.eval(arg))
    
    def run (self, args, env:Enviro):
        self.bind_args(args, env)
        return self.eval(self.body)


# the following are wrappers around python functions:

class Print:

    def __init__(self, _eval):
        self.eval = _eval

    def run(self, args, env:Enviro):
        print(*[self.eval(arg) for arg in args])


class Object:

    def run(self, args, env:Enviro):
        return {}


class Get:

    def __init__(self, _eval):
        self.eval = _eval

    def run(self, args, env:Enviro):
        d = self.eval(args[0])
        k = self.eval(args[1])
        return d[k] # TODO: handle key error

class Set:

    def __init__(self, _eval):
        self.eval = _eval

    def run(self, args, env:Enviro):
        d = self.eval(args[0])
        k = self.eval(args[1])
        v = self.eval(args[2])
        d[k] = v
        return d