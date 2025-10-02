

import streamlit as st
from prob_viz import plot_normal_distribution, plot_binomial_distribution

st.title("확률 분포 시각화 데모 🎲")
st.write("확률 분포의 의미를 직관적으로 이해할 수 있도록 다양한 분포를 시각화합니다.")

tab1, tab2 = st.tabs(["정규분포", "이항분포"])

with tab1:
    st.header("정규분포 시각화")
    mu = st.slider("평균(μ)", -5.0, 5.0, 0.0, 0.1)
    sigma = st.slider("표준편차(σ)", 0.1, 5.0, 1.0, 0.1)
    buf = plot_normal_distribution(mu, sigma)
    st.image(buf, caption=f"Normal(μ={mu}, σ={sigma})")

with tab2:
    st.header("이항분포 시각화")
    n = st.slider("시행 횟수(n)", 1, 50, 10)
    p = st.slider("성공 확률(p)", 0.0, 1.0, 0.5, 0.01)
    buf = plot_binomial_distribution(n, p)
    st.image(buf, caption=f"Binomial(n={n}, p={p})")
