
def encrypt(plain_text, key):
    """
    plain text will be the un-encrypted text
    key will be the shift number
    encrypt('12345', 2)
    plain_text: 12345
    shift: 2
    --> 34567
    """
    encrypted_text = ''
    print(f'The plain text data is {plain_text}.')
    for char in plain_text:
        num = int(char)
        shifted_number = num + key
        # do something to account for > 10
        shifted_number = (num + key) % 10
        # if shifted_number > 9:
        #     shifted_number -= 10
        encrypted_text += str(shifted_number)
    print(f'The encrypted data with a shift of {key} is {encrypted_text}.')
    print('#'*50)   
    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)

if __name__ == "__main__":
    # assert encrypt('12345', 1) == '23456'
    # assert encrypt('12345', 2) == '34567'
    # assert encrypt('12345', 12) == '34567'
    # assert encrypt('12345', 21) == '23456'
    # assert encrypt('12345', 356) == '78901'
    # assert encrypt('23456', -1) == '12345'

 
    key = 5
    plain = '12345'

    encypted = encrypt(plain, key)
    print (encypted)
    # return --> 67890
    decrypted = decrypt(encypted, key)
    print(decrypted)
    # return --> 12345

    assert decrypted == plain