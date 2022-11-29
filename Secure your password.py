from tkinter import messagebox, simpledialog, Tk

def is_even(num):
    return num % 2 == 0

def get_even_letters(message):
    even_letters = []
    for count in range(0, len(message)):
        if is_even(count):
            even_letters.append(message[count])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for count in range(0, len(message)):
        if not is_even(count):
            odd_letters.append(message[count])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def get_event():
    event = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return event

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
while True:
    event = get_event()
    if event == 'encrypt':
        message = get_message()
        encrypt = swap_letters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypt)
        
    elif event == 'decrypt':
        message = get_message()
        decrypt = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypt)
    else:
        break
root.mainloop()