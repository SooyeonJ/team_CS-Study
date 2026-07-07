# Programmers
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

## 📚 문법별 문제 정리
- 레벨이 아니라 **실제로 사용하는 핵심 문법 기준**으로 분류
- 문제명에 레벨 표기 (Lv0 / Lv1 / Lv2)
- 각 표는 쉬운 문제가 위쪽에 오도록 정렬

#### 🗂️ lambda (sorted/sort key)
> 실제로 `key=lambda x: 기준` 형태가 필요한 문제만

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [문자열 내 마음대로 정렬하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12915) | `sorted(key=lambda x: (x[n], x))` — 다중 기준 | [x] |
| 2 | [실패율 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42889) | `sorted(key=lambda x: -x[1])` | [ ] |
| 3 | [가장 큰 수 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42746) | `sorted(key=lambda x: x*3, reverse=True)` | [x] |
| 4 | [저울 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/154051) | `sorted(key=lambda x: -x)` | [ ] |

#### 🗂️ Counter (개수 세기)

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [완주하지 못한 선수 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | `Counter` 차집합 | [ ] |

#### 🗂️ set 연산

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [폰켓몬 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/1845) | `set()` + `len()` + `min()` | [ ] |
| 2 | [없는 숫자 더하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/86051) | `set()` 차집합 + `sum()` | [ ] |

#### 🗂️ sorted (lambda 없이 기본 정렬)

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [정수 내림차순으로 배치하기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120813) | `sorted(reverse=True)` + `join` | [ ] |
| 2 | [최댓값 만들기 (1) (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120891) | `sorted()` + 슬라이싱 | [ ] |
| 3 | [K번째수 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42748) | `sorted()` + 슬라이싱, 컴프리헨션 | [ ] |
| 4 | [예산 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12982) | `sorted()` + 누적합 | [ ] |

#### 🗂️ enumerate / zip

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [모의고사 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42840) | `enumerate` 순회 | [ ] |
| 2 | [캐릭터의 좌표 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/154538) | `zip`으로 방향 딕셔너리 매핑 | [ ] |
| 3 | [로또의 최고 순위와 최저 순위 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/72410) | 컴프리헨션 + `zip` | [x] |

#### 🗂️ 컴프리헨션 (Lv0 기본기)

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [배열 두 배 만들기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120811) | 컴프리헨션 한 줄 | [ ] |
| 2 | [문자열 반복해서 출력하기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120821) | `*` 연산자 (반복문 없이) | [ ] |
| 3 | [머쓱이보다 키 큰 사람 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120810) | 컴프리헨션 + 조건, `sum()` | [ ] |
| 4 | [짝수는 싫어요 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120825) | 컴프리헨션 + `range(시작,끝,간격)` | [ ] |
| 5 | [자릿수 더하기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120817) | `str()` 변환 + `sum()` + 컴프리헨션 | [ ] |
| 6 | [옹알이 (1) (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120891) | `any()` / `in` 조건 | [ ] |
| 7 | [약수의 개수와 덧셈 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120878) | 컴프리헨션 + `sum()` | [ ] |
| 8 | [3진법 뒤집기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/68935) | 컴프리헨션 + `join` + `int(x, 3)` | [ ] |

#### 🗂️ itertools (완전탐색/조합)

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [피자 나눠 먹기 (3) (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/120814) | 완전탐색 + 나머지 조건 | [ ] |
| 2 | [소수 찾기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42839) | `itertools.permutations` + 소수 판별 | [ ] |
| 3 | [카펫 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42842) | 완전탐색 (약수 조합) | [ ] |

#### 🗂️ 스택/큐

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [같은 숫자는 싫어 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12906) | 스택으로 직전 값 비교 | [ ] |
| 2 | [크레인 인형뽑기 게임 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/64061) | 스택 push/pop 패턴 | [ ] |
| 3 | [올바른 괄호 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/12909) | 스택으로 짝 맞추기 | [ ] |
| 4 | [기능개발 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42586) | 큐 + 진행률 시뮬레이션 | [ ] |

#### 🗂️ 해시(딕셔너리) — Counter로 해결 안 되는 것
- Counter는 "개수"만 다룰 수 있고, "순서 / 관계 / 조합"이 필요한 문제는 Dict로 풀어야 함

| 순서 | 문제명 | 핵심 문법 | 체크 |
|------|--------|------|------|
| 1 | [가장 가까운 같은 글자 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/142086) | 해시 + 문자열 | [ ] |
| 2 | [달리기 경주 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/178871) | 해시 + 시뮬레이션 | [ ] |
| 3 | [신고 결과 받기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/92334) | 해시 + 집합 | [ ] |
| 4 | [성격 유형 검사하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/118666) | 해시 + `Counter` + `zip` + `defaultdict` | [ ] |
| 5 | [전화번호 목록 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42577) | 해시 + 문자열 | [ ] |
| 6 | [의상 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42578) | 해시 + 조합 | [ ] |
