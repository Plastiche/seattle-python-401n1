
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

    for char in plain_text:
        num = int(char)
        shifted_number = num + key
        # do something to account for > 10
        shifted_number = (num + key) % 10
        # if shifted_number > 9:
        #     shifted_number -= 10
        encrypted_text += str(shifted_number)
    print(encrypted_text)    
    return encrypted_text


if __name__ == "__main__":
    assert encrypt('12345', 2) == '34567'
    assert encrypt('12345', 12) == '34567'
    assert encrypt('12345', 21) == '23456'
    assert encrypt('12345', 356) == '78901'