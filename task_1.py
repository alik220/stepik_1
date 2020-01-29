import numpy as np
import pandas as pd

our_students = pd.read_csv('C://Users//HP//Downloads//StudentsPerformance.csv')
#our_students.groupby('gender').aggregate ({'writing score' : mean'})

#обращаемся по столбцам integerLocation
our_students_new = our_students.iloc[[0, 3, 4, 7, 8]]

#даем название каждой строке - индексы (по умолчанию - нумерация от 0)
our_students_new.index = ["Cercai", "Tywin", "Greog", "Jeff", "Ilin"]

#обращаемся по индексам к строкам
our_students_new.loc[['Jeff', 'Ilin'], ['gender']]

#создаем серию из цифр с индексами
my_ser1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
my_ser2 = pd.Series([4, 5, 6], index=["a", "b", "c"])

#создаем датафрейм с 2 сериями
pd.DataFrame({'col_name_1':my_ser1, 'col_name_2':my_ser2})
