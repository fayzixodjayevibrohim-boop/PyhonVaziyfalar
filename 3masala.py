import os
os.system("cls")

son1= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
son2= [son[:-1] + (100,) for son in son1]
print(son2)
