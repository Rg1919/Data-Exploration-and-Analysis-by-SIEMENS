#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv(r'C:\Users\HP G5\Desktop\NEW PROJECTT.csv')

search_str = input('Enter the string to search for x axis: ')

matched = []
serial_num = 1

for col in file.columns:
    if search_str in col:
        matched.append((serial_num, col))
        serial_num += 1

for serial, column_name in matched:
    print(f'{serial}.{column_name}')

if not matched:
    print('The string does not match')
else:
    num = int(input('Enter the number to select: '))
    if 1 <= num <= len(matched):
        selected_column = matched[num - 1][1]
        print('Selected column: ', selected_column)
            
x = selected_column
y_count = int(input('Enter the number of Y-columns: '))

y_names = []
colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink'] 

for i in range(y_count):
    search_str2 = input('Enter the string to search for y axis: ')
    matched2 = []
    serial_num2 = 1

    for col in file.columns:
        if search_str2 in col:
            matched2.append((serial_num2, col))
            serial_num2 += 1

    for serial2, column_name2 in matched2:
        print(f'{serial2}.{column_name2}')

    if not matched2:
        print('The string does not match')
    else:
        num2 = int(input('Enter the number to select: '))
        if 1 <= num2 <= len(matched2):
            selected_column2 = matched2[num2 - 1][1]
            print('Selected column: ', selected_column2)

    y_names.append(selected_column2)


fig, ax = plt.subplots()

x_data = file[x]
y1_data = file[y_names[0]]
line1, = ax.plot(x_data, y1_data, label=y_names[0])

ax.set_xlabel(x,color ='r')
y1_label = ax.set_ylabel(y_names[0], color=colors[0])
ax.legend(loc='upper center')

x_min = min(x_data)
x_max = max(x_data)
interval = (x_max - x_min) / 2

plt.xticks(np.arange(x_min, x_max + 1, interval))

legends = [line1]

for i in range(1, len(y_names)):
    ax_new = ax.twinx()
    y_data = file[y_names[i]]
    line, = ax_new.plot(x_data, y_data, label=y_names[i], color=colors[i])
    ax_new.plot(x_data, y_data, label=y_names[i], color=colors[i])
    ax_new.set_ylabel(y_names[i], color=colors[i])
    ax_new.spines['right'].set_position(('outward', i * 50))
    #ax_new.legend(loc='upper right')
    legends.append(line)
    
ax.legend(legends, [line.get_label() for line in legends], loc='upper center')


plt.title('Multiple Y-Columns Plot')

plt.show()


# In[ ]:





# In[ ]:




