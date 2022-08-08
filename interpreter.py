from enviro import Enviro
from parser import dotdict
from fun import Fun


class Interpreter:

    def __init__(self):
        self.enviro_stack = []
        self.enviro_stack.append(Enviro(None)) # global

    @property
    def env(self): # current environment
        return self.enviro_stack[-1]
    
    def exit_env(self):
        if len(self.enviro_stack) > 1: # 'cuz keep global
            self.enviro_stack.pop()

    def enter_env(self, env:Enviro):
        self.enviro_stack.append(env)

    def eval(self, ast:dotdict):
        
        if ast.type in ['num', 'str', 'bool']:
            return ast.val

        if ast.type == 'var':
            return self.env.get(ast.val)

        if ast.val == '=': # assignment
            rv = self.eval(ast.right)
            self.env.set(ast.left['val'], rv)
            return rv 

        if ast.type in ['add', 'sub', 'mul', 'div', 'or', 'and', '==', '!=', '>', '<', '>=', '<=']:
            return self.apply_op(ast.type, self.eval(ast.left), self.eval(ast.right))

        if ast.type == 'block':
            r = None
            for s in ast.val:
                r = self.eval(s)
            return r

        if ast.type == 'if':
            
            if self.eval(ast.cond):
                return self.eval(ast.then) 

            if 'else' in ast: 
                return self.eval(ast['else'])


        if ast.type == 'fun':
            return self.make_fun(ast)

        if ast.type == 'call':
            
            f:Fun = self.env.get(ast.name)
            self.enter_env(f.env)
            r = f.run(ast.args)
            self.exit_env()
            return r


    def apply_op(self, op:str, left, right):
        
        if op == 'add':
            return left + right
        
        if op == 'sub':
            return left - right

        if op == 'mul':
            return left * right

        if op == 'div':
            return left / right

        return eval(f"{left} {op} {right}") # TODO unsafe python eval (remove later)
        
        
    def make_fun(self, fun): # lol
        return Fun(fun.params, fun.body, self.env, self.eval)


