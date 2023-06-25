import streamlit as st
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import koreanize_matplotlib

# KOSPI 상위 10개 기업 종목 및 기업 이름
kospi_top10 = [
    {'code': '005930', 'name': '삼성전자'},
    {'code': '000660', 'name': 'SK하이닉스'},
    {'code': '207940', 'name': '삼성바이오로직스'},
    {'code': '035420', 'name': 'NAVER'},
    {'code': '005380', 'name': '현대차'},
    {'code': '068270', 'name': '셀트리온'},
    {'code': '051910', 'name': 'LG화학'},
    {'code': '005490', 'name': 'POSCO'},
    {'code': '017670', 'name': 'SK텔레콤'},
    {'code': '105560', 'name': 'KB금융'}
]
# 사이드바
sidebar = st.sidebar
sidebar.header('날짜와 종목명을 선택해주세요')

# 기간 선택
start_date = st.sidebar.date_input('시작 날짜')
end_date = st.sidebar.date_input('종료 날짜')

# 종목 선택
selected_symbols = st.sidebar.multiselect('종목 선택', [item['code'] for item in kospi_top10])



# 선택된 종목의 가격 차트 그리기
for item in kospi_top10:
    if item['code'] in selected_symbols:
        df = fdr.DataReader(item['code'], start_date, end_date)
        plt.plot(df.index, df['Close'], label=item['name'])

plt.title('KOSPI 상위 10개 기업 주식 가격')
plt.xlabel('날짜')
plt.ylabel('주식 가격')
plt.legend([item['name'] for item in kospi_top10 if item['code'] in selected_symbols])
plt.xticks(rotation=45)
plt.tight_layout()

# Matplotlib 그래프를 Streamlit에 표시
st.pyplot(plt)


