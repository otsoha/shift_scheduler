import pandas as pd
SHIFTDATASTARTS = 1
WORKERSPERSHIFT = [6,5,4,1,1,1,1]

def load_file(file_name: str): 
  df = pd.read_csv(file_name)
  return df

def sort(df):
  df['sumOfAvailability'] = df.iloc[:, SHIFTDATASTARTS:].sum(axis=1)
  df = df.sort_values(by='sumOfAvailability', ascending=True)
  return df

def is_element_present(shifts, worker):
    return any(worker in row for row in shifts)

def check_collisions(shift_name, worker):
  if is_element_present(shifts, worker): 
    return False

def find_worker_with_fewest_shifts(shift_name, assigned_workers):
  available_workers = df[(df[shift_name] == 1) & (~df['Name'].isin(assigned_workers))]
  if available_workers.empty:
    return None 
  min_worker = available_workers.loc[available_workers['sumOfAvailability'].idxmin(), 'Name'] 
  return min_worker

def sort_shifts():
  internal = df.T
  internal['sumOfAvailability'] = internal.iloc[1:-1].sum(axis=1)
  internal = internal.sort_values(by='sumOfAvailability', ascending=True)
  labels_list = internal.T.columns.tolist()
  print(labels_list)
  return labels_list[0:len(labels_list)-1-SHIFTDATASTARTS]
  

df = load_file('Example.csv')
shifts = []
df = sort(df)
labels_list = sort_shifts()


i = 0
for label in labels_list:
  shifts.append([])
  found = 0
  while found < WORKERSPERSHIFT[i]: 
    shifts[i].append(find_worker_with_fewest_shifts(label, [x for xs in shifts for x in xs]))
    found += 1
  i += 1
print(shifts)

# Mihin kaikkiin pääset
# Monta nakkia haluat
# Kaveritoive






