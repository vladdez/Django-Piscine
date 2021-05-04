def read_numbers():
	with open("numbers.txt", "r") as file:
		numbers = file.read().split(',')
		for i in numbers:
			print(i.strip())

if __name__ == '__main__':
    read_numbers()