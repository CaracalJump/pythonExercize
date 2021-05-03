def div(n):
    print("-----{}-----".format(n))


# 1

div(1)

films = [
    "Walking Dead",
    "Entourage",
    "The Sopranos",
    "Vampire Diarys",
    ]

for i, new in enumerate(films):
    new = films[i]
    print(new)

# 2

div(2)

for i in range(25, 51):
    print(i)

# 3

div(3)

for i, new in enumerate(films):
    new = films[i]
    print("{}: {}".format(i, new))

# 4

div(4)

corrects = [1, 10, 100, 1000, 10000,]

while True:
    q = input("type a number, or q to quit: ")
    if q == "q":
        print("Game Over")
        break
    elif int(q) in corrects:
        print("BINGO!")
        break
    else:
        print("Boooo")
    
# 5

div(5)

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)

    






    
    
