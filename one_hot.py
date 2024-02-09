#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
#Метод для создания списка и создания словаря, который может представлен в виде One_Hot 
def oneHot():
  lst = ['robot'] * 10
  lst += ['human'] * 10
  random.shuffle(lst)

  st = set(lst) #набор со списком уникальных значений
  st = list(st) #Списко с тем же набором уникальных значения
  col = [] #Список для значений столбца
  tbl = [] #Список для значения списков со значениями столбцов
  data = {} #Словарь для хранения заголовка столбца и его названия

  for k in st:
      for i in lst:
          if k == i:
            col.append(1)
          else: col.append(0)

      tbl.append(col)
      col = [] 
  for i in range(len(st)):
    data[st[i]] = tbl[i]
  return data

df = pd.DataFrame(oneHot())
df
