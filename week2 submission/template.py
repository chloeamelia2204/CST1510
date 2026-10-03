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

count=0
while True:
    
    label = input("enter a hostname: ")      # replace with an input() call
    value = float(input("enter fisrt number: "))     # replace with an input() call, converted with float()
    limit = float(input("enter second number: "))     # replace with an input() call, converted with float()
    

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit-value  # replace with your calculation
    percent = (value/limit) * 100      # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"


    if percent > 100:
        status = "OVER LIMIT"   # replace with your if / else (or if / elif / else)
    else :
        status = "OK"
    print(status)

    if status == "OVER LIMIT":
        count += 1
    if label == "quit":
                break

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
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

# your report lines go here

    print("=" * 34)
    print(f"{'label':>5}      = {label:>15}")
    print(f"{'value':>5}      = {value:>15.2f}")
    print(f"{'limit':>5}      = {limit:>15.2f}")
    print(f"{'difference':>5} = {difference:>15.2f}")
    print(f"{'percent':>5}    = {percent:>15.2f}%")
    print("=" * 34)

    
    print(f"There were {count} percentage(s) that were over limit")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds

"""
The error is in the percentage calculation when dividing by zero we get a division by zero error
"""