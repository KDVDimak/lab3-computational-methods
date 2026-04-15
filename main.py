# Модель: Обчислення значення функції та оцінка похибок (5 семестр)
# Автор: Кривонос Дмитро, група АІ-231

from decimal import Decimal, getcontext

getcontext().prec = 30


def task1():
    print("=== Завдання 1 ===")

    a, Da = 16.5, 0.05
    b, Db = 4.12, 0.005
    c, Dc = 0.198, 0.0005

    f = (a * c) / (a - b**2)

    rel_ac = Da / a + Dc / c
    delta_ac = abs(a * c) * rel_ac

    delta_b2 = 2 * b * Db
    delta_d = Da + delta_b2
    rel_d = delta_d / abs(a - b**2)

    rel_f = rel_ac + rel_d
    df_rules = abs(f) * rel_f

    df_da = -(c * b**2) / (a - b**2) ** 2
    df_db = (2 * a * b * c) / (a - b**2) ** 2
    df_dc = a / (a - b**2)

    df_formula = abs(df_da) * Da + abs(df_db) * Db + abs(df_dc) * Dc

    print(f"f = {f:.5f}")
    print(f"Δf (за правилами) ≈ {df_rules:.3f}")
    print(f"Δf (за формулою) ≈ {df_formula:.3f}")
    print(f"Результат: f = {f:.2f} ± {df_rules:.2f}")
    print()


def task2():
    print("=== Завдання 2 ===")

    true1 = Decimal(7) / Decimal(22)
    approx1 = Decimal("0.318")
    abs1 = abs(true1 - approx1)
    rel1 = abs1 / true1 * 100

    true2 = Decimal(13).sqrt()
    approx2 = Decimal("3.60")
    abs2 = abs(true2 - approx2)
    rel2 = abs2 / true2 * 100

    print(f"7/22 відносна похибка = {rel1:.4f}%")
    print(f"sqrt(13) відносна похибка = {rel2:.4f}%")

    if rel1 < rel2:
        print("Точніша рівність: 7/22 ≈ 0.318")
    else:
        print("Точніша рівність: sqrt(13) ≈ 3.60")


def main():
    task1()
    task2()


if __name__ == "__main__":
    main()