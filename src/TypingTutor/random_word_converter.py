with open("random_words.txt", 'r') as f:
    line = f.readlines()

for n, i in enumerate(line):
    line[n] = i[:-1]
    if n == 999:
        line[n] = i

print(line)