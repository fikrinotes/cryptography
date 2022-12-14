from tkinter import *
import numpy as np

def encryption() :
    plaintext = str(entry1.get()).lower()
    kata = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    key_matrix = np.array([[5, 3], [3, 2]])
    # menentukan determinan matriks kunci
    determinant = round(np.linalg.det(key_matrix))
    # menentukan faktor reciprocal/kebalikan dari matriks kunci
    for i in range(1,26) :
        if ((determinant*i)%26==1) :
            reciprocal = i
            break

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
    text.set(encrypted_text)


def btn_clicked():
    encryption()


window = Tk()

text = StringVar()
text.set('')

window.title("Hill Cipher App - An App By Fikri Mulyana Setiawan")
window.geometry("804x386")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 386,
    width = 804,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    608.0, 312.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0, textvariable=text)

entry0.place(
    x = 474.0, y = 266,
    width = 268.0,
    height = 90)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    348.0, 193.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 549, y = 177,
    width = 118,
    height = 32)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    608.0, 138.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 474.0, y = 122,
    width = 268.0,
    height = 30)

window.resizable(False, False)
window.mainloop()
