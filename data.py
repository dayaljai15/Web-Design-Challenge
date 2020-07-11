import pandas as pd

# Read csv file 
df = pd.read_csv('downloads/cities.csv')

# Save 
df.to_html('data.html', index=False)


table = df.to_html()
print(table)
