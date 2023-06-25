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


# Streamlit 앱의 제목 설정
st.title("날짜별 주식가격 캔들차트")

# 사용자로부터 날짜와 종목명 입력 받기
start_date = st.date_input("시작 날짜")
end_date = st.date_input("종료 날짜")
stock_code = st.text_input("종목 코드")

# FinanceDataReader를 사용하여 주식 데이터 가져오기
df = fdr.DataReader(stock_code, start_date, end_date)

# 시각화를 위한 데이터 준비
fig = go.Figure(data=go.Candlestick(x=df.index,
                                   open=df['Open'],
                                   high=df['High'],
                                   low=df['Low'],
                                   close=df['Close']))

# 그래프에 타이틀 설정
fig.update_layout(title=f'{stock_code} 주식 가격',
                  yaxis_title='주식 가격',
                  xaxis_rangeslider_visible=False)

# 그래프 출력
st.plotly_chart(fig)












