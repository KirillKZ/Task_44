#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
transformed = ohe.fit_transform(data[['whoAmI']])
data[ohe.categories_[0]] = transformed.toarray()  
data.drop('whoAmI', axis= 1 , inplace= True )
print(data)

##Еще один вариант
import random
st = set(lst)
strn = ""
print(f'       {st}')
for i in range(len(lst)):
    for k in st:
        if k == lst[i]:
            strn += "1      "
        else: strn += "0      "
    print(f'{i} {lst[i]}    {strn}')
    strn = ""
