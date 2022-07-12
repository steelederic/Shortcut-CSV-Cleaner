import pandas as pd

"""
This script will look for a CSV named "target". After running it will scrape the .csv of
the columns found in the list "keeps".

It will then output a new CSV with the name of var 'output_file_name'
"""
output_file_name = "July 11"

keeps = [
    "id",
    "name",
    "type",
    "requester",
    "owners",
    "is_completed",
    "external_tickets",
    "epic_id",
    "epic",
]

data = pd.read_csv(f"target.csv")
data = data[data.is_completed != False]

for col in data:
    if col not in keeps:
        data.pop(col)
        print(f"Deleted {col}")

# Sort by Features first, create our output CSV.
sorted_data = data.sort_values(by=["type"], ascending=False)
sorted_data.to_csv(output_file_name + ".csv", encoding="utf-8", index=False)
