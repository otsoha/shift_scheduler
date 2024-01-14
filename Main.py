import pandas as pd
SHIFTDATASTARTS = 1

def load_file(file_name: str): 
  df = pd.read_csv(file_name, index_col=0, skip_blank_lines=True)
  return df.T


# Sor
df = load_file('Example.csv')
df['Available'] = df.iloc[:, :].sum(axis=1)
df = df.sort_values(by='Available', ascending=True)
print(df)






# Mihin kaikkiin pääset
# Monta nakkia haluat
# Kaveritoive






