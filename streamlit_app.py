

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("� 몬테카를로 시뮬레이션 시각화")

st.write("실행 횟수를 입력하고, 동전 던지기(성공 확률 0.5)의 누적 평균을 시뮬레이션합니다.")

# 실행 횟수 입력
num_trials = st.number_input("실행 횟수 (예: 1000)", min_value=10, max_value=10000, value=1000, step=10)

if st.button("시뮬레이션 실행"):
    # 몬테카를로 시뮬레이션: 동전 던지기 (성공 확률 0.5)
    results = np.random.binomial(1, 0.5, int(num_trials))
    cumulative_mean = np.cumsum(results) / (np.arange(1, int(num_trials)+1))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(cumulative_mean, label="누적 평균")
    ax.axhline(0.5, color='red', linestyle='--', label="이론적 확률 0.5")
    ax.set_xlabel("시도 횟수")
    ax.set_ylabel("성공 비율")
    ax.set_title("몬테카를로 시뮬레이션: 동전 던지기 누적 평균")
    ax.legend()
    st.pyplot(fig)
