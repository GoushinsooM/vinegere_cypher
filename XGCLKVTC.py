def create_vigenere_table():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = [[0 for _ in range(26)] for _ in range(26)]
    
    for row in range(26):
        for col in range(26):
            vigenere_table[row][col] = alphabet[(row + col) % 26]
    
    return vigenere_table

def vigenere_cipher(text, key, mode='encrypt'):
    vigenere_table = create_vigenere_table()
    result = []
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            row = ord(key[i % key_length]) - ord('A')
            col = ord(char) - ord('A')
            
            if mode == 'decrypt':
                decrypted_char = vigenere_table[row].index(char)
                result.append(chr(decrypted_char + ord('A')))
            else:
                result.append(vigenere_table[row][col])
        else:
            result.append(char)
    
    return ''.join(result)

plaintext = input('Digite sua mensagem: ').upper()
key = input('Digite sua chave: ').upper()
encrypted_text = vigenere_cipher(plaintext, key, mode='encrypt')
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
