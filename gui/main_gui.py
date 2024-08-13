import tkinter as tk
from tkinter import messagebox
from core.playfair import PlayfairCipher

def load_txt(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        ascii_content = content.encode('latin1', 'replace').decode('latin1')
        return ascii_content
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo de texto: {e}")
        return None

def load_cipher(filename):
    try:
        with open(filename, 'r', encoding='latin1') as file:
            content = file.read()
        return content
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo cifrado: {e}")
        return None

def save_result(filename, content):
    try:
        with open(filename, 'w', encoding='latin1') as file:
            file.write(content)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

def execute_action():
    try:
        key = key_entry.get().strip().upper()
        cipher = PlayfairCipher(key)
        
        if load_file_var.get() == 1:
            if action_var.get() == "cipher":
                text_plain = load_txt('data/plain.txt')
                if text_plain is None:
                    return
                text_plain = text_plain.strip().upper()
                result = cipher.encrypt(text_plain)
                save_result('data/cipher.txt', result)
            else:
                cipher_txt = load_cipher('data/cipher.txt')
                if cipher_txt is None:
                    return
                result = cipher.decrypt(cipher_txt.strip().upper())
                save_result('data/decrypt.txt', result)
        else:
            if action_var.get() == "cipher":
                text_plain = text_entry.get().strip().upper()
                result = cipher.encrypt(text_plain)
                save_result('data/cipher.txt', result)
            else:
                cipher_txt = text_entry.get().strip().upper()
                result = cipher.decrypt(cipher_txt)
                save_result('data/decrypt.txt', result)
        
        messagebox.showinfo("Resultado", result)
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar la acción: {e}")

def toggle_text_entry():
    if load_file_var.get() == 1:
        text_entry.config(state=tk.DISABLED)
    else:
        text_entry.config(state=tk.NORMAL)

def mainGui():
    global key_entry, action_var, load_file_var, text_entry

    root = tk.Tk()
    root.title("Playfair Cipher GUI")

    tk.Label(root, text="Clave:").pack()
    key_entry = tk.Entry(root)
    key_entry.pack()

    action_var = tk.StringVar(value="cipher")
    load_file_var = tk.IntVar()

    tk.Label(root, text="Acción:").pack()
    tk.Radiobutton(root, text="Cifrar", variable=action_var, value="cipher").pack()
    tk.Radiobutton(root, text="Descifrar", variable=action_var, value="decrypt").pack()

    tk.Checkbutton(root, text="Cargar texto desde archivo", variable=load_file_var, command=toggle_text_entry).pack()

    tk.Label(root, text="Texto:").pack()
    text_entry = tk.Entry(root)
    text_entry.pack()

    tk.Button(root, text="Ejecutar", command=execute_action).pack()

    root.mainloop()

if __name__ == "__main__":
    mainGui()