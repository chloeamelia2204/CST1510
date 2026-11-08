"""
RECORD CHECK  -  my version
===========================

Name  :Allas Chloe Marie Amelia
Lane  :  AI 
Date  : 22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:

    over_limit_count = 0  # attribute shared by all objects
    def __init__(self, label, value, limit): #
        """Initialises objects attribute when created"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Calculate percent and return a status for each value and limit pairs """
        percent = (self.value/self.limit) * 100
        return "OVER LIMIT" if percent>= 100 else  "WARNING" if percent >= 90 else "OK" #check percent and assign a status
        

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

  # replace with your code
def load_records(path):
    """Reads label, value, limit lines from a file and return a list of Records objects"""
    records = [] # empty list created

    with open(path) as f:
        for line in f: #reads each line from a file 
            label, value, limit = line.strip().split(",") # removes whitespaces and separate label, value and limit
            records.append(Record(label, float(value), float(limit))) #creates an object and add it to the list
    return records
    
records = load_records("records_sample.txt")

for record in records:
    print(f"{record.label} = {record.status()}") #prints each label and their corresponding status


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

Record.over_limit_count=0 # sets counter to 0
for record in records: #loops through each objects in the list
    print()
    """Display the formatted report"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"label     = {record.label:>10}")
    print(f"value     = {record.value:>10.2f}")
    print(f"limit     = {record.limit:>10.2f}")
    print(f"status    = {record.status():>10}")
    print("=" * 34)

    # your report lines go here
    if record.status() == "OVER LIMIT":
        Record.over_limit_count += 1 #updates count by one for each values that are over limit
print(f"There has been a total of {Record.over_limit_count} OVER LIMIT records ") # displays the number of over limit count


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
