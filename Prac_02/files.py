# File 1

output_file = open('name.txt', 'w')
name = str(input("What is your name?"))
print(name, file=output_file)
output_file.close()

# File 2

in_file = open("name.txt", "r")
print("Your name is", in_file.read())

# File 3

total = 0
in_file2 = open("numbers.txt", "r")
for line in range(2):
    total = total + int(in_file2.readline())
in_file2.close()
print(total)

# File 4

in_file3 = open("numbers2.txt", "r")
total = 0
for line_str in in_file3:
    total = total + int(line_str)
print(total)
