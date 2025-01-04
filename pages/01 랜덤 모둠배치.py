import streamlit as st
import random

st.title("랜덤 모둠 배치 (숫자 버전)")

# 1) 입력: 인원 수, 모둠 수
people_count = st.number_input("인원 수를 입력하세요", min_value=1, value=10, step=1)
team_count = st.number_input("모둠 수를 입력하세요", min_value=1, value=2, step=1)

# 버튼 클릭 시 실행
if st.button("랜덤 모둠 배치하기"):
    # 2) 인원수만큼 '숫자 리스트' 만들기
    #    예) people_count=5 -> [1,2,3,4,5]
    people_list = [str(i + 1) for i in range(people_count)]
    
    # 3) 랜덤 셔플
    random.shuffle(people_list)

    # 4) 균등 배분
    base_size = people_count // team_count     # 모둠당 최소 배정 인원
    remainder = people_count % team_count      # 나머지

    teams = []
    start_index = 0
    
    for t in range(team_count):
        # 이 모둠에 들어갈 사람 수
        team_size = base_size + (1 if t < remainder else 0)
        team_members = people_list[start_index:start_index + team_size]
        start_index += team_size
        teams.append(team_members)

    # 5) 결과 출력
    st.write(f"**총 {people_count}명**을 **{team_count}개** 모둠으로 랜덤 배정:")
    for i, team in enumerate(teams, start=1):
        st.write(f"- 모둠 {i} ({len(team)}명): {', '.join(team)}")
