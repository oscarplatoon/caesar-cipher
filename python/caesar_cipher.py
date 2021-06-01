def caesar_cipher(string, shift_amount):


	list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	answer = ""

	key = list_lower + list_upper

	for x in range(shift_amount % 26):
		hold = list_lower.pop(0)
		list_lower.append(hold)
		hold = list_upper.pop(0)
		list_upper.append(hold)

	key_out = list_lower + list_upper

	for y in string:
		if y.isalpha():
			answer += key_out[key.index(y)]
		else:
			answer += y

	return answer