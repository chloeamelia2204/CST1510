# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, percent):    #self should be a parameter here
        return percent

r = Record()
print(r.status(95))
