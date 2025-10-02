import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 몬테카를로 시뮬레이션 페이지
st.header("몬테카를로 시뮬레이션")

# 실행 횟수 입력
num_simulations = st.number_input("실행 횟수 입력", min_value=100, max_value=1000000, value=10000, step=100)

if st.button("시뮬레이션 실행"):
    import numpy as np
    # 예시: 동전 던지기(앞면 확률 추정)
    results = np.random.binomial(1, 0.5, num_simulations)
    estimated_prob = np.mean(results)
    st.write(f"{num_simulations}번 동전 던지기에서 앞면이 나온 비율(추정 확률): {estimated_prob:.4f}")
