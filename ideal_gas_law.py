def ideal_gas_law(p, v, n, r):
    return (n * r * p) / v

def main():
    p = float(input("Введите давление (Па): "))
    v = float(input("Введите объем (м^3): "))
    n = float(input("Введите количество вещества (моль): "))
    r = 8.31  # универсальная газовая постоянная в Дж/(моль*К)

    temperature = ideal_gas_law(p, v, n, r)
    print(f"Температура: {temperature:.2f} K")

if __name__ == '__main__':
    main()
