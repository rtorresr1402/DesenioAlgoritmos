def count(coins, n, sum):
    # Si la suma es 0, entonces hay una solución (no incluir ninguna moneda)
    if sum == 0:
        return 1

    # Si la suma es menor que 0, no hay solución
    if sum < 0:
        return 0

    # Si no hay monedas y la suma es mayor que 0, no hay solución
    if n <= 0:
        return 0

    # Cuenta es la suma de soluciones (i) incluyendo la moneda n-1 (ii) excluyendo la moneda n-1
    return count(coins, n - 1, sum) + count(coins, n, sum - coins[n - 1])

# Programa para probar la función anterior
coins = [1, 2, 3]
n = len(coins)
print(count(coins, n, 5))
