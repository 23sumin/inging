import streamlit as st


import numpy as np

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

st.title("� 몬테카를로 시뮬레이션 시각화")

# 실행 횟수 입력
num_simulations = st.number_input("실행 횟수(시뮬레이션 반복 횟수)", min_value=100, max_value=100000, value=1000, step=100)

st.write(f"총 {num_simulations}번의 시뮬레이션을 실행합니다.")

# 예시: 동전 던지기(성공 확률 0.5)
success_prob = st.slider("성공 확률(예: 동전 앞면 나올 확률)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
trials = st.number_input("한 번에 시도할 횟수(예: 동전 던지는 횟수)", min_value=1, max_value=100, value=10)

if st.button("시뮬레이션 실행"):
    # 몬테카를로 시뮬레이션: 각 시뮬레이션마다 성공 횟수 기록
    results = np.random.binomial(trials, success_prob, int(num_simulations))
    st.write(f"각 시뮬레이션에서 성공한 횟수 분포 (총 {num_simulations}회)")
    if MATPLOTLIB_AVAILABLE:
        fig, ax = plt.subplots()
        ax.hist(results, bins=range(0, trials+2), edgecolor='black', alpha=0.7)
        ax.set_xlabel('성공 횟수')
        ax.set_ylabel('빈도')
        ax.set_title('몬테카를로 시뮬레이션 결과 분포')
        st.pyplot(fig)
    else:
        # matplotlib이 없으면 streamlit 내장 bar_chart 사용
        import pandas as pd
        value_counts = pd.Series(results).value_counts().sort_index()
        st.bar_chart(value_counts)
        st.info('matplotlib이 설치되어 있지 않아 Streamlit 기본 차트로 대체되었습니다.')
