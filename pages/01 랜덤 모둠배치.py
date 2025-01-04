import streamlit as st
import random

st.title("랜덤 모둠 배치 (숫자 버전, remainder 무작위 분배)")

# 1) 입력: 인원 수, 모둠 수
people_count = st.number_input("인원 수를 입력하세요", min_value=1, value=19, step=1)
team_count = st.number_input("모둠 수를 입력하세요", min_value=1, value=4, step=1)

if st.button("랜덤 모둠 배치하기"):
    # 2) 1번 ~ people_count번까지 숫자 문자열로 준비
    people_list = [str(i + 1) for i in range(people_count)]
    # 셔플해서 무작위 순서로 만든다
    random.shuffle(people_list)

    # 3) 균등 분배를 위한 기본 값 & 나머지
    base_size = people_count // team_count
    remainder = people_count % team_count

    # 4) 모든 팀에 우선 base_size만큼 할당
    team_sizes = [base_size] * team_count

    # 5) 나머지 remainder만큼을 "무작위 팀"에 1명씩 추가
    #    team_count 중에서 remainder개의 팀을 뽑아 각 팀에 +1
    if remainder > 0:
        extra_teams = random.sample(range(team_count), remainder)
        for t_idx in extra_teams:
            team_sizes[t_idx] += 1

    # 6) 실제 인원을 teams 리스트에 할당
    teams = []
    start_index = 0
    for size in team_sizes:
        team_members = people_list[start_index : start_index + size]
        start_index += size
        teams.append(team_members)

    # 7) 결과 출력
    st.write(f"총 {people_count}명을 {team_count}개 모둠으로 랜덤 배정했습니다.")
    for i, t in enumerate(teams, start=1):
        st.write(f"- 모둠 {i} ({len(t)}명): {', '.join(t)}")
