# Ejemplo de uso


from core.playfair import PlayfairCipher


def load_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    ascii_content = content.encode('latin1', 'replace').decode('latin1')
    return ascii_content

def load_cipher(filename):
    with open(filename, 'r', encoding='latin1') as file:
        content = file.read()
    return content

def decrypt_text():
    print('Has elegido la opcion de descifrar mensajes')
    print('<-------------------------------------->')
    print('Por favor, ingrese los siguientes datos:')
    print('desea cargar un archivo con el mensaje a descifrar? (y/n): ')
    option = input('> ').strip().lower()
    if option == 'y':
        encrypted_text = load_cipher('data/cipher.txt')
        print('Mensaje a descifrar => {}'.format(encrypted_text))
    else:
        print('Inserte el mensaje a descifrar: ')
        encrypted_text = input('> ').strip().upper()
    key = input('Inserte la clave utilizada para cifrar: ').strip().upper()
    cipher = PlayfairCipher(key)
    mssg = cipher.decrypt(encrypted_text)
    with open('data/decrypt.txt', 'w', encoding='latin1') as file:
        file.write(mssg)
    print('El mensaje cifrado ha sido guardado en data/cipher.txt')
    print('<-------------------------------------->')
    print(f'Texto descifrado:')
    print('{}'.format(mssg))

def cipher_text():
    print('Has elegido la opcion de cifrar mensajes')
    print('<-------------------------------------->')
    print('Por favor, ingrese los siguientes datos:')
    print('desea cargar un archivo con el mensaje a cifrar? (y/n): ')
    option = input('> ').strip().lower()
    if option == 'y':
        textPlain = load_txt('data/plain.txt').strip().upper()
        print('Mensaje a cifrar => {}'.format(textPlain))
    else:
        textPlain = input('Inserte el mensaje a encriptar: ').strip().upper()
    key = input('Inserte la clave: ').strip().upper()
    cipher = PlayfairCipher(key)
    c = cipher.encrypt(textPlain)
    print('<-------------------------------------->')
    print('Texto cifrado:')
    print('{}'.format(c))
    
    # Guardar el texto cifrado en un archivo
    with open('data/cipher.txt', 'w', encoding='latin1') as file:
        file.write(c)
    print('El mensaje cifrado ha sido guardado en data/cipher.txt')

def playfair_CLI():
    print('1. Cifrar texto')
    print('2. Descifrar texto')
    print('Seleccione una opción: ')
    option = input('> ')
    if option == '1':
        cipher_text()
    elif option == '2':
        decrypt_text()
    else:
        print('Opción no válida')