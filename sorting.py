import numpy as np
import pandas as pd

with open("tf_idf_word.txt", "r") as f:
    d = eval(f.read())

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []

for k, v in d.items():
  l1.append((k, v[0]))
  l2.append((k, v[1]))
  l3.append((k, v[2]))
  l4.append((k, v[3]))
  l5.append((k, v[4]))
  l6.append((k, v[5]))

l1.sort(key=lambda x: x[1], reverse=True)
l2.sort(key=lambda x: x[1], reverse=True)
l3.sort(key=lambda x: x[1], reverse=True)
l4.sort(key=lambda x: x[1], reverse=True)
l5.sort(key=lambda x: x[1], reverse=True)
l6.sort(key=lambda x: x[1], reverse=True)

n1 = l1[:50]
n2 = l2[:50]
n3 = l3[:50]
n4 = l4[:50]
n5 = l5[:50]
n6 = l6[:50]

myarray1 = np.array(n1)
myarray2 = np.array(n2)
myarray3 = np.array(n3)
myarray4 = np.array(n4)
myarray5 = np.array(n5)
myarray6 = np.array(n6)

mydf1 = pd.DataFrame(myarray1, columns=['کلمه', 'مقدار'])
mydf2 = pd.DataFrame(myarray2, columns=['کلمه', 'مقدار'])
mydf3 = pd.DataFrame(myarray3, columns=['کلمه', 'مقدار'])
mydf4 = pd.DataFrame(myarray4, columns=['کلمه', 'مقدار'])
mydf5 = pd.DataFrame(myarray5, columns=['کلمه', 'مقدار'])
mydf6 = pd.DataFrame(myarray6, columns=['کلمه', 'مقدار'])

mydf1.to_excel('output1.xlsx', sheet_name='نتایج', index=False)
mydf2.to_excel('output2.xlsx', sheet_name='نتایج', index=False)
mydf3.to_excel('output3.xlsx', sheet_name='نتایج', index=False)
mydf4.to_excel('output4.xlsx', sheet_name='نتایج', index=False)
mydf5.to_excel('output5.xlsx', sheet_name='نتایج', index=False)
mydf6.to_excel('output6.xlsx', sheet_name='نتایج', index=False)