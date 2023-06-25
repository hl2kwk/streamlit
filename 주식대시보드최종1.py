import streamlit as st
import matplotlib.pyplot as plt
import koreanize_matplotlib
import FinanceDataReader as fdr
import plotly.graph_objects as go

# 주식 종목 리스트
stocks = {
    '삼성전자': '005930',
    'LG에너지솔루션': '051910',
    'SK하이닉스': '000660',
    '삼성바이오로직스': '207940',
    'LG화학': '051910'
}

# Streamlit 앱 설정
st.title('KOSPI 5 주식 종가 차트')
selected_stock = st.selectbox('주식 선택', list(stocks.keys()))

# 날짜 범위 설정
start_date = st.date_input('시작 날짜')
end_date = st.date_input('종료 날짜')

# 주식 데이터 가져오기
stock_code = stocks[selected_stock]
df = fdr.DataReader(stock_code, start_date, end_date)

# 차트 그리기
fig, ax = plt.subplots()
ax.plot(df.index, df['Close'])
ax.set(xlabel='날짜', ylabel='가격', title=f'{selected_stock} 종가')


# 차트 출력
st.pyplot(fig)













