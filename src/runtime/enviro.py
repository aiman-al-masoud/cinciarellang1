class Enviro:

    def __init__(self, parent:'Enviro'):
        # print("creation of new env from:", parent)
        self.parent = parent
        self.vars:dict = {} if not parent else parent.vars

    def new_child(self):
        return Enviro(self)

    def get(self, key:str):
        # print('vars:',self.vars,'key:', key)
        return self.vars[key]

    def set(self, key:str, val):

        if self.parent and (self.vars is self.parent.vars):
            self.vars = self.vars.copy()

        self.vars[key] = val

    def __repr__(self):
        return str(self.vars)


def main():
    e = Enviro(None)
    e.set('x', 1)
    e.set('y', 1)

    v = e.new_child()
    # print(e)
    print(v)
    v.set('x', 'capra')
    print(v)
    print(e)

if __name__ == "__main__":
    main()
