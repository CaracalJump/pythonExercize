# 1

with open("../socialwelfare_new/information.html", "r", encoding = "utf-8") as f:
    print(f.read())
    
# 2

answer = input("What color do you like?: ")

with open("answer.txt", "w", encoding = "utf-8") as f:
    f.write(answer)

with open("answer.txt", "r", encoding = "utf-8") as f:
    print(f.read())

# 3

import csv

lists = [
        ["Top Gun", "Risky Business", "Minority Report",],
        ["Titanic", "The Revenant", "Inception",],
        ["Training Day", "Man on Fire", "Flight"],
        ]

with open("lists.csv", "w", newline = '') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(lists[0])
    w.writerow(lists[1])
    w.writerow(lists[2])

with open("lists.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

# 4

listsJ = [
        ["トップガン", "リスキービジネス", "マイノリティーリポート",],
        ["タイタニック", "レヴェナント", "インセプション",],
        ["トレーニング・デイ", "マンオンファイア", "フライト"],
        ]

with open("listsJ.csv", "w", encoding="utf-8", newline = '') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(listsJ[0])
    w.writerow(listsJ[1])
    w.writerow(listsJ[2])

with open("listsJ.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
