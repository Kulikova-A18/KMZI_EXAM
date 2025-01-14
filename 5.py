def mod_exp(base, exp, mod):
    """Возводит base в степень exp по модулю mod."""
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # если exp нечетное
            result = (result * base) % mod
        exp = exp >> 1  # делим exp на 2
        base = (base * base) % mod
    return result

# Данные
p = 67  # Простое число
g = 2   # Генератор
y = 7   # Открытый ключ

# a) Найти соответствующий открытый текст для шифртекста (u, v) = (3, 45)
u, v = 3, 45

print("Шифртекст (u, v):", (u, v))

# Определим секретный ключ x
print("\nПоиск секретного ключа x:")
print(f"y = g^x mod p => {y} = {g}^x mod {p}")
secret_key = None
for x in range(p):
    computed_y = mod_exp(g, x, p)
    print(f"Пробуем x = {x}: {g}^{x} mod {p} = {computed_y}")
    if computed_y == y:
        secret_key = x
        print(f"Найден секретный ключ: x = {secret_key}")
        break

# Теперь можем найти открытый текст
print("\nВосстановление открытого текста m:")
print(f"m = v * (y^-x mod p) mod p")

# Находим y^-x mod p
y_inv_x = mod_exp(y, p - 1 - secret_key, p)
print(f"Находим y^-x mod p: y^-{secret_key} ≡ {y_inv_x} (mod {p})")

m = (v * y_inv_x) % p
print(f"m = {v} * {y_inv_x} mod {p} ≡ {m} (mod {p})")
print(f"Открытый текст m: {m}")

# b) Зашифровать сообщение 21
message = 21
import random

# Случайное k
k = random.randint(1, p - 2)
print("\nШифрование сообщения:", message)
print(f"Выбираем случайное k: k = {k}")

# Вычисляем u и v для зашифрованного сообщения
u_new = mod_exp(g, k, p)
v_new = (message * mod_exp(y, k, p)) % p

print(f"Вычисляем u: u = g^k mod p => u = {g}^{k} mod {p} ≡ {u_new} (mod {p})")
print(f"Вычисляем v: v = m * (y^k mod p) => v = {message} * ({y}^{k} mod {p})")
print(f"Сначала находим y^{k} mod {p}: y^{k} ≡ {mod_exp(y, k, p)} (mod {p})")
print(f"Теперь находим v: v ≡ {message} * ({mod_exp(y, k, p)}) mod {p} ≡ {v_new} (mod {p})")

print(f"\nЗашифрованное сообщение: (u, v) = ({u_new}, {v_new})")
