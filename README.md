# Programmers
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

## 📚 문법 연습용 (컴프리헨션 / Counter / zip / enumerate / sorted) 문제 정리
- `for-if` 반복문 위주로만 풀어와서 아래 문법에 익숙해지기 위한 연습용 목록
- 조건은 단순하지만 여러 문법을 적용해볼 수 있는 문제들 위주로 선정
- 같은 문제라도 "반복문 버전"과 "문법 적용 버전"을 둘 다 짜보고 비교하는 걸 추천

#### 🗂️ 레벨 0

| 문제명 | 레벨 | 연습 문법 | 링크 | 체크 |
|--------|------|------|------|------|
| 배열 두 배 만들기 | Lv0 | 컴프리헨션 한 줄 | https://school.programmers.co.kr/learn/courses/30/lessons/120811 | [ ] |
| 머쓱이보다 키 큰 사람 | Lv0 | 컴프리헨션 + 조건, `sum()` | https://school.programmers.co.kr/learn/courses/30/lessons/120810 | [ ] |
| 자릿수 더하기 | Lv0 | `str()` 변환 + `sum()` + 컴프리헨션 | https://school.programmers.co.kr/learn/courses/30/lessons/120817 | [ ] |
| 짝수는 싫어요 | Lv0 | 컴프리헨션 + `range(시작,끝,간격)` | https://school.programmers.co.kr/learn/courses/30/lessons/120825 | [ ] |
| 정수 내림차순으로 배치하기 | Lv0 | `sorted(reverse=True)` + `join` | https://school.programmers.co.kr/learn/courses/30/lessons/120813 | [ ] |
| 최댓값 만들기 (1) | Lv0 | `sorted()` + 슬라이싱 | https://school.programmers.co.kr/learn/courses/30/lessons/120891 | [ ] |
| 문자열 반복해서 출력하기 | Lv0 | `*` 연산자 (반복문 없이) | https://school.programmers.co.kr/learn/courses/30/lessons/120821 | [ ] |
| 약수의 개수와 덧셈 | Lv0 | 컴프리헨션 + `sum()` | https://school.programmers.co.kr/learn/courses/30/lessons/120878 | [ ] |
| 가장 큰 수 | Lv0 | `sorted(key=lambda ...)` | https://school.programmers.co.kr/learn/courses/30/lessons/120894 | [ ] |
| 옹알이 (1) | Lv0 | `any()` / `in` 조건 | https://school.programmers.co.kr/learn/courses/30/lessons/120891 | [ ] |

#### 🗂️ 레벨 1

| 문제명 | 레벨 | 연습 문법 | 링크 | 체크 |
|--------|------|------|------|------|
| 완주하지 못한 선수 | Lv1 | `Counter` 차집합 | https://school.programmers.co.kr/learn/courses/30/lessons/42576 | [ ] |
| K번째수 | Lv1 | `sorted()` + 슬라이싱, 컴프리헨션 | https://school.programmers.co.kr/learn/courses/30/lessons/42748 | [ ] |
| 문자열 내 마음대로 정렬하기 | Lv1 | `sorted(key=lambda x: (x[n], x))` | https://school.programmers.co.kr/learn/courses/30/lessons/12915 | [ ] |
| 크레인 인형뽑기 게임 | Lv1 | `enumerate` + 스택 pop | https://school.programmers.co.kr/learn/courses/30/lessons/64061 | [ ] |
| 폰켓몬 | Lv1 | `set()` + `len()` + `min()` | https://school.programmers.co.kr/learn/courses/30/lessons/1845 | [ ] |
| 모의고사 | Lv1 | `enumerate` 순회 | https://school.programmers.co.kr/learn/courses/30/lessons/42840 | [ ] |
| 실패율 | Lv1 | `Counter` + `sorted(key=lambda x: x[1], reverse=True)` | https://school.programmers.co.kr/learn/courses/30/lessons/42889 | [ ] |
| 로또의 최고 순위와 최저 순위 | Lv1 | 컴프리헨션 + `zip` | https://school.programmers.co.kr/learn/courses/30/lessons/72410 | [ ] |
| 없는 숫자 더하기 | Lv1 | `set()` 차집합 + `sum()` | https://school.programmers.co.kr/learn/courses/30/lessons/86051 | [ ] |
| 3진법 뒤집기 | Lv1 | 컴프리헨션 + `join` + `int(x, 3)` | https://school.programmers.co.kr/learn/courses/30/lessons/68935 | [ ] |
| 캐릭터의 좌표 | Lv1 | `zip`으로 방향 딕셔너리 매핑 | https://school.programmers.co.kr/learn/courses/30/lessons/154538 | [ ] |
| 성격 유형 검사하기 | Lv2 | `Counter` + `zip` + `defaultdict` | https://school.programmers.co.kr/learn/courses/30/lessons/118666 | [ ] |

#### 🗂️ 레벨 1 — itertools (완전탐색/조합)

| 문제명 | 레벨 | 연습 문법 | 링크 | 체크 |
|--------|------|------|------|------|
| 소수 찾기 | Lv1 | `itertools.permutations` + 소수 판별 | https://school.programmers.co.kr/learn/courses/30/lessons/42839 | [ ] |
| 카펫 | Lv1 | 완전탐색 (약수 조합) | https://school.programmers.co.kr/learn/courses/30/lessons/42842 | [ ] |
| 로또의 최고 순위와 최저 순위 (재풀이) | Lv1 | `itertools.combinations`으로도 접근 가능 | https://school.programmers.co.kr/learn/courses/30/lessons/72410 | [ ] |
| 피자 나눠 먹기 (3) | Lv1 | 완전탐색 + 나머지 조건 | https://school.programmers.co.kr/learn/courses/30/lessons/120814 | [ ] |

#### 🗂️ 레벨 1 — 스택/큐

| 문제명 | 레벨 | 연습 문법 | 링크 | 체크 |
|--------|------|------|------|------|
| 크레인 인형뽑기 게임 | Lv1 | 스택 push/pop 패턴 | https://school.programmers.co.kr/learn/courses/30/lessons/64061 | [ ] |
| 같은 숫자는 싫어 | Lv1 | 스택으로 직전 값 비교 | https://school.programmers.co.kr/learn/courses/30/lessons/12906 | [ ] |
| 올바른 괄호 | Lv2 | 스택으로 짝 맞추기 | https://school.programmers.co.kr/learn/courses/30/lessons/12909 | [ ] |
| 기능개발 | Lv2 | 큐 + 진행률 시뮬레이션 | https://school.programmers.co.kr/learn/courses/30/lessons/42586 | [ ] |
