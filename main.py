import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="확률과 통계 수업 - 원순열과 중복순열", 
    page_icon=":two_hearts:",
    layout="centered"
)

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
    - 총 \( n \)개의 원소를 원형(동그란 테이블 등)에 나열하는 순열을 **원순열**이라고 해요.
    - 일반적인 순열과 달리, 시작점이 어디인지 구분이 되지 않고 **회전**해서 같으면 같은 경우로 봐요.
    
    예를 들어, A, B, C 세 사람을 원형 테이블에 앉힌다고 했을 때,  
    A-B-C, B-C-A, C-A-B 는 모두 같은 배치로 간주해요.
    
    원순열의 개수 공식은 보통 **\((n-1)!\)** 입니다.
    """
)

# 원순열 계산 예시
st.markdown("#### 원순열 예시 계산해보기 :heart:")
n_value = st.number_input("원소의 개수 n을 입력하세요", min_value=1, value=5)
if n_value == 1:
    st.write("원소가 1개만 있으면, 원순열은 1가지밖에 없어요 :wink:")
elif n_value > 1:
    circular_permutation = 1
    for i in range(1, n_value):
        circular_permutation *= i
    st.write(f"원소가 {n_value}개라면, 원순열의 개수는 **{circular_permutation}** 가지입니다!")

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
    여기서, \(n = n_1 + n_2 + \\dots + n_k\) 이고,  
    각 \(n_i\)는 동일한 원소가 몇 개씩 있는지 나타내요.
    """
)

# 중복순열 계산 예시
st.markdown("#### 중복순열 예시 계산해보기 :heart_decoration:")
st.write("서로 다른 원소의 종류(k)와, 각 원소가 몇 개씩 있는지 입력해 보세요!")

# 종류(k) 입력
k = st.number_input("원소 종류의 개수(k)", min_value=1, value=3, step=1)

# 각 원소에 대한 개수 입력
import math

counts = []
for i in range(k):
    counts.append(
        st.number_input(f"{i+1}번 원소의 개수를 입력하세요", min_value=1, value=1, step=1, key=f"count_{i}")
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
    오늘은 확률과 통계에서 자주 등장하는 원순열과 중복순열에 대해 알아봤어요.  
    다음 시간에도 재미있는 이론과 예제로 돌아올게요! :sparkling_heart:
    """
)
