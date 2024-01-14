import pandas as pd

SHIFTDATASTARTS = 1
WORKERSPERSHIFT = [6, 5, 4, 1, 1, 1, 1]

def load_file(file_name: str):
  return pd.read_csv(file_name)

def sort(df):
  df['sumOfAvailability'] = df.iloc[:, SHIFTDATASTARTS:].sum(axis=1)
  return df.sort_values(by='sumOfAvailability', ascending=True)

def is_element_present(shifts, worker):
  return any(worker in row for row in shifts)

def check_collisions(shifts, shift_name, worker):
  return is_element_present(shifts[shift_name], worker)

def find_worker_with_fewest_shifts(df, shift_name, assigned_workers):
  available_workers = df[(df[shift_name] == 1) & (~df['Name'].isin(assigned_workers))]
  if available_workers.empty:
    return None
  return available_workers.loc[available_workers['sumOfAvailability'].idxmin(), 'Name']

def sort_shifts(df):
  internal = df.T
  internal['sumOfAvailability'] = internal.iloc[1:-1].sum(axis=1)
  internal = internal.sort_values(by='sumOfAvailability', ascending=True)
  labels_list = internal.T.columns.tolist()
  return labels_list[0:len(labels_list)-1-SHIFTDATASTARTS]

df = load_file('Example.csv')
df_sorted = sort(df)
labels_list = sort_shifts(df_sorted)

shifts = [[] for _ in range(len(labels_list))]

for i, label in enumerate(labels_list):
  found = 0
  while found < WORKERSPERSHIFT[i]:
    assigned_workers = [x for xs in shifts for x in xs]
    shifts[i].append(find_worker_with_fewest_shifts(df_sorted, label, assigned_workers))
    found += 1

print(shifts)


# Mihin kaikkiin pääset
# Monta nakkia haluat
# Kaveritoive






