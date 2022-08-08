class Enviro:

    def __init__(self, parent:'Enviro'):
        self.vars:dict = (parent or {}) and parent.vars.copy() 

    def new_child(self):
        return Enviro(self)

    def get(self, key:str):
        return self.vars[key]

    def set(self, key:str, val):
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

if __name__ == "__main__":
    main()
