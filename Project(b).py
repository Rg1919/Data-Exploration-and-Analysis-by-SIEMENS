#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read data from the imported file (update the file path accordingly)
df = pd.read_csv(r"C:\Users\HP G5\Desktop\IDS292B_20221007073000_tdy285.csv")

# Prompt the user to enter the search string for X-axis
search_string_x = input("Enter the search string for X-axis: ")
matching_columns_x = [col for col in df.columns if search_string_x in col]

if matching_columns_x:
    for i, col in enumerate(matching_columns_x, 1):
        print(f"{i}. {col}")

    if len(matching_columns_x) == 1:
        selected_column_x = matching_columns_x[0]
        print(f"Selected column for X-axis: {selected_column_x}")
    else:
        while True:
            try:
                selection_x = int(input("Enter the serial number of the column for X-axis: "))
                if selection_x >= 1 and selection_x <= len(matching_columns_x):
                    selected_column_x = matching_columns_x[selection_x - 1]
                    print(f"Selected column for X-axis: {selected_column_x}")
                    break
                else:
                    print("Invalid selection. Please enter a valid serial number.")
            except ValueError:
                print("Invalid input. Please enter a valid serial number.")
else:
    print("No matching columns found for X-axis.")

# Prompt the user to enter the search string and serial number for each Y-axis
y_columns = []
y_labels = []
colors = ['blue', 'green', 'red', 'purple', 'orange']
num_columns = int(input("Enter the number of Y-axis columns: "))

for i in range(num_columns):
    search_string_y = input(f"Enter the search string for Y-axis column {i+1}: ")
    matching_columns_y = [col for col in df.columns if search_string_y in col]

    if matching_columns_y:
        for j, col in enumerate(matching_columns_y, 1):
            print(f"{j}. {col}")

        if len(matching_columns_y) == 1:
            selected_column_y = matching_columns_y[0]
            print(f"Selected column for Y-axis column {i+1}: {selected_column_y}")
        else:
            while True:
                try:
                    selection_y = int(input(f"Enter the serial number of the column for Y-axis column {i+1}: "))
                    if selection_y >= 1 and selection_y <= len(matching_columns_y):
                        selected_column_y = matching_columns_y[selection_y - 1]
                        print(f"Selected column for Y-axis column {i+1}: {selected_column_y}")
                        break
                    else:
                        print("Invalid selection. Please enter a valid serial number.")
                except ValueError:
                    print("Invalid input. Please enter a valid serial number.")
    else:
        print(f"No matching columns found for Y-axis column {i+1}.")

    y_columns.append(selected_column_y)
    y_labels.append(f"Y-axis label {i+1}")

# Prompt the user to enter the range for the x-axis ["dd-mm-yyyy HH:MM"]
x_min = input("Enter the minimum value for the x-axis (dd-mm-yyyy HH:MM): ")
x_max = input("Enter the maximum value for the x-axis (dd-mm-yyyy HH:MM): ")

# Convert x-axis values to datetime objects with custom format
date_format = "%d-%m-%Y %H:%M"
df[selected_column_x] = pd.to_datetime(df[selected_column_x], format=date_format)

# Filter the dataframe based on the selected range of x-axis values
filtered_df = df[(df[selected_column_x] >= datetime.strptime(x_min, date_format)) &
                 (df[selected_column_x] <= datetime.strptime(x_max, date_format))]


# Create the figure and axes
fig, ax1 = plt.subplots()

# Plot y values with the corresponding y-axis
lines = []
line_labels = []
for i, y_column in enumerate(y_columns):
    if i == 0:
        line, = ax1.plot(filtered_df[selected_column_x], filtered_df[y_column], color=colors[i])
        line_labels.append(y_labels[i])
        lines.append(line)
        ax1.set_ylabel(y_labels[i], color=colors[i])
        ax1.tick_params(axis='y', labelcolor=colors[i])
    else:
        ax = ax1.twinx()
        line, = ax.plot(filtered_df[selected_column_x], filtered_df[y_column], color=colors[i])
        line_labels.append(y_labels[i])
        lines.append(line)
        ax.spines['right'].set_position(('outward', 60 + (i - 1) * 40))  # Adjust position of additional y-axes
        ax.set_ylabel(y_labels[i], color=colors[i])

# Set the limits of the x-axis
ax1.set_xlim(datetime.strptime(x_min, date_format), datetime.strptime(x_max, date_format))

# Set the x-ticks to the four equal partitions
x_ticks = pd.date_range(start=datetime.strptime(x_min, date_format), end=datetime.strptime(x_max, date_format), periods=5)
ax1.set_xticks(x_ticks)

# Rotate the x-axis tick labels by 90 degrees
ax1.set_xticklabels(x_ticks.strftime(date_format).tolist(), rotation=90)

# Adjust the spacing between subplots
fig.tight_layout()

# Set the y-axis labels for all subplots
if len(y_labels) > 0:
    plt.legend(lines, line_labels, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=len(y_labels))

# Set the title of the plot

plt.xlabel(selected_column_x)
plt.show()


# In[ ]:





# In[ ]:




