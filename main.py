from Lesson_one.user import *

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

if __name__ == '__main__':
    my_class = Class_for_lessons()
