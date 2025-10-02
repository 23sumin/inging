import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom
from io import BytesIO


def plot_normal_distribution(mu=0, sigma=1, size=1000):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, size)
    y = norm.pdf(x, mu, sigma)
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'Normal($\mu$={mu}, $\sigma$={sigma})')
    ax.set_title('정규분포')
    ax.set_xlabel('x')
    ax.set_ylabel('확률밀도')
    ax.legend()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf

def plot_binomial_distribution(n=10, p=0.5):
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)
    fig, ax = plt.subplots()
    ax.bar(x, y, label=f'Binomial(n={n}, p={p})')
    ax.set_title('이항분포')
    ax.set_xlabel('성공 횟수')
    ax.set_ylabel('확률')
    ax.legend()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf
