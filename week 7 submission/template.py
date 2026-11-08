"""
RECORD CHECK  -  my version
===========================

Name  : Allas Chloe Marie Amelia
Lane  : AI 
Date  : 05/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):

    """Cleans and parses one raw, messy line into a dict"""

    line = raw_line.strip().lower() #removes unnecessary whitespaces and converts the text to lowercase
    survey_part, rest = line.split(",", 1) # separates the survey from the rest of the string
    survey = survey_part.strip() #removes unnecessary whitespaces at the beginning and the end of the survey and stores it

    storage = {} #creates an empty dictionary
    for i in rest.split(","): # separates the rest at comma and loops through each item
        key, value = i.strip().split("=", 1) # removes unnecessary whitespaces, separates at equal sign and assign values to key and value
        storage[key.strip().lower()] = float(value.strip()) # converts the keys to lowercase and the values to float

    return {'survey': survey, 'rating': storage["rating"], 'age': storage["age"]} #return a dictionary

def status_of(storage):

    """Return the status based on the value of rating"""

    count = 0 # set count to 0
    #conditions for different status categories
    if storage["rating"] >= 8:
        status = "OVER LIMIT"
    elif storage["rating"] >= 4:
        status = "WARNING"
    else:
        status = "FLAGGED"


    return status

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [" SURVEY_2026,RATING=4, AGE=23",
               "survey_2027,   rating=6,   age=35",
               "   survey_2028,rating=5,AGE=20   ",
               " Survey_2029, RATING=8, age=29 ",
               "    SURVEY_2030, rating=9,age=26   "]   # replace with your code

with open("survey.txt","w") as f: #creates a .txt file 
    for line in raw_records:
        f.write(line + "\n") # writes in the file add skips a line


raw_records = []
with open("survey.txt", "r") as f: # opens the file for reading
    for line in f: #loops through each line in the file
        raw_records.append(line) #loading the lines from the file
        

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.


count = 0 # set count to 0
for raw_record in raw_records:
    cleaned_record = parse_line(raw_record) #calls the parse_line function and stores it
    status = status_of(cleaned_record) # calls the status_of function and stores it
    print(cleaned_record, status) # displays the cleaned survey records and the status



if status == "flagged":
    count += 1 # updates count whenever a rating is flagged

print(f"There are {len(raw_records)} records amongst which, {count} were flagged ") # displays a summary on the number of records and of  flagged records


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
