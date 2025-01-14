p_c = '00110100'
# '01010101', '11111111', '10101010'
keys = ['11111111', '01010101', '10101010']

# s_box = [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
# inverse_s_box = [14, 6, 12, 10, 5, 3, 15, 1, 0, 9, 4, 13, 7, 11, 2, 8]
# p_indices = [1, 8, 3, 5, 7, 4, 6, 2]
# inverse_p_indices = [8, 1, 5, 6, 4, 7, 2, 3]

# s_box = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
# inverse_s_box = [14, 3, 4, 8, 1, 12, 10, 15, 7, 13, 9, 5, 11, 2, 0, 6]  # Обратный S-блок
# p_indices = [1, 5, 2, 6, 3, 7, 4, 8]
# inverse_p_indices = [1, 3, 5, 7, 2, 6, 4, 8]  # Обратный P-блок

def s_box(input_bits):
    # Таблица S-блока
    s_box = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    left = int(input_bits[:4], 2)  # Левые 4 бита
    right = int(input_bits[4:], 2)  # Правые 4 бита
    # Применяем S-блок к левым и правым частям
    output = f"{s_box[left]:04b}{s_box[right]:04b}"
    print(f"S-блок: {input_bits} -> {output}")
    return output
def inverse_s_box(output_bits):
    # Обратная таблица S-блока
    inverse_s_box = [14, 3, 4, 8, 1, 12, 10, 15, 7, 13, 9, 5, 11, 2, 0, 6]
    left = int(output_bits[:4], 2)  # Левые 4 бита
    right = int(output_bits[4:], 2)  # Правые 4 бита
    # Применяем обратный S-блок к левым и правым частям
    output = f"{inverse_s_box[left]:04b}{inverse_s_box[right]:04b}"
    print(f"Обратный S-блок: {output_bits} -> {output}")
    return output
def p_block(input_bits):
    # P-блок
    p_indices = [1, 5, 2, 6, 3, 7, 4, 8] 
    output = ''.join(input_bits[i-1] for i in p_indices)
    print(f"P-блок: {input_bits} -> {output}")
    return output
def inverse_p_block(input_bits):
    # Обратный P-блок
    inverse_p_indices = [1, 3, 5, 7, 2, 6, 4, 8] 
    output = ''.join(input_bits[i-1] for i in inverse_p_indices)
    print(f"Обратный P-блок: {input_bits} -> {output}")
    return output
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
    k1 = keys[0]
    k2 = keys[1]
    k3 = keys[2]
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
ciphertext = p_c
plaintext = decrypt(ciphertext)
print(f"\nОткрытый текст: {plaintext}")
