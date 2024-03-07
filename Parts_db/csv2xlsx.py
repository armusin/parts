import os
import pandas as pd

# Current directory containing CSV files
csv_directory = os.getcwd()

# Output Excel file name
excel_file = 'Parts.xlsx'

# List all CSV files in the current directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# Create a Pandas Excel writer using XlsxWriter as the engine
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

# Read each CSV file and write to separate sheets in the Excel file
for csv_file in csv_files:
    csv_path = os.path.join(csv_directory, csv_file)
    sheet_name = os.path.splitext(csv_file)[0]  # Use file name as sheet name
    df = pd.read_csv(csv_path)
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

# Close the Pandas Excel writer to save the Excel file
excel_writer.close()

print(f'Excel file "{excel_file}" created successfully.')
