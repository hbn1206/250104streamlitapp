import streamlit as st
import math
import itertools
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------
# 스트림릿 페이지 기본 설정
# --------------------------------------------------------
st.set_page_config(
    page_title="확률과 통계 수업 - 원순열과 같은 것이 있는 순열", 
    page_icon=":two_hearts:",
    layout="centered"
)

# --------------------------------------------------------
# (1) 원형으로 순열을 시각화하는 함수
#     - 좌표 축 범위를 여유롭게 설정
# --------------------------------------------------------
def draw_single_permutation(ax, permutation):
    """
    permutation: 튜플/리스트 형태 (예: (0,1,2) 또는 (2,0,1))
    ax: 그릴 subplot의 axis
    """
    n = len(permutation)
    # 각도 설정
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)
    
    # 점 연결 (순열 순서대로 연결 -> 원형)
    for i in range(n):
        curr_idx = permutation[i]
        next_idx = permutation[(i + 1) % n]
        ax.plot([x[curr_idx], x[next_idx]], [y[curr_idx], y[next_idx]], 'k-', alpha=0.5)

    # 점 그리기
    ax.scatter(x, y, s=200, c='pink', alpha=0.7, edgecolors='red', linewidths=1)

    # 라벨: 여기서는 permutation[i] + 1 형태로 표시
    for i in range(n):
        label = str(i + 1)
        ax.text(x[i], y[i],
                label,
                ha='center', va='center',
                fontsize=10, fontweight='bold')
    
    # 좌표축 등 숨기기
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    # 필요하다면 축 범위 살짝 넓게 잡아서 원이 안 잘리도록
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)


# --------------------------------------------------------
# (2) 최대 4개까지만 순열을 그려주는 함수
#     - figsize 크기를 키우고, fig.tight_layout() 사용
# --------------------------------------------------------
def draw_circular_permutation_examples(n, max_examples=4):
    """
    n개의 원소에 대한 '모든 일반 순열' 중 최대 4개만 골라
    원형 배치로 시각화 (subplot) 해서 보여줍니다.
    """
    all_perms = list(itertools.permutations(range(n)))
    selected_perms = all_perms[:max_examples]  # 최대 4개만

    num_examples = len(selected_perms)
    if num_examples == 1:
        fig, ax = plt.subplots(1, 1, figsize=(3, 3))
        draw_single_permutation(ax, selected_perms[0])
        fig.tight_layout()
        st.pyplot(fig)
    else:
        rows = 2 if num_examples > 2 else 1
        cols = 2 if num_examples > 2 else num_examples
        fig, axs = plt.subplots(rows, cols, figsize=(3*cols, 3*rows))
        axs = axs.flatten() if num_examples > 1 else [axs]
        for i in range(num_examples):
            draw_single_permutation(axs[i], selected_perms[i])
        # 사용하지 않는 subplot 숨기기
        for i in range(num_examples, len(axs)):
            axs[i].axis('off')

        fig.tight_layout()
        st.pyplot(fig)


# --------------------------------------------------------
# 스트림릿 페이지 구성
# --------------------------------------------------------
st.title(":sparkles: 확률과 통계 실습 :sparkles:")
st.subheader("원순열과 중복순열을 알아보자! :ribbon:")

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

# --------------------------------------------------------
# (A) 원순열(Circular Permutation) 설명
# --------------------------------------------------------
st.markdown("### :round_pushpin: 원순열 (Circular Permutation) :unicorn:")
st.write(
    r"""
    - 총 \( n \)개의 원소를 원형(동그란 테이블 등)에 나열하는 순열을 **원순열**이라고 해요.
    - 일반적인 순열과 달리, 시작점이 어디인지 구분이 되지 않고 **회전**해서 같으면 같은 경우로 봐요.
    
    예를 들어, A, B, C 세 사람을 원형 테이블에 앉힌다고 했을 때,  
    A-B-C, B-C-A, C-A-B 는 모두 같은 배치로 간주해요.
    
    원순열의 개수 공식은 보통 **\((n-1)!\)** 입니다.
    """
)

