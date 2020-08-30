import pandas as pd
import re

nao_extra = [10., 7., 8., 7., 5., 5., 4., 1.]
df = pd.read_csv('./data/grades.csv')

df['aula'] = df['assignment'].apply(lambda x: re.search('Aula\d', x).group(0) if re.search('Aula\d', x) else None)

table = pd.pivot_table(df, values='score', index=['student_id'], columns=['aula'], aggfunc=max)

for a in range(8):
    num_aula = a+1
    table[f'nota_aula_{num_aula}'] = 10*table[f'Aula{num_aula}']/nao_extra[a]

table['media'] = 10*table.sum(axis=1)/sum(nao_extra)
table['media_tamponada'] =table['media'].apply(lambda x: min(x, 10))
table.to_excel('./notas.xls')