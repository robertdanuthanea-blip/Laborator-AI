#EX1
# import pandas as pd
# df = pd.read_csv('data - data.csv')
# pd.set_option('display.max_rows', None)      
# pd.set_option('display.max_columns', None)   
# pd.set_option('display.width', None)         
# pd.set_option('display.max_colwidth', None)  
# print(df)

#EX2
# import pandas as pd
# df = pd.read_csv('data - data.csv')
# print(df[df['Age'] > 40].head(10))

#EX3
# import pandas as pd
# df = pd.read_csv('data - data.csv')
# rezultat = df[(df['Overall'] >= 85) & (df['Age'] < 25)]
# print(rezultat)

#EX4
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# df_sortat = df.sort_values(by='Skill Moves', ascending=False)

# print(df_sortat)

#EX5
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# df['Contract Valid Until'] = pd.to_numeric(df['Contract Valid Until'], errors='coerce')
# rezultat = df[df['Contract Valid Until'] == 2021]

# print(rezultat)

#EX6
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# print(df.shape)
# print(df['Name'].nunique())

#EX7
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# print(df['Nationality'].value_counts().head(5).to_frame())

#EX8

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data - data.csv')

# top_5 = df['Nationality'].value_counts().head(5)

# top_5.plot(kind='pie', autopct='%1.1f%%')
# plt.title('Top 5 Naționalități Jucători')
# plt.ylabel('') 
# plt.show()

#EX9
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# rezultat = df.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()

# print(rezultat.to_string())


#EX10
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# df['Position'] = df['Position'].fillna("Unknown")

# print(df['Position'].to_string(index=False))

#EX11
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# top_club = df.groupby('Club')['Overall'].mean().sort_values(ascending=False).head(1)

# print(top_club.to_string())

#EX12
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# def clean_money(value):
#     if isinstance(value, str):
#         value = value.replace('€', '')
#         if 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         elif 'K' in value:
#             return float(value.replace('K', '')) * 1000
#     return pd.to_numeric(value, errors='coerce')

# df['Value_Num'] = df['Value'].apply(clean_money)
# df['Wage_Num'] = df['Wage'].apply(clean_money)

# rezultat = len(df[df['Value_Num'] > df['Wage_Num']])

# print(rezultat)

#EX13
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# def clean_money(value):
#     if isinstance(value, str):
#         value = value.replace('€', '')
#         if 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         elif 'K' in value:
#             return float(value.replace('K', '')) * 1000
#     return pd.to_numeric(value, errors='coerce')

# df['Value_Num'] = df['Value'].apply(clean_money)
# df['Wage_Num'] = df['Wage'].apply(clean_money)
# df['is_underpaid'] = df['Wage_Num'] < (df['Value_Num'] / 100)

# print(df[['Name', 'Wage', 'Value', 'is_underpaid']].head(10).to_string(index=False))

#EX14
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# df['SprintSpeed'] = pd.to_numeric(df['SprintSpeed'], errors='coerce').fillna(0)

# df['Scor_Personalizat'] = 0.3 * df['Overall'] + 0.3 * df['Potential'] + 0.2 * df['SprintSpeed']

# rezultat = df[['Name', 'Overall', 'Potential', 'SprintSpeed', 'Scor_Personalizat']].sort_values(by='Scor_Personalizat', ascending=False).head(10)

# print(rezultat.to_string(index=False))

#EX15
# import pandas as pd

# df = pd.read_csv('data - data.csv')

# def clean_money(value):
#     if isinstance(value, str):
#         value = value.replace('€', '')
#         if 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         elif 'K' in value:
#             return float(value.replace('K', '')) * 1000
#     return pd.to_numeric(value, errors='coerce')

# df['Value_Num'] = df['Value'].apply(clean_money)
# df['Wage_Num'] = df['Wage'].apply(clean_money)

# afacere_df = df[['Name', 'Wage', 'Value']].copy()
# afacere_df['difference'] = df['Value_Num'] - df['Wage_Num']
# afacere_df = afacere_df.sort_values(by='difference', ascending=False)

# print(afacere_df.to_string(index=False))

#EX16
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv('data - data.csv')

# def clean_money(value):
#     if isinstance(value, str):
#         value = value.replace('€', '')
#         if 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         elif 'K' in value:
#             return float(value.replace('K', '')) * 1000
#     return pd.to_numeric(value, errors='coerce')

# df['Value_Num'] = df['Value'].apply(clean_money)
# df['Wage_Num'] = df['Wage'].apply(clean_money)

# sns.scatterplot(data=df, x='Value_Num', y='Wage_Num')
# plt.title('Relația dintre Valoare și Salariu')
# plt.show()

