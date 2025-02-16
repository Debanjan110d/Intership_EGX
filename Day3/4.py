import pandas as pd

data ={
    "Student Name":["St1","St2","St3"],
    "Dept":["CSE","ECE","EEE"],
    "Fees":[10000,20000,30000]
}

table = pd.DataFrame(data)
print(table)