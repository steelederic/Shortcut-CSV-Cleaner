# Shortcut-CSV-Cleaner
Short Pandas script to clean up Shortcut iteration exports.

This script will look for a CSV named "target". After running it will scrape the .csv of
the columns found in the list "keeps".

It will then output a new CSV with the name of var 'output_file_name', with only completed rows, sorted by Features first.
```
*This currently outputs to the directory that main.py is run in.
```

**To run**
```
Clone repo
Install python > 3.8
pip install -r requirements.txt
```
