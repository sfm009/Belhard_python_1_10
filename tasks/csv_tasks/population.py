"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import csv
change_perc = []
years = []


def max_delta():

    with open('world_population.csv', 'r') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            change_perc.append(float(row[2]))  # составляем список из значений по приросту населения
            years.append(int(row[0]))  # составляем список с годами
        max_change = max(change_perc)  # находим максимальное значение по приросту населения
        for i in range(len(change_perc)):
            if change_perc[i] == max_change:
                print(years[i])  # выводим значения тех годов, в которых прирост населения был максимальным


max_delta()



