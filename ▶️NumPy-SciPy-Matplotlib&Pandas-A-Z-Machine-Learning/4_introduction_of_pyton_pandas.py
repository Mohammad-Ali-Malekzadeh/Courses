import pandas as pd

mydataset = {"cars": ["bmw", "volvo", "ford"], "passing": [3, 7, 3]}

myvar = pd.DataFrame(mydataset)
print(myvar)