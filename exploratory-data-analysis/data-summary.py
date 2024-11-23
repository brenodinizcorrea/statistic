import pandas as pd
import os.path

fullpath = os.path.abspath("/Users/breno.diniz/Documents/studies/github_personal/statistic/database/Dados_EB.xls")

data = pd.read_excel(io=fullpath, sheet_name=2)

print(data)