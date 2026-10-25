"""
RECORD CHECK  -  my version
===========================

Name  : Allas Chloé Marie Amélia
Lane  :  AI 
Date  :28/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.
#asking the user for inputs and converting first and second number to float
label =input( "Enter your name: ")      # : replace with an input() call
first = float(input("please enter a number: "))   # : replace with an input() call, converted
second = float(input("please enter a number: "))   # : replace with an input() call, converted
#inputs always give strings

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference =  first-second   # calculate the difference between first and second and store the calculation in difference
percent = (first/second) * 100      # calculate the first as a percentage of the second and store the calculation in percent

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print() # add a blank line in the output
print("=" * 34) #prints a line of 34 equal signs(the top border)
print(f"  RECORD CHECK  -  {label}") #prints the record check and its label as title
print(f"  name           = {label:>10}") # prints the label and right align by 10 spaces
print(f"  first number   = {first:>10.2f}") # prints the first number and right align it by 10 spaces and round it to 2 decimal places
print(f"  second number  = {second:>10.2f}") # prints the second number and right align it by 10 spaces and round it to 2 decimal places
print() # add a blank line in the output
print(f"  The difference = {difference:>10.2f}") # prints the difference and right align it by 10 spaces and round it to 2 decimal places
print(f"  The percentage = {percent:>+10.2f}%") # prints the percentage and right align it by 10 spaces and round it to 2 decimal places
print("=" * 34) #prints a line of 34 equal signs(the bottom border)

# : your report lines go here



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
