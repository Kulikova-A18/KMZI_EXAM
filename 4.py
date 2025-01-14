s_box_table = [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
inverse_s_box_table = [14, 6, 12, 10, 5, 3, 15, 1, 0, 9, 4, 13, 7, 11, 2, 8]

p_indices = [1, 8, 3, 5, 7, 4, 6, 2]
inverse_p_indices = [8, 1, 5, 6, 4, 7, 2, 3]

def inverse_function(func):
    """Декоратор для автоматического преобразования функций в их обратные."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__name__ = f'inverse_{func.__name__}'
    return wrapper

@inverse_function
def s_box(input_bits):
    """S-блок"""
    left = int(input_bits[:4], 2)  
    right = int(input_bits[4:], 2)  
    output = f"{s_box_table[left]:04b}{s_box_table[right]:04b}"
    print(f"S-блок: {input_bits} -> {output}")
    return output

@inverse_function
def inverse_s_box(output_bits):
    """Обратный S-блок"""
    left = int(output_bits[:4], 2)  
    right = int(output_bits[4:], 2)  
    output = f"{inverse_s_box_table[left]:04b}{inverse_s_box_table[right]:04b}"
    print(f"Обратный S-блок: {output_bits} -> {output}")
    return output

@inverse_function
def p_block(input_bits):
    """P-блок"""
    output = ''.join(input_bits[i-1] for i in p_indices)
    print(f"P-блок: {input_bits} -> {output}")
    return output

@inverse_function
def inverse_p_block(input_bits):
    """Обратный P-блок"""
    output = ''.join(input_bits[i-1] for i in inverse_p_indices)
    print(f"Обратный P-блок: {input_bits} -> {output}")
    return output

# Примеры использования функций
input_bits = '11001100'
s_output = s_box(input_bits)
inv_s_output = inverse_s_box(s_output)

p_output = p_block(s_output)
inv_p_output = inverse_p_block(p_output)


def xor(bits1, bits2):
    print(f"Выполняем побитовый XOR между {bits1} и {bits2}:")
    
    result = []
    for b1, b2 in zip(bits1, bits2):
        if b1 != b2:
            result.append('1')
            print(f"{b1} ⊕ {b2} = 1")  # Если биты разные, результат 1
        else:
            result.append('0')
            print(f"{b1} ⊕ {b2} = 0")  # Если биты одинаковые, результат 0

    result_str = ''.join(result)
    print(f"Итоговый результат XOR: {result_str}")
    return result_str


def decrypt(ciphertext):
    # Ключи шифрования
    k1 = '01010101'
    k2 = '11111111'
    k3 = '10101010'

    print(f"Шифртекст: {ciphertext}")

    # Третий цикл
    print("\nШаг 1: Применение третьего цикла")
    print(f"p(2) = c ⊕ k(3)")
    p2 = xor(ciphertext, k3)  # c ⊕ k(3)
    
    # Второй цикл
    print("\nШаг 2: Применение второго цикла")
    print(f"p(2) после P-блока: p(2) = P^(-1)(p(2))")
    p2_after_p = inverse_p_block(p2)  # Обратный P-блок
    print(f"p(1) после S-блока: p(1) = S^(-1)(p(2))")
    p1_after_s = inverse_s_box(p2_after_p)  # Обратный S-блок
    print(f"p(0) = p(1) ⊕ k(2)")
    p0 = xor(p1_after_s, k2)  # p(1) ⊕ k(2)

    # Первый цикл
    print("\nШаг 3: Применение первого цикла")
    print(f"plaintext = p(0) ⊕ k(1)")
    plaintext = xor(p0, k1)  # p(0) ⊕ k(1)

    return plaintext

# Пример использования
ciphertext = '00110000'
plaintext = decrypt(ciphertext)
print(f"\nОткрытый текст: {plaintext}")
