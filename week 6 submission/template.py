"""
RECORD CHECK  -  my version
===========================

Name  : Allas Chloe Marie Amelia
Lane  :  AI 
Date  : 30/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

# open and read a csv file called myowncsv
df = pd.read_csv("myowncsv.csv")   # replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
df["percent"] = ((df["value"] / df["limit"]) * 100).round(1) #calculate and create new column percent and round to 1dp
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK") #add new column status using inline small function lambda that gives conditions for percent to have different status categories


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)
print()
print(df[df["status"] != "OK"]) #only prints the rows with status: "OK"
print()
grouped = df.groupby("status")# groups the different status categories together
status_count = grouped["status"].count() # counts the number of rows in each category
print(status_count)
df.to_csv("newcsv.csv") #saves the column and rows of df to a new csv file

import matplotlib.pyplot as plt
plt.bar(status_count.index, status_count.values) #plots a bar chart using the labels and values from the status count
plt.savefig("status_count.png") # saves the bar chart
plt.show() #displays the bar chart


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
