a=str(input('Введите фамилию учёного '))
#Просим ввести пользователя фамилию ученого. Это будет переменная а.
ph=('Эйнштейн','Тесла','Ньютон','Хокинг','Кюри-Склодовская','Рентген')
#Создаём кортеж,в котором будут фамилии только физиков.
math=('Аристотель','Абель','Архимед','Бернулли')
#Создаём кортеж,в котором будут фамилии только математиков.
bio=('Дарвин','Броун','Везе','Кребс','Павлов')
#Создаём кортеж,в котором будут фамилии только биологов.
if a in ph:
    print('Физик')
if a in math:
    print('Математик')
if a in bio:
    print('Биолог')
if a not in ph and a not in math and a not in bio:
    print('Программа не знает такого человека ')
"""Проверяем наличие фамилии в каждом кортеже и при её содержании выводим (print)
профессиональную принадлежность, либо ,что программа не знает такого человека."""