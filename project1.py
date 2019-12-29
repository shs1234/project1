import pandas as pd

#월별 입국자 현황
df=pd.read_excel('./data/목적별 국적별 입국_191227081243.xls',thousands=',')
foreigner_month=df.iloc[-1,2:-1]
#foreigner_month=foreigner_month.reset_index(drop=True)

#기온 데이터
df1=pd.read_excel('./data/기온_전체_2010-2019.xlsx')
#순서 역순으로 바꾸기
df1=df1.loc[::-1].reset_index(drop=True)
#평균기온, 평균최고, 평균최저만 남기고 drop
df1.drop(['지역번호','지역명','최고기온관측지점','최저기온관측지점','최고기온(℃)','최저기온(℃)'],axis=1,inplace=True)

#2019년 9월까지 자르기
df1=df1.iloc[:117]

#독립변수 종속변수 설정
X=df1[['평균기온(℃)','평균최고기온(℃)','평균최저기온(℃)']]
Y=foreigner_month.iloc[::]

#train data, test data 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)  

#다중 회귀분석
from sklearn.linear_model import LinearRegression

lr =LinearRegression()
lr.fit(X_train, Y_train)

r_square = lr.score(X_test, Y_test) # 결정 계수 계산
print(r_square)

#결정계수가 -0.0911728573793209 입니다....
#연도순으로 나열하는게 의미가 없어보입니다.