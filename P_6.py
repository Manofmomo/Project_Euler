squares = []
nums = []
for i in range(101):
    squares.append(i ** 2)
    nums.append(i)
sum_of_squares = sum(squares)
square_of_sums = sum(nums) ** 2
difference = square_of_sums - sum_of_squares
print(difference)
