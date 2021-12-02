money =float(input("Введите ваши деньги:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [money*per_cent['ТКБ'],money*per_cent['СКБ'],money*per_cent['ВТБ'],money*per_cent['СБЕР']]
print("Максимальная сумма, которую вы можете заработать — ",max(deposit))