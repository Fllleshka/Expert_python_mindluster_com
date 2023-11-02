from Lesson_one.user import *

from time import time

class Class_for_lessons:

    def __init__(self):
        self.first_lesson()

    # Первый урок
    def first_lesson(self):

        # Класс полином
        class Polynomial:
            def __init__(self, *coeffs):
                self.coeffs = coeffs
            def __repr__(self):
                return 'Polynomial(*{!r})'.format(self.coeffs)
            def __add__(self, other):
                return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))
            def __len__(self):
                return len(self.coeffs)
            def __call__(self):
                pass
        p1 = Polynomial(1,2,3) #  x² + 2x + 3
        p2 = Polynomial(3,4,3) # 3x² + 4x + 3
        print(p1+p2)

        # Метакласс
        user_class = Derived()
        user_class.bar()

        # Декораторы
        # Рукописный декоратор
        class My_Decorator:
            def __init__(self, function):
                self.function = function
            def __call__(self, *args, **kwargs):
                self.function(*args, **kwargs)
                self.before = time()
                self.after = time()
                print(f"Start: {self.before}\t\tEnd: {self.after}\t\tDifference: {self.after - self.before}")
        @My_Decorator
        def add(x, y = 10):
            return x + y
        @My_Decorator
        def sub(x, y = 10):
            return x - y

        #dec_class = Decorators()
        print(f"add(3,7)\t\t{add(3, 7)}")
        print(f"add(20,)\t\t{add(20)}")
        print(f"add('a','b')\t{add('a', 'b')}")
        print(f"sub(3,7)\t\t{sub(3, 7)}")
        print(f"sub(20,)\t\t{sub(20, 0)}")

if __name__ == '__main__':
    my_class = Class_for_lessons()
