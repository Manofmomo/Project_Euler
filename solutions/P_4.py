# 999x999
# 100x100
# 999x999
def is_palindrome(num):
    """Returns True or False on the basis of if the given number is a palindrome"""
    string = str(num)
    return string == string[::-1]

print("Hello hagda ")
nums = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(i*j):
            nums.append(i*j)
print(max(nums))
