# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

#with open("records.txt") as f:--> the file does not exist
with open("records.txt","w+") as f: #uses a mode that writes and read the file
    f.write("R-001 has a value of 87.0 and a limit of 100.0")
    print(f.read())
