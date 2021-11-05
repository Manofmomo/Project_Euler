in_file = open('p067_triangle.txt')
lines = in_file.read().splitlines()
in_file.close()

BIG_LIST = []

for line in lines:
    BIG_LIST.append(line.split())

for i in range(len(BIG_LIST)-2, -1, -1):
    for j in range(0, len(BIG_LIST[i])):
        BIG_LIST[i][j] = int(BIG_LIST[i][j]) + int(max(BIG_LIST[i+1][j], BIG_LIST[i+1][j+1]))

print(BIG_LIST[0])
