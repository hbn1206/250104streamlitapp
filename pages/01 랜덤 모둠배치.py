import streamlit as st
import random

st.title("랜덤 모둠 배치 (숫자 버전)")

# 인원 수 입력
people_count = st.number_input("인원 수를 입력하세요", min_value=1, value=19, step=1)
# 모둠 수 입력
team_count = st.number_input("모둠 수를 입력하세요", min_value=1, value=4, step=1)

# 버튼 클릭 시 실행
if st.button("랜덤 모둠 배치하기"):
    # 1) 인원 수만큼 '숫자' 리스트 만들기
    #    예: 19명이면 ["1","2","3",...,"19"]
    people_list = [str(i + 1) for i in range(people_count)]
    
    # 2) 무작위 셔플
    random.shuffle(people_list)

    # 3) 균등 분배 로직
    base_size = people_count // team_count   # 모둠당 기본 인원
    remainder = people_count % team_count    # 나머지 인원

    teams = []
    start_index = 0
    for i in range(team_count):
        # 이 모둠에 들어갈 사람 수
        size = base_size + (1 if i < remainder else 0)
        team_members = people_list[start_index:start_index + size]
        start_index += size
        teams.append(team_members)

    # 4) 결과 출력
    st.write(f"총 {people_count}명을 {team_count}개 모둠으로 랜덤 배정:")
    for idx, t in enumerate(teams, start=1):
        st.write(f"- 모둠 {idx} ({len(t)}명): {', '.join(t)}")
