import pandas as pd
'''
This script will look for a CSV named "target". After running it will scrape the .csv of
the columns found in the list "keeps".

It will then output a new CSV with the name of var 'output_file_name'
'''
output_file_name = 'June 22'
keeps = ['id', 'name', 'type', 'requester', 'owners', 'description',
         'is_completed', 'external_tickets', 'epic_id', 'epic']

# Make this the location of your CSV.
data = pd.read_csv(
    f'C:\\Users\\NetYield Support\\Desktop\\shortcut\\target.csv')

# Wipe out every row that is incomplete
data = data[data.is_completed != False]

# Iterate through columns and get rid of trash
for col in data:
    if col not in keeps:
        data.pop(col)
        print(f'Deleted {col}')

# Sort by Features first, create our output CSV.
sorted_data = data.sort_values(by=['type'], ascending=False)
sorted_data.to_csv(output_file_name + '.csv', encoding='utf-8', index=False)