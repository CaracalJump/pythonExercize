# 1

def nijou():
    n = int(input("Type a number: "))
    print(n ** 2)

nijou()

# 2

def print_str(moji):
    print(moji)

print_str("mojiretsu")

# 3

def sumsup(a, b, c, d = 19, e = 12):
    return a + b + c + d + e

print(sumsup(8, 9, 10, 11))

# 4

def div2(n):
    return n // 2

def mul4(n):
    return n * 4

result = div2(18)
mul4(result)

# 5

def toFloat(n):
    try:
        print(float(n))
    except ValueError:
        print("Invalid input.")

toFloat(12)
toFloat("Hello")
