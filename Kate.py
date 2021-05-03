import statistics

list = []

def sumup():
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    for m in range(1, 7):
                        result = i + j + k + l + m
                        list.append(result)

sumup()
print(statistics.mode(list))
for i in range(5, 31):
    print(list.count(i))
    
