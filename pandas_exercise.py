import pandas as pd

cvs_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.csv'

csv_df = pd.read_csv(cvs_url, skiprows=1)

csv_df

tsv_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.tsv'

tsv_df = pd.read_csv(tsv_url, skiprows=1, sep='\t')

print(tsv_df)

xlsx_url = 'https://github.com/PacktWorkshops/The-Data-Science-Workshop/blob/master/Chapter01/Dataset/overall_topten_2012-2013.xlsx?raw=true'

xlsx_df = pd.read_excel(xlsx_url, skiprows=1, sheet_name=1)

print(xlsx_df)