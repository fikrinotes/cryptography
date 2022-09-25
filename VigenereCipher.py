import os

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# use the value to convert number to char, and use it's index to convert char to number
def decrypt(x) :
    return char[x]
def encrypt(x) :
    return char.index(x)

os.system('cls')

print('<<< ONE TIME PAD ENCRYPTION >>>\n')
msg1 = input('masukkan kata yang ingin dienkripsi : ').lower()
pw1 = input('masukkan password : ').lower()

l_pw1 = len(pw1)
l_msg1 = len(msg1)

while l_msg1 < l_pw1 :
    os.system('cls')
    print('\npassword tidak boleh lebih panjang dari kata yang ingin anda enkripsi-kan. silakan ulangi :\n')
    msg1 = input('masukkan kata yang ingin dienkripsi : ').lower()
    pw1 = input('masukkan password : ').lower()
    l_pw1 = len(pw1)
    l_msg1 = len(msg1)


def convert(msg, pw, l_msg, l_pw) :
    result = ''
    for i in range(0, l_msg) :
        key = i % l_pw
        if msg[i] in char :
            final = encrypt(msg[i]) + encrypt(pw[key]) + 1
            if final>25 :
                final = final%25-1
            result = result + decrypt(final)
        else :
            result = result + msg[i];
    return result


def translate(msg, pw, l_msg, l_pw) :
    result = ''
    for i in range(0, l_msg) :
        key = i % l_pw
        if msg[i] in char :
            final = encrypt(msg[i]) - (encrypt(pw[key]) + 1)
            if final<0 :
                final = 25-(-1*final)%25+1
            result = result + decrypt(final)
        else :
            result = result + msg[i];
    return result

print('hasil enkripsi : ' + convert(msg1, pw1, l_msg1, l_pw1))
#encrypted = convert(msg1, pw1, l_msg1, l_pw1)
#print('teks asli : ' + translate(encrypted, pw1, l_msg1, l_pw1))
