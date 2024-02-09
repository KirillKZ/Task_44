#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
def oneHot():
  lst = ['robot'] * 10
  lst += ['human'] * 10
  random.shuffle(lst)

  st = set(lst)
  st = list(st)
  col = []
  tbl = []
  data = {}

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
