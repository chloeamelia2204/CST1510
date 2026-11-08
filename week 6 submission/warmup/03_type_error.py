# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})
for key,value in df.items():
    df["value"] = df["value"].astype(int)


df["percent"] = (df["value"] / df["limit"]) * 100 #arithmetic operations cannot be done on strings and numbers
print(df["percent"])