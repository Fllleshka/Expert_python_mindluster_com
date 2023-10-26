class Base:
    def food(self):
        return self.bar()

old_bc = __build_class__
def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('Проверка метода.')
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__ = my_bc