

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("� 몬테카를로 시뮬레이션: 원주율 추정")

st.write("정사각형에 내접하는 원 위에 무작위로 점을 찍어 원주율(π)을 추정합니다.")

num_points = st.number_input("찍을 점의 개수", min_value=100, max_value=1000000, value=1000, step=100)

if st.button("시뮬레이션 실행"):
    # 무작위 점 생성
    x = np.random.uniform(-1, 1, int(num_points))
    y = np.random.uniform(-1, 1, int(num_points))
    # 원 안에 있는 점 판별
    inside = x**2 + y**2 <= 1
    num_inside = np.sum(inside)
    pi_estimate = 4 * num_inside / int(num_points)

    # 시각화
    fig, ax = plt.subplots(figsize=(6, 6))
    # 정사각형
    square = plt.Rectangle((-1, -1), 2, 2, fill=False, color='black')
    ax.add_patch(square)
    # 원
    circle = plt.Circle((0, 0), 1, fill=False, color='blue')
    ax.add_patch(circle)
    # 점
    ax.scatter(x[inside], y[inside], color='green', s=2, label='원 안')
    ax.scatter(x[~inside], y[~inside], color='red', s=2, label='원 밖')
    ax.set_aspect('equal')
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.legend()
    ax.set_xticks([])
    ax.set_yticks([])
    st.pyplot(fig)

    st.write(f"원 안에 찍힌 점의 수: {num_inside} / {int(num_points)}")
    st.write(f"추정된 원주율(π): {pi_estimate}")
