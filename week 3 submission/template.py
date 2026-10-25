"""
RECORD CHECK  -  my version
===========================

Name  : Chloe  Marie Amelia Allas
Lane  :  AI 
Date  :09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(percent):
    """Returns the status based on the percentage"""
    if percent>= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value,limit):
    """function that return the difference and percentage"""
    difference = limit - value
    percentage= (value/limit) * 100
    return difference , percentage

    

# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
count=0
while True:
    #ask user for input and convert strings to decimal for numbers
    label =input("enter a name: ")      # replace with an input() call
    limit = float(input("enter number: "))
    value = float(input("enter number: "))   # replace with an input() call, converted

    if label == "quit": #while loop stops if label is entered as quit
        break
    
# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.
    
    difference = limit - value   # replace with your code
    percent = (value/limit) * 100    # replace with your code
    status = status_of(percent)         # replace with your code

    if status == "OVER LIMIT":
        count += 1 # count updates by 1 when status is over limit

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    def print_report(label,value,limit,difference,percent,status):
        """print the report"""

        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {label}")
        print("=" * 34)
        # format to right align by 10 spaces and round decimal numbers to 2 dpp
        print(f"label       = {label:>10}")
        print(f"value       = {value:>10.2f}")
        print(f"limit       = {limit:>10.2f}")
        print(f"difference  = {difference:>10.2f}")
        print(f"percent     = {percent:>10.2f}")
        print(f"status      = {status:>10}")
        print("=" * 34)


    print_report(label, value, limit, difference, percent , status) # display the report

    print(f"{count} values were over limit") # display the count for over limit values

# your report lines go here




# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
