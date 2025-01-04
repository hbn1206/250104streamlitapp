import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# 페이지 기본 설정
st.set_page_config(
    page_title="확률과 통계 수업 - 원순열과 중복순열", 
    page_icon=":two_hearts:",
    layout="centered"
)

# 함수: 원순열 그림 그리기
def draw_circular_permutation(n):
    """
    n개의 요소를 원 형태로 배치해 시각화합니다.
    n ≤ 26일 경우 알파벳 A, B, C... 로 Label,
    그 이상일 경우 숫자 1, 2, 3...로 Label합니다.
    """
    # 그리기 위한 figure, axis 생성
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_aspect('equal', 'box')
    plt.axis('off')  # 축 표시 제거

    # 원 위의 각 요소의 각도 계산
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)

    # 원 위의 점들 연결 (순서대로 연결하여 원형 표현)
    for i in range(n):
        next_i = (i + 1) % n
        ax.plot([x[i], x[next_i]], [y[i], y[next_i]], 'k-', alpha=0.5)

    # 점 그리기
    ax.scatter(x, y, s=300, c='pink', alpha=0.7, edgecolors='red', linewidths=1)

    # 라벨 설정 (알파벳 or 숫자)
    labels = []
    if n <= 26:
        # 알파벳 사용 (A, B, C, ...)
        base_ord = ord('A')
        for i in range(n):
            labels.append(chr(base_ord + i))
    else:
        # 숫자 사용
        labels = [str(i + 1) for i in range(n)]

    for i in range(n):
        ax.text(x[i], y[i],
                labels[i],
                ha='center', va='center',
                fontsize=12, fontweight='bold')

    st.pyplot(fig)

# 페이지 헤더
st.title(":sparkles: 확률과 통계 실습 :sparkles:")
st.subheader("원순열과 중복순열을 알아보자! :ribbon:")

# 간단한 소개 섹션
st.write(
    """
    안녕하세요? :smiley:  
    이번 실습에서는 **원순열**과 **중복순열**을 간단히 살펴볼 거예요.  
    아래 설명을 따라가면서, 해당 개념들을 직접 계산해 보거나 예시를 살펴볼 수 있도록 
    간단한 기능들을 준비했어요. :two_hearts:
    """
)

# 구분선
st.markdown("---")

# 원순열(Circular Permutation) 설명 섹션
st.markdown("### :round_pushpin: 원순열 (Circular Permutation) :unicorn:")
st.write(
    """
    - 총 \\( n \\)개의 원소를 원형(동그란 테이블 등)에 나열하는 순열을 **원순열**이라고 해요.
    - 일반적인 순열과 달리, 시작점이 어디인지 구분이 되지 않고 **회전**해서 같으면 같은 경우로 봐요.
    
    예를 들어, A, B, C 세 사람을 원형 테이블에 앉힌다고 했을 때,  
    A-B-C, B-C-A, C-A-B 는 모두 같은 배치로 간주해요.
    
    원순열의 개수 공식은 보통 **\\((n-1)!\\)** 입니다.
    """
)

# 원순열 계산 + 시각화 예시
st.markdown("#### 원순열 예시 계산해보기 :heart:")
n_value = st.number_input("원소의 개수 n을 입력하세요", min_value=1, value=5)
if n_value == 1:
    st.write("원소가 1개만 있으면, 원순열은 1가지밖에 없어요 :wink:")
else:
    circular_permutation = math.factorial(n_value - 1)
    st.write(
        f"원소가 {n_value}개라면, 원순열의 개수는 "
        f"**{circular_permutation}** 가지입니다!"
    )

# 원형 배치 시각화
if n_value >= 1:
    st.write(":star: 원소들을 원형으로 배치해보면 이런 모습이 돼요!")
    draw_circular_permutation(n_value)

# 구분선
st.markdown("---")

# 중복순열(Permutation with Repetition) 설명 섹션
st.markdown("### :round_pushpin: 중복순열 (Permutation with Repetition) :rainbow:")
st.write(
    """
    - **중복순열**은 동일한 원소가 여러 번 나타날 수 있는 순열이에요.
    - 예를 들어, {1, 2, 2, 3}과 같이 같은 숫자(2)가 여러 번 등장해도 순열을 계산할 수 있어요.
    - 중복순열의 개수를 구하는 대표적인 공식 중 하나는 다음과 같아요:
    
    \[
    \\text{중복순열의 개수} = \\frac{n!}{n_1! \\times n_2! \\times \\cdots \\times n_k!}
    \]
    여기서, \\(n = n_1 + n_2 + \\dots + n_k\\) 이고,  
    각 \\(n_i\\)는 동일한 원소가 몇 개씩 있는지 나타내요.
    """
)

# 중복순열 계산 예시
st.markdown("#### 중복순열 예시 계산해보기 :heart_decoration:")
st.write("서로 다른 원소의 종류(k)와, 각 원소가 몇 개씩 있는지 입력해 보세요!")

# 종류(k) 입력
k = st.number_input("원소 종류의 개수(k)", min_value=1, value=3, step=1)

counts = []
for i in range(k):
    counts.append(
        st.number_input(
            f"{i+1}번 원소의 개수를 입력하세요", 
            min_value=1, 
            value=1, 
            step=1, 
            key=f"count_{i}"
        )
    )

if st.button("중복순열 계산하기"):
    # 총 개수
    n_total = sum(counts)
    
    # 분모(각 계수 팩토리얼 곱)
    denominator = 1
    for c in counts:
        denominator *= math.factorial(c)
        
    # 결과
    result = math.factorial(n_total) // denominator
    st.write(f"총 원소의 개수 n = {n_total} 이고,")
    st.write(f"중복순열의 개수는 **{result}** 가지입니다 :star2:")

# 구분선
st.markdown("---")

# 마무리 멘트
st.write(
    """
    오늘은 확률과 통계에서 자주 등장하는 **원순열**과 **중복순열**에 대해 알아봤어요.  
    시각화한 그림을 통해 좀 더 직관적으로 이해할 수 있었길 바래요.  
    다음 시간에도 재미있는 이론과 예제로 돌아올게요! :sparkling_heart:
    """
)
