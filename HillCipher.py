import numpy as np
def encryption() :
    plaintext = input("masukkan kata untuk dienkripsi : ").lower()

    # definisi matriks kunci untuk enkripsi
    if len(plaintext)%2!=0:
        plaintext += plaintext[-1]
    v = [0,0]
    i = 0
    encrypted_text = ""
    while i+1 <= len(plaintext) :
        if i%2!=0 :
            v = np.array([kata.index(plaintext[i-1]), kata.index(plaintext[i])])
            result = np.matmul(key_matrix, v)
            result = result%26
            encrypted_text = encrypted_text + kata[result[0]] + kata[result[1]]
        i += 1
    print("hasil enkripsi : {}".format(encrypted_text))

def decryption() :
    encrypted_text = input("masukkan kata yang ingin didekripsi : ").lower()
    plaintext = ""
    if len(plaintext)%2!=0:
        plaintext += plaintext[-1]
    v = [0,0]
    i = 0

    while i+1 <= len(encrypted_text) :
            if i%2!=0 :
                v = np.array([kata.index(encrypted_text[i-1]), kata.index(encrypted_text[i])])
                result = np.matmul(decrypting_key, v)
                result = result%26
                plaintext = plaintext + kata[result[0]] + kata[result[1]]
            i += 1
    print("plain text : " + plaintext)

def num_encryption() :
    text_input = input("masukkan angka untuk dienkripsi : ")
    plaintext = str(text_input)
    # definisi matriks kunci untuk enkripsi
    if len(plaintext)%2!=0:
        plaintext += plaintext[-1]
    v = [0,0]
    i = 0
    encrypted_text = ""
    while i+1 <= len(plaintext) :
        if i%2!=0 :
            v = np.array([int(plaintext[i-1]), int(plaintext[i])])
            result = np.matmul(key_matrix, v)
            result = result%10
            encrypted_text = encrypted_text + str(result[0]) + str(result[1])
        i += 1
    print("hasil enkripsi : {}".format(encrypted_text))




# opsi untuk memilih antara enkripsi atau dekripsi
ulang = 'y'
while ulang == 'y' :
    kata = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    key_matrix = np.array([[5, 3], [3, 2]])
    # menentukan determinan matriks kunci
    determinant = round(np.linalg.det(key_matrix))
    # menentukan faktor reciprocal/kebalikan dari matriks kunci
    for i in range(1,26) :
        if ((determinant*i)%26==1) :
                reciprocal = i
                break
    # kunci untuk mendekripsi ciphertext (tapi belum berhasil)
    decrypting_key = np.around(reciprocal*determinant*np.linalg.inv(key_matrix))
    decrypting_key = decrypting_key%26
    decrypting_key = decrypting_key.astype(int)

    option = input("(1) enkripsi atau (2) dekripsi ? ")
    if int(option) == 1 :
        text_or_num = int(input("text atau angka ? (1 = text, 2 = angka) "))
        if text_or_num == 1 :
            encryption()
        else :
            num_encryption()
    elif int(option) == 2 :
        decryption()
    ulang = input('ulangi ? (y/n)').lower()
