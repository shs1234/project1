import pandas as pd

#월별 입국자 현황
df=pd.read_excel('./data/목적별 국적별 입국_191227081243.xls',thousands=',')
foreigner_month=df.iloc[-1,2:-1]

