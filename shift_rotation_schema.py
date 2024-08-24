import pandas as pd
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Definer listen over personer i vaktrulleringen
person_liste = ['Doe, Jane', 'Doe, John', 'Poppins, Mary', 
                'Karlsen, Lill-Kristin']

# Norske månedsnavn
måned_dict = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'mai', 6: 'jun', 
              7: 'jul', 8: 'aug', 9: 'sep', 10: 'okt', 11: 'nov', 12: 'des'}

# Generer vaktplanen
vaktplan = []
start_dato = datetime.strptime("15.03.24", "%d.%m.%y")
for i in range(9):
    for person in person_liste:
        start_dato_str = f'{start_dato.day}.{måned_dict[start_dato.month]}'
        uke_nummer = start_dato.isocalendar()[1]
        vaktplan.append([person, start_dato_str, uke_nummer])
        start_dato += timedelta(days=7)

# Konverter planen til en pandas DataFrame
plan_df = pd.DataFrame(vaktplan, columns=['Navn', 'Start', 'Uke'])

# Initialiser en workbook og velg aktivt ark
wb = Workbook()
ws = wb.active

# Skriv DataFrame til Excel-arket
for r in dataframe_to_rows(plan_df, index=False, header=True):
    ws.append(r)

# Lagre workbook
wb.save('vaktplan_2024.xlsx')
