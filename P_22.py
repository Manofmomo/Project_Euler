in_file = open("p022_names.txt")
lines=in_file.read().split(",")
in_file.close()
line_no=int(1)
score=int(0)
sum=int(0)
lines.sort()
for line in lines:
    sum=int(0)
    print(line[1:-1])
    for char in line[1:-1]:
        sum += ord(char)-64
    score+= sum*line_no
    line_no += 1
print(score)
print(ord("A")-64)
