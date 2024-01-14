import pandas as pd
SHIFTDATASTARTS = 1
SHIFT0WORKERS = 1
SHIFT1WORKERS = 1
SHIFT2WORKERS = 1
SHIFT3WORKERS = 1
SHIFT4WORKERS = 1

def load_file(file_name: str): 
  df = pd.read_csv(file_name, index_col=0, skip_blank_lines=True)
  return df.T


df = load_file('Example.csv')
df['Available'] = df.iloc[:, :].sum(axis=1)
df = df.sort_values(by='Available', ascending=True)
print(df)

assigned_shifts = []

# Go row by row and pick the first available worker
for index, row in df.iterrows():
  print(row)
  




# Mihin kaikkiin pääset
# Monta nakkia haluat
# Kaveritoive






