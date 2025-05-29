import random
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'x', 'z', 'A', 'B', 'C', 'D', 'E', 'F', '6', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S',
          'w', 'X','Y','Z']
numbers = ['0', '1', '2', '3', '4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*','+']
print("Welcome to Password Generator!")
n_letters=int(input("How many letters you want in your password?\n")) #4
n_symbols=int(input("How many symbols you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))
password_list=[]
for i in range(1,n_letters+1): 
	char = random.choice(letters)
	password_list += char
for i in range(1,n_symbols+1):
	char = random.choice(symbols)
	password_list+= char
for i in range(1,n_numbers+1):
	char=random.choice(symbols)
	password_list+= char
print(password_list) #['Y', 'r', 'v', 'u', '$', '%', '&', '8', '3']
random.shuffle(password_list)
print(password_list) #['8, '3', '&', 'u', '$', 'r','y','%','v']
password=""
for char in password_list:
	password += char
print(password)
