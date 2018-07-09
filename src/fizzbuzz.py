# FizzBuzz code

result = ""

for i in range(1, 100):
    if i % 3 == 0:
        result += "fizz"
    if i % 5 == 0:
        result += "buzz"
    if (i % 5 != 0) & (i % 3 != 0):
        result += str(i)
    result += ", "

print(result)
