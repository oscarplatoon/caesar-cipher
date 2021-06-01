def caesar_cipher(string, shift_amount):
    return_cipher = ''
    for letter in string:
        # maintain space characters 
        if not letter.isalpha():
            return_cipher += letter
        # encrypts uppercase characters without removing case
        elif letter.isupper():
            #convert letter to unicode, subtract base unicode to get place in alpha
            #A=65, A=95 A=30 A=4 A=69
            return_cipher += chr((ord(letter) + shift_amount - 65) % 26 + 65)
        elif letter.islower():
            # same but with lowercase
            return_cipher += chr((ord(letter) + shift_amount - 97) % 26 + 97)
    return(return_cipher)    
# caesar_cipher("Boy! What a string!", -5)