# 원순열 계산
st.markdown("#### 원순열 예시 계산해보기 :heart:")
n_value = st.number_input("원소의 개수 n을 입력하세요", min_value=1, value=4)
if n_value == 1:
    st.write("원소가 1개면, 원순열은 1가지밖에 없어요 :wink:")
else:
    circular_permutation = math.factorial(n_value - 1)
    st.write(
        f"원소가 {n_value}개라면, 원순열의 개수는 "
        f"**{circular_permutation}** 가지입니다!"
    )

# 시각화 (예시 4개)
st.write(":star: 실제로는 회전하여 같은 순열은 동일하게 보지만, 여기서는 **서로 다른 일반 순열** 중 4가지만 예시로 시각화해볼게요!")
draw_circular_permutation_examples(n_value, max_examples=4)

# 구분선
st.markdown("---")

# --------------------------------------------------------
# (B) 같은 것이 있는 순열 설명
# --------------------------------------------------------
st.markdown("### :round_pushpin: 같은 것이 있는 순열 :rainbow:")
st.write(
    r"""
    - **같은 것이 있는 순열**은 동일한 원소가 여러 번 나타날 수 있는 순열이에요.
    - 예를 들어, \(\{1, 2, 2, 3\}\)과 같이 같은 숫자(2)가 여러 번 등장해도 순열을 계산할 수 있어요.
    - 같은 것이 있는 순열의 개수를 구하는 대표적인 공식 중 하나는 다음과 같아요:
    """
)
st.latex(
    r"""
    \text{같은 것이 있는 순열의 개수} = \frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}
    """
)
st.write(
    r"""
    여기서 \(n = n_1 + n_2 + \dots + n_k\) 이고, 
    각 \(n_i\)는 동일한 원소가 몇 개씩 있는지 나타내요.
    """
)

# 같은 것이 있는 순열 계산 예시
st.markdown("#### 같은 것이 있는 순열 예시 계산해보기 :heart_decoration:")
st.write("서로 다른 원소의 종류(k)와, 각 원소가 몇 개씩 있는지 입력해 보세요!")

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

if st.button("같은 것이 있는 순열 계산하기"):
    # 총 개수
    n_total = sum(counts)
    
    # 분모(각 계수 팩토리얼 곱)
    denominator = 1
    for c in counts:
        denominator *= math.factorial(c)
        
    # 결과
    result = math.factorial(n_total) // denominator
    st.write(f"총 원소의 개수 n = {n_total} 이고,")
    st.write(f"같은 것이 있는 순열의 개수는 **{result}** 가지입니다 :star2:")

    # (추가) 가능한 같은 것이 있는 순열을 전부 출력
    import itertools
    elements = []
    for i, c in enumerate(counts):
        elements.extend([chr(65 + i)] * c)  # A부터 시작
    perm_set = set(itertools.permutations(elements, n_total))
    perm_list = sorted("".join(p) for p in perm_set)
    st.write("**가능한 같은 것이 있는 순열(사전순):**")
    st.write(", ".join(perm_list))

# 구분선
st.markdown("---")

# --------------------------------------------------------
# 마무리 인사
# --------------------------------------------------------
st.write(
    """
    오늘은 확률과 통계에서 자주 등장하는 **원순열**과 **같은 것이 있는 순열**에 대해 알아봤어요.  
    특히 원순열은 회전을 같은 경우로 취급한다는 점이 핵심이에요.  
    예시로 보인 4가지 그림은 '서로 다른 일반 순열'을 그린 것이니 참고하세요.  
    같은 것이 있는 순열 계산 결과와 실제 가능한 순열 목록도 꼭 확인해 보세요.  
    다음 시간에도 재미있는 이론과 예제로 돌아올게요! :sparkling_heart:
    """
)
