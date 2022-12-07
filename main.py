import pandas as pd
from Absolute_Loader import abs_loader

list = ['Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ,
 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]

df = pd.DataFrame(columns = list)

# Absolute loader
print(abs_loader)
df = abs_loader.get_absolute_loader(df)
print(df)