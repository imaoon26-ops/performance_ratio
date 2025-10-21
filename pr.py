import pandas as pd 

excel_file = 'Performance Ratio.xlsx'
xls = pd.ExcelFile(excel_file)
print('Found sheets: ', xls.sheet_names)

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    output_name = f'{sheet_name}.xlsx'
    df.to_excel(output_name, index=False)
    print(f'Seperated {sheet_name} into individual files succcessfully.')