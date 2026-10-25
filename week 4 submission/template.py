"""
RECORD CHECK  -  my version
===========================

Name  :Chloe Marie Amelia Allas
Lane  :  AI 
Date  :17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value,limit):
    """function that return the difference and percentage of a value and a limit"""
    difference = limit - value # subtracting value from limit and store the result in a variable called difference
    percentage= (value/limit) * 100 # value as a percentage of limit and the result is stored in a variable called percentage
    if value >= limit:
          status = "OVER LIMIT"
    else:
          status = "OK"
    return difference , percentage , status



def print_report(label,value,limit,difference,percent,status):
        """print the report and format the values"""

        print()
        print("=" * 34) # separator: a line of 34 = is printed
        print(f"  RECORD CHECK  -  {label}")
        print("=" * 34)
        print(f"label       = {label:>10}") # right aligned by 10 spaces
        print(f"value       = {value:>10.2f}") # right aligned by 10 spaces adn rounded to 2 decimal places
        print(f"limit       = {limit:>10.2f}") # right aligned by 10 spaces adn rounded to 2 decimal places
        print(f"difference  = {difference:>10.2f}") # right aligned by 10 spaces adn rounded to 2 decimal places
        print(f"percent     = {percent:>10.2f}") # right aligned by 10 spaces adn rounded to 2 decimal places
        print(f"status      = {status}")
        print("=" * 34)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
      """reads label,value,limit lines from a file and returns the list."""                  
      records = []   # empty list to store the dicts
      with open(path) as f: # open the file to read
            for line in f:
                  label, value, limit = line.strip().split(",")
                  records.append({"label": label,
                                 "value": float(value),
                                 "limit": float(limit)}) # adding the dicts to the empty list using append
      return records
records=load_records("records.txt")



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
count = 0 #start counter at 0
for record in records: # looping through each dict in the list
      difference, percent, status = check_record(record["value"], record["limit"]) # calling the function check_record with its arguments
      print_report(record["label"], record["value"], record["limit"], difference, percent, status)# calling the function print_report with its arguments

if status == "OVER LIMIT":
      count += 1 # increaing the counter by 1 if it is over limit

print(f"there are {count} values that are over limit")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
 
 #error: FileNotFoundError: [Errno 2] No such file or directory: 'record.txt'