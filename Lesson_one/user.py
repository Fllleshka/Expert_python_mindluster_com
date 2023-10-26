from Lesson_one.library import *

# Проверка на наличие такой функции классе наследуемом
#assert hasattr(Base, 'foo', "Такой функции нет. Оно сломано")

class Derived(Base):
    def bar(self):
        return 'bar'