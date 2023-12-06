from Lesson_one.user import *

from time import time
from time import sleep
from sqlite3 import connect
from contextlib import contextmanager

# Класс для уроков
class Class_for_lessons:

    def __init__(self):
        #self.first_lesson()
        #self.second_lesson()
        self.third_lesson()

    # Первый урок | What Does It Take To Be An Expert At Python
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
        # Рукописный декоратор времени работы функции
        def Decorator_timer(func):
            def f(*args, **kwargs):
                before = time()
                rv = func(*args, **kwargs)
                after = time()
                print(f"Start: {before}\t\tEnd: {after}\t\tDifference: {after - before}")
                return rv
            return f
        # Рукописный декоратор количества раз выполняемой функции
        def ntimes_decorator(n):
            def inner(f):
                def wrapper(*args, **kwargs):
                    for _ in range(n):
                        print('Running {.__name__}'.format(f))
                        rv = f(*args, **kwargs)
                    return rv
                return wrapper
            return inner

        @ntimes_decorator(2)
        def add(x, y = 10):
            return x + y
        @ntimes_decorator(3)
        def sub(x, y = 10):
            return x - y
        @Decorator_timer
        def fore(x, y = 10):
            result = x
            for elem in range(0, x*10):
                result = result * y
            return result

        print(f"add(20,)\t\t{add(20)}")
        print(f"add('a','b')\t{add('a', 'b')}")
        print(f"sub(3,7)\t\t{sub(3, 7)}")
        print(f"sub(20,)\t\t{sub(20, 0)}")
        print(f"add(3,7)\t\t{fore(3, 7)}")

        # Генераторы
        def add1(x, y):
            return x + y
        class Adder:
            def __call__(self, x, y):
                return x + y

        print(f"Adder1:\t{add1(10, 20)}\t{type(add1)}")
        add2 = Adder()
        print(f"Adder2:\t{add2(10, 20)}\t{type(add2)}")

        # Функция каких либо вычислений
        def compute():
            rv = []
            for i in range(10):
                sleep(.5)
                rv.append(i)
            return rv
        print(f"Compute:\t{compute()}")

        # Класс каких либо вычислений
        class Compute():
            def __iter__(self):
                self.last = 0
                return self
            def __next__(self):
                rv = self.last
                self.last += 1
                if self.last > 10:
                    raise StopIteration()
                sleep(.5)
                return rv
        for val in Compute():
            print(val)
        def compute_gen():
            for i in range(10):
                sleep(.5)
                yield i
        for val in compute_gen():
            print(val)

        '''
        # Контент-менеджер
        class contextmanager:
            def __init__(self, gen):
                self.gen = gen
            def __call__(self, *args, **kwargs):
                self.args, self.kwargs = args, kwargs
                return self
            def __enter__(self):
                self.gen_inst = self.gen(*self.args, **self.kwargs)
                next(self.gen_inst)
            def __exit__(self, *args):
                next(self.gen_inst, None)
        '''
        @contextmanager
        def tempteble(cur):
            cur.execute('create table points(x int, y int)')
            try:
                yield
            finally:
                cur.execute('drop table points')

        with connect('test.db') as conn:
            cur = conn.cursor()
            with tempteble(cur):
                cur.execute('insert into points (x, y) values(1, 1)')
                cur.execute('insert into points (x, y) values(1, 2)')
                cur.execute('insert into points (x, y) values(2, 1)')
                for row in cur.execute('select x, y from points'):
                    print(row)
                for row in cur.execute('select sum(x * y) from points'):
                    print(row)

    # Второй урок | Creating Awesome 3D Animations With Python In Blender
    def second_lesson(self):
        # Тут рассматривался Blender и применение библиотек python в построении кубов, кривых на плоскости
        pass

    # Третий урок | Top To Down Left To Right || James Powell
    def third_lesson(self):
        pass
        '''
        Python откладывет выполение функции на RunTime.
        К примеру поиск "a.b" выясним так ли это только когда код будет запущен.
        На этапе компиляции Python не будет выяснять что это ошибка.
        
        Принцип TOP->BOTTOM, LEFT->REGHT говорит что при перевода кода в байты python не анализирает код, а просто его выполняет.
        '''

    # Третий урок | Top To Down Left To Right || James Powell
    def fourth_lesson(self):
        pass


if __name__ == '__main__':
    my_class = Class_for_lessons()
