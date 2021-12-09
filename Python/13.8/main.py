amount =int(input("Введите количество билетов:"))
print("Для детей меньше 18 - бесплатно\n Для лиц от 18 до 25 - 990\n Для людей старше - 1390")
years=[]
summ=0
for i in range(amount):
    years.append(int(input("Введите возраст посетителя:")))
for i in range(0, len(years)):
    if years[i] > 18:
        if years[i] < 25:
            summ+=990
        else:
            summ+=1390
if amount>3:
    summ=summ*0.9
print("Вы купили ",amount," билетов. C вас ", summ)