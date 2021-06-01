def caesar_cipher(string, shift_amount=0):
   result = ""
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   ALPHABET = alphabet.upper()
   for letter in string:
       if(letter.islower()):
           #Move "letter" "shift_amount" times
           pos = alphabet.find(letter)
           pos += shift_amount
           while pos < 0:
               pos += 26
           while pos > 25:
               pos -= 26
           letter = alphabet[pos]
       elif(letter.isupper()):
           #Move "letter" "shift_amount" times
           pos = ALPHABET.find(letter)
           pos += shift_amount
           while pos < 0:
               pos += 26
           while pos > 25:
               pos -= 26
           letter = ALPHABET[pos]
       result += letter

   return result
       
