import string

def encrypt(text:str, rot:int, abc:str) -> str:
	"""
	Encrypt the text

	Args:
		text (int): input
		rot (int): rotations
		abc (str): abc

	Returns:
		str: returns encrypted text
	"""
	temp = ""
	for i in text:
		if i in abc:
			pos = abc.index(i)
			temp += abc[(pos+rot)%26]
		else:
			temp += i
	return temp

def decrypt(text:str, rot:int, abc:str) -> str:
	"""
	Decrypt the text

	Args:
		text (int): input
		rot (int): rotations
		abc (str): abc

	Returns:
		str: returns decrypted text
	"""
	temp = ""
	for i in text:
		if i in abc:
			pos = abc.find(i)
			temp += abc[(pos-rot)%26]
		else:
			temp += i
	return temp

def main(text:str, rot:int, inp:int) -> str:
	"""
	encrypt/decrypt with caesar (main)

	Args:
		text (_type_, optional): Input from user.
		rot (_type_, optional): rotation (by how many places it shifts).

	Returns:
		str: returns encrypted/decrypted text or another string
	"""

	text = text.upper()
	abc = string.ascii_uppercase

	if inp == "1":
		output = encrypt(text, rot, abc)

	elif inp == "2":
		output = decrypt(text, rot, abc)

	else:

		return "You have to choose something"
	
	return output

		
loop = True
while loop:
	inp = input("[1] Encrypt [2] Decrypt\n\n")
	text = input("\nText: ")
	try:
		rot = int(input("Rotation: "))
	except ValueError:
		print("Make sure to use a number at the rotation")
	else:
		loop = False

print(f"Output: {main(text, rot, inp)}")
