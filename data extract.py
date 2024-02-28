import pandas as pd

# Load the Wave4.csv file to extract the specified variables
wave4_df = pd.read_csv('wave/Wave4.csv')

# List of variables to extract
variables_to_extract = [
    'R4GENDER', 'S4GENDER', 'R4SHLT', 'S4SHLT', 'R4BMI', 'S4BMI', 'R4MSTOT', 'S4MSTOT', 'R4COGTOT', 'S4COGTOT',
    'R4INHPFN', 'S4INHPFN', 'R4INHPE', 'S4INHPE', 'H4HHRES', 'H4CHILD', 'R4LIVSIB', 'S4LIVSIB',
    'H4INPOV', 'H4INPOVA', 'H4AIRA', 'H4ATOTB', 'R4IEARN', 'S4IEARN', 'H4ITOT', 'R4PENINC', 'S4PENINC',
    'R4HIGOV', 'S4HIGOV', 'R4PRPCNT', 'S4PRPCNT', 'R4UNEMP', 'S4UNEMP', 'R4SLFEMP', 'S4SLFEMP', 'R4RETMON', 'S4RETMON'
]

# Filter the dataframe for the specified variables
extracted_variables_df = wave4_df.filter(items=variables_to_extract)

# Export the filtered dataframe to a new CSV file
export_path = 'extracted_variables_wave4.csv'
extracted_variables_df.to_csv(export_path, index=False)
