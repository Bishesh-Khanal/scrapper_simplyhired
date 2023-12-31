import pandas as pd

def replace(column, to_replace, replace_with):
    df[column] = df[column].apply(lambda x: x.replace(to_replace, replace_with))

def salary_type(new_column, old_column, position, keyword):
    nan = 'nan'
    df[new_column] = pd.Series([float])
    df[new_column] = df[old_column].apply(lambda x: 1 if keyword in x else float(nan) if nan in x else 0)
    df.insert(position, new_column, df.pop(new_column))

df_original = pd.read_csv('jobs_uncleaned.csv')
df = df_original.copy()

del df['Unnamed: 0']

# ------------------------------------------------------CLEANED THE SALARY---------------------------------------------
df['Salary'] = df['Salary'].apply(lambda x: str(x))

salary_type('Hourly', 'Salary', 2, 'hour')
salary_type('Monthly', 'Salary', 3, 'month')
salary_type('Yearly', 'Salary', 4, 'year')

replace('Salary', 'an hour', '')
replace('Salary', 'a month', '')
replace('Salary', 'a year', '')
replace('Salary', 'Estimated: ', '')
replace('Salary', '$', '')
replace('Salary', ',', '')
replace('Salary', ' ', '')

df['Salary_Begin'] = df['Salary'].apply(lambda x: x[0:x.index('-')] if '-' in x else x if 'From' in x else 'nan')
df.insert(2, 'Salary_Begin', df.pop('Salary_Begin'))
df['Salary_End'] = df['Salary'].apply(lambda x: x[x.index('-')+1:len(x)] if '-' in x else x if 'Upto' in x or 'From' not in x else 'nan')
df.insert(3, 'Salary_End', df.pop('Salary_End'))

replace('Salary_Begin', 'From', '')
replace('Salary_End', 'Upto', '')

df['Salary_Begin'] = df['Salary_Begin'].apply(lambda x: (x+'00' if '.' in x else x+'000') if 'K' in x else x)
df['Salary_End'] = df['Salary_End'].apply(lambda x: (x+'00' if '.' in x else x+'000') if 'K' in x else x)

df['Salary_Begin'] = df['Salary_Begin'].apply(lambda x: x.replace('.', '') if 'K' in x else x)
df['Salary_End'] = df['Salary_End'].apply(lambda x: x.replace('.', '') if 'K' in x else x)

replace('Salary_Begin', 'K', '')
replace('Salary_End', 'K', '')

df['Salary_Begin'] = df['Salary_Begin'].apply(lambda x: float(x))
df['Salary_End'] = df['Salary_End'].apply(lambda x: float(x))


df['Salary_Begin'][870] = 62250
df['Salary_End'][870] = 91300
df['Hourly'][870] = 0
df['Monthly'][870] = 0
df['Yearly'][870] = 1


del df['Salary']

# ------------------------------------------------------CLEANED THE COMPANY NAME-------------------------------------------
replace('Company', ' —', '')

# ------------------------------------------------------CLEANED THE POSTED DATE-------------------------------------------
df['Posted'] = df['Posted'].apply(lambda x: str(x))

df['Posted_Date'] = df['Posted'].apply(lambda x: 6 if 'h' in x else 6 - float(x.replace('d', '')))
df.insert(9, 'Posted_Date', df.pop('Posted_Date'))
df['Posted_Date'] = df['Posted_Date'].apply(lambda x: 30 + x if x <= 0 else x)

df['Posted_Month'] = df['Posted_Date'].apply(lambda x: 10 if x <= 6 else 9 if x in range(7,31) else float('nan'))
df.insert(10, 'Posted_Month', df.pop('Posted_Month'))
df['Posted_Month'] = df['Posted_Month'].apply(lambda x: float(x))

del df['Posted']

# ------------------------------------------------------CLEANED THE TYPE-------------------------------------------
df['Type'] = df['Type'].apply(lambda x: str(x))
replace('Type', ' ', '')
replace('Type', '|', ', ')

df['Type'] = df['Type'].apply(lambda x: float('nan') if '$' in x else x)
df['Type'][421] = float('nan')
df['Type'][510] = float('nan')

# ------------------------------------------------------DROPING THE RELATED JOBS AND RESETING THE INDEX-------------------------------------------
df = df.drop([240, 280, 260, 281, 300])
df = df.reset_index(drop=True)

# ------------------------------------------------------EXPORTING-------------------------------------------
df.to_csv('jobs_cleaned.csv')