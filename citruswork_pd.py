import pandas as pd

citruswork_dick_list = [
    {'날짜': '2022-02-15', '작업내용': '전정', '농약명': '없음'},
    {'날짜': '2022-03-01', '작업내용': '밑거름', '농약명': '없음'},
    {'날짜': '2022-03-31', '작업내용': '약치기', '농약명': '왕중왕'}
]
df = pd.DataFrame(citruswork_dick_list)
df = df[['날짜', '작업내용', '농약명']]
df['날짜'] = pd.to_datetime(df['날짜'], format='%Y-%m-%d')
print(df)
df.to_csv('citruswork.csv', index = True, header= True, na_rep = '없음', encoding='cp949')

#CSV에서 파일 읽고 원하는 시리즈만으로 데이터프레임 만들기
#df = pd.read_csv('c:\hks\hksapp\citruswork.csv')
#df['날짜'] = pd.to_datetime(df['날짜'], format='%Y-%m-%d')
#df_filtered = df[['ID', '날짜', '작업내용', '농약명']]
#df_filtered.to_csv('citruswork.csv', index = False, header= True, na_rep = '없음')

#from collections import OrderedDict
#citruswork_ordered_dick = OrderedDict(
#    [
#       ('날짜', [2022_02_15, 2022_03_01, 2022_03_31]),
#       ('작업내용', ["전정", "밑거름", "약치기"]),
#       ('농약명', ["없음", "없음", "왕중왕"])
#    ]
#)
#df = pd.DataFrame.from_dict(citruswork_ordered_dick)
#print(df)

#citruswork_list = [
#    [2022_02_15, "전정", "없음"],
#    [2022_03_01, "밑거름", "없음"],
#    [2022_03_31, "약치기", "왕중왕"]
#]
#column_name = ['날짜', '작업내용', '농약명']
#df = pd.DataFrame.from_records(citruswork_list, columns = column_name)
#print(df)

#citruswork_dick = [
#       ['날짜', [2022_02_15, 2022_03_01, 2022_03_31]],
#       ['작업내용', ["전정", "밑거름", "약치기"]],
#       ['농약명', ["없음", "없음", "왕중왕"]]
#    ]
#df = pd.DataFrame.from_dict(dict(citruswork_dick))
#print(df)

#df = pd.read_csv('c:\hks\hksapp\study\citruswork.csv')
#df = pd.read_csv('c:\hks\hksapp\study\citruswork.txt')
#df = pd.read_csv('c:\hks\hksapp\study\citruswork.txt', delimiter = '\t') 탭으로 구분한 경우
#df = pd.read_csv('c:\hks\hksapp\study\citruswork.txt', header = None) 데이터만 있고 헤더가 없는 경우
#df = pd.read_csv('c:\hks\hksapp\study\citruswork.txt', header = None, names = ['wdate', 'work', 'pesticide'] )

#print(df.head)
#type(df.head)

#s1 = pd.core.series.Series([2022_02_15, 2022_03_01, 2022_03_31]) 
#s2 = pd.core.series.Series(["전정", "밑거름", "약치기"])
#s3 = pd.core.series.Series(["없음", "없음", "왕중왕"])
