import pandas as pd

#기온 데이터
df1=pd.read_excel('./data/기온_전체_2010-2019.xlsx')
#순서 역순으로 바꾸기
df1=df1.loc[::-1].reset_index(drop=True)
#평균기온, 평균최고, 평균최저만 남기고 drop
df1.drop(['지역번호','지역명','최고기온관측지점','최저기온관측지점','최고기온(℃)','최저기온(℃)'],axis=1,inplace=True)
#2019년 9월까지 자르기
temp=df1.iloc[96:108]
temp.set_index(['일시'],inplace=True)

#강수일수
df2=pd.read_excel('./data/2018_강수일수.xlsx')

df2T=df2.transpose()
rain_days=df2T[8].iloc[1:13]
rain_days.astype('float')

#강수량
rainfall=pd.read_excel('./data/2018_강수량.xlsx',skiprows=[1,2,3,4,5,6,7])
rainfall=rainfall['Unnamed: 2']

#황사일수
dust=pd.read_excel('./data/2018_황사일수.xlsx')
dustT=dust.transpose()
dust=dustT[8].iloc[1:13]

#체감온도
feelingtemp = pd.read_excel('./data/2018_체감온도.xlsx', header=3)

for i in range(len(feelingtemp['일자'])):
    feelingtemp.loc[i, '월별'] = str(feelingtemp.loc[i, '일자'])[0:4]+ '.' + str(feelingtemp.loc[i, '일자'])[5:7] 

feelingtemp = feelingtemp.groupby('월별').mean()

#소비자 물가지수
df7 = pd.read_csv('C:/project1/data/2018소비자물가지수.csv', encoding='cp949', header=0).iloc[:, 2:]
sobija = pd.DataFrame(df7.T[0])

#폭염지수
heat_wave = pd.read_excel('./data/2018_폭염지수.xlsx', header=5).iloc[[1], 1:13]
heat_wave = heat_wave.T

rain_days.index=rainfall.index=dust.index=feelingtemp.index=sobija.index=heat_wave.index=temp.index

total_data=pd.concat([temp,rain_days,rainfall,dust,feelingtemp,heat_wave,sobija],axis=1)
cols=['평균기온(℃)','평균최고기온(℃)','평균최저기온(℃)','강수일수','강수량','황사일수','기온(°C)','풍속(m/s)','체감기온(°C)','폭염지수','소비자물가지수']
total_data.columns=cols

