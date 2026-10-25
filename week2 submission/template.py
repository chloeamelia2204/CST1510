"""
RECORD CHECK  -  my version
===========================

Name  :Chloe Allas
Lane  :  AI 
Date  :02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

count=0 #set count at 0
while True: # while loop that stops if label is quit
    #Ask user 3 inputs and convert to float where there are numbers
    label = input("enter a hostname: ")      # replace with an input() call
    value = float(input("enter fisrt number: "))     # replace with an input() call, converted with float()
    limit = float(input("enter second number: "))     # replace with an input() call, converted with float()
#input always give string
   

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit-value  # store the difference between limit and value in a variable
    percent = (value/limit) * 100  # store the percentage into a varibale called percent

# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"


    if percent > 100: #describing condition for percent to be overlimit
        status = "OVER LIMIT"   # status stores over limit
    else : # if condition is false, this runs
        status = "OK" # status stores ok
    print(status)

    if status == "OVER LIMIT":
        count += 1 # count increases by 1 if status is over limit
    if label == "quit": # program stops running if label  is quit
                break # stops the program 

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34) # report border of 34 '='
    print(f"  RECORD CHECK  -  {label}") # the report title
    print("=" * 34) # report border of 34 '='

# your report lines go here

    print("=" * 34) #opens another border to enclose the data
    print(f"{'label':>5}      = {label:>15}") # f string format the data by right aligning by 15 spaces
    print(f"{'value':>5}      = {value:>15.2f}") # value is right aligned and rounded to 2 decimal  places
    print(f"{'limit':>5}      = {limit:>15.2f}")  # limit is right aligned and rounded to 2 decimal  places
    print(f"{'difference':>5} = {difference:>15.2f}")# difference is right aligned and rounded to 2 decimal  places
    print(f"{'percent':>5}    = {percent:>15.2f}%") # percent is right aligned and rounded to 2 decimal  places
    print("=" * 34)

    
    print(f"There were {count} percentage(s) that were over limit") # prints the number of values that are over limit 

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds

"""
The error is in the percentage calculation when dividing by zero we get a division by zero error
"""