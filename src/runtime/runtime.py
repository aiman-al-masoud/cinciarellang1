try: from enviro import Enviro
except: from .enviro import Enviro
try: from fun import Fun, Print, Object
except: from .fun import Fun, Print, Object, Get, Set


class Runtime:

    def __init__(self):
        self.enviro_stack = []
        self.enviro_stack.append(Enviro(None)) # global
        self.env.set('print', Print(self.eval))
        self.env.set('chirp', Print(self.eval))
        self.env.set("obj", Object())
        self.env.set("get", Get(self.eval))
        self.env.set("set", Set(self.eval))


    @property
    def env(self): # current environment
        return self.enviro_stack[-1]
    
    def exit_env(self):
        if len(self.enviro_stack) > 1: # 'cuz keep global
            self.enviro_stack.pop()

    def enter_env(self, env:Enviro):
        self.enviro_stack.append(env)

    def eval(self, ast):#:dotdict):

        if ast is None:
            return False

        if ast['type'] in ['num', 'str', 'bool']:
            return ast['val']

        if ast['type'] == 'id':
            return self.env.get(ast['val'])

        if ast['type'] == '=': # assignment
            rv = self.eval(ast['right'])
            self.env.set(ast['left']['val'], rv)
            return rv 

        if ast['type'] in ['add', 'sub', 'mul', 'div', 'or', 'and', '==', '!=', '>', '<', '>=', '<=']:
            return self.apply_op(ast['type'], self.eval(ast['left']), self.eval(ast['right']))

        if ast['type'] == 'block':
            r = None
            for s in ast['val']:
                r = self.eval(s)
            return r

        if ast['type'] == 'if':
            
            if self.eval(ast['cond']):
                return self.eval(ast['then']) 

            if 'else' in ast: 
                return self.eval(ast['else'])


        if ast['type'] == 'fun':
            return self.make_fun(ast) # lol

        if ast['type'] == 'call':
            
            f:Fun = self.env.get(ast['name']['val'])
            e:Enviro = self.env.new_child()


            if ast['name']['val'] in ['eval', 'import']: # eval and import run in the gloval scope/env!
                r = f.run(ast['args'], e)
            else:
                self.enter_env(e)
                r = f.run(ast['args'], e)
                self.exit_env()

            return r

        if ast['type'] == '-':
            return -1*self.eval(ast['arg'])
        
        if ast['type'] == '!':
            return not self.eval(ast['arg'])
        


    def apply_op(self, op:str, left, right):
        
        if op == 'add':
            return left + right
        
        if op == 'sub':
            return left - right

        if op == 'mul':
            return left * right

        if op == 'div':
            return left / right

        if op == '==':
            return left == right
        
        if op == '!=':
            return left != right

        if op == ">":
            return left > right

        return eval(f"{left} {op} {right}") # TODO unsafe python eval (remove later)
        
        
    def make_fun(self, fun): # lol
        return Fun(fun['params'], fun['body'], self.eval)#self.env, self.eval)


