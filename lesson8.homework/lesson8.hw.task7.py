# № 7
#
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:

    def __init__(self, real, imag=0):
        self.complex = complex(real, imag)

    def __add__(self, other):
        other = other.complex
        z = self.complex + other
        return ComplexNumber(z.real, int(z.imag))

    # def __sub__(self, other):
    #     other = other.complex
    #     z = self.complex - other
    #     return ComplexNumber(z.real, int(z.imag))

    def __mul__(self, other):
        other = other.complex
        z = self.complex * other
        return ComplexNumber(z.real, int(z.imag))

    # def __truediv__(self, other):
    #     other = other.complex
    #     z = self.complex / other
    #     return ComplexNumber(z.real, int(z.imag))

    def __str__(self):
        return self.complex.__str__()


z1 = ComplexNumber(5, -7)
z2 = ComplexNumber(6, 4)

print(z1 + z2, complex(5, -7) + complex(6, 4))
# print(z1 - z2, complex(5, -7) - complex(6, 4))
print(z1 * z2, complex(5, -7) * complex(6, 4))
# print(z1 / z2, complex(5, -7) / complex(6, 4))
