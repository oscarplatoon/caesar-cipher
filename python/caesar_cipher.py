def caesar_cipher(string, num):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  new_word = ""

  for i in string:
    if i in alphabet:
      if alphabet.index(i) + num >= 0:
        new_word += alphabet[(alphabet.index(i) + num) % 26]
      else:
        new_word += alphabet[26 + (alphabet.index(i) + num)]

    elif i in caps:
      if caps.index(i) + num >= 0:
        new_word += caps[(caps.index(i) + num) % 26]
      else:
        new_word += caps[26 + (caps.index(i) + num)] 

    else:
      new_word += i

  return new_word

# print(caesar_cipher("hello", 3))