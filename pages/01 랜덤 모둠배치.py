import streamlit as st
import random
import string

st.title("랜덤 모둠 배치")

# 1) 입력: 인원 수, 모둠 수
people_count = st.number_input("인원 수를 입력하세요", min_value=1, value=10, step=1)
team_count = st.number_input("모둠 수를 입력하세요", min_value=1, value=2, step=1)

# 버튼 클릭 시 실행
if st.button("랜덤 모둠 배치하기"):
    # 2) 인원수만큼 '알파벳' 리스트 만들기
    #    - 예: people_count=5 -> ['A','B','C','D','E']
    #    - 만약 26보다 많으면? 알파벳 반복 or 확장
    #      여기서는 간단히 'A'부터 시작하여 반복(27명이면 'A'~'Z' 뒤 다시 'A'...)
    
    letters = []
    for i in range(people_count):
        # A=65 in ASCII, 26이 넘어가면 다시 돌도록
        letters.append(chr(65 + (i % 26)))
    
    # 3) 랜덤 셔플
    random.shuffle(letters)

    # 4) 균등 배분
    #    - 팀마다 people_count // team_count 명씩 우선 배정
    #    - 나머지(people_count % team_count)는 앞쪽부터 1명씩 추가
    base_size = people_count // team_count
    remainder = people_count % team_count
    
    # team_list[i]에 배정
    teams = []
    start_index = 0
    
    for t in range(team_count):
        # 이 팀에 들어갈 사람 수
        team_size = base_size + (1 if t < remainder else 0)
        team_members = letters[start_index:start_index + team_size]
        start_index += team_size
        teams.append(team_members)

    # 5) 결과 출력
    st.write(f"**총 {people_count}명**을 **{team_count}개** 모둠으로 랜덤 배정:")
    for i, team in enumerate(teams, start=1):
        st.write(f"- 모둠 {i} ({len(team)}명): {', '.join(team)}")
