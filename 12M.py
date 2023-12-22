# Вычислить сумму знакопеременного ряда (-1)**n-1(|х**(2n)|)/(2n)!,
# где х-матрица ранга к (к и матрица задаются случайным образом), n - номер слагаемого.
# Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
# У алгоритма д.б. линейная сложность.
import numpy as np
def result_sum(det_x, t):
    n = 1
    fact = 1
    current_sum = 0
    det_x_pow = det_x

    first_term = (-1) * det_x_pow / fact
    current_sum += first_term

    while True:
        n += 1
        fact *= (2 * n - 1) * (2 * n)  # Вычисляем факториал в знаменателе
        det_x_pow *= np.dot(det_x, det_x)  # Вычисляем х**(2n)
        term = ((-1)**(n-1)) * det_x_pow / fact  # Вычисляем очередное слагаемое

        current_sum += term if n % 2 == 0 else -term

        if abs(term) < t:
            break

    return current_sum

while True:
    t = input("Введите желаемую точность вычислений (не равную нулю): ")
    try:
        t = int(t)
        if t == 0:
            print("Ошибка: значение точности не может быть равным нулю. Пожалуйста, введите другое значение.")
        else:
            break
    except ValueError:
        print("Ошибка: введите число")

k = np.random.randint(2, 6)
random_matrix = np.random.uniform(-1, 1, (k, k))
print("Сгенерирована матрица:\n", random_matrix)

det_x = np.linalg.det(random_matrix)
result = result_sum(det_x, t)

precision_format = "{:." + str(int(t)) + "f}"
print(f"Сумма знакопеременного ряда: {precision_format.format(result)}")
