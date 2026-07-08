# Programmers

This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

## 📚 문법별 문제 정리

* 레벨이 아니라 **실제로 사용하는 핵심 문법 기준**으로 분류
* 문제명에 레벨 표기 (Lv0 / Lv1 / Lv2 / Lv3)
* 각 표는 쉬운 문제가 위쪽에 오도록 정렬

---

## 🗂️ lambda

| 순서 | 문제명                                                                               | 핵심 문법                                     | 체크  |
| -- | ----------------------------------------------------------------------------------- | ----------------------------------------- | --- |
| 1  | [문자열 내 마음대로 정렬하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12915) | `sorted(key=lambda x: (x[n], x))`         | ✅   |
| 2  | [실패율 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42889)             | `sorted(key=lambda x: -x[1])`             | ❌   |
| 3  | [가장 큰 수 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42746)          | `sorted(key=lambda x: x*3, reverse=True)` | [x] |

---

## 🗂️ sorted

| 순서 | 문제명                                                                                | 핵심 문법                             | 체크  |
| -- | -------------------------------------------------------------------------------------- | --------------------------------- | --- |
| 1  | [최댓값 만들기 (1) (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120847)   | `sorted()` + 슬라이싱                 | [ ] |
| 2  | [정수 내림차순으로 배치하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12933) | `sorted(reverse=True)` + `join()` | [ ] |
| 3  | [K번째수 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42748)           | `sorted()` + 슬라이싱                 | [ ] |

---

## 🗂️ Counter

| 순서 | 문제명                                                                            | 핵심 문법         | 체크  |
| -- | ------------------------------------------------------------------------------ | ------------- | --- |
| 1  | [완주하지 못한 선수 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | `Counter` 차집합 | [ ] |

---

## 🗂️ set 연산

| 순서 | 문제명                                                                                  | 핵심 문법                       | 체크  |
| -- | ------------------------------------------------------------------------------------- | --------------------------- | --- |
| 1  | [폰켓몬 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/1845)               | `set()` + `len()` + `min()` | [ ] |
| 2  | [없는 숫자 더하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/86051)        | `set()` 차집합 + `sum()`       | [ ] |
| 3  | [로또의 최고 순위와 최저 순위 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/77484) | `set()` + `count()`         | [x] |

---

## 🗂️ enumerate

| 순서 | 문제명                                                                      | 핵심 문법         | 체크  |
| -- | -------------------------------------------------------------------------- | ------------- | --- |
| 1  | [모의고사 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/42840) | `enumerate()` | [ ] |

---

## 🗂️ 컴프리헨션

| 순서 | 문제명                                                                                | 핵심 문법                         | 체크  |
| -- | -------------------------------------------------------------------------------------- | ----------------------------- | --- |
| 1  | [배열 두 배 만들기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120809)    | 리스트 컴프리헨션                     | [ ] |
| 2  | [문자열 반복해서 출력하기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/181950) | `*` 연산자                       | [ ] |
| 3  | [머쓱이보다 키 큰 사람 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120585)  | 컴프리헨션 + 조건                    | [ ] |
| 4  | [짝수는 싫어요 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120813)       | 컴프리헨션 + `range()`             | [ ] |
| 5  | [자릿수 더하기 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120906)       | `sum(int(x) for x in str(n))` | [ ] |
| 6  | [옹알이 (1) (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120956)       | `any()` + 문자열                 | [ ] |
| 7  | [약수의 개수와 덧셈 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/77884)     | 컴프리헨션 + `sum()`               | [ ] |
| 8  | [3진법 뒤집기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/68935)        | `join()` + `int(..., 3)`      | [ ] |

---

## 🗂️ 스택 / 큐

| 순서 | 문제명                                                                             | 핵심 문법         | 체크  |
| -- | ----------------------------------------------------------------------------------- | ------------- | --- |
| 1  | [같은 숫자는 싫어 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12906)   | 스택            | [ ] |
| 2  | [크레인 인형뽑기 게임 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/64061) | 스택 `push/pop` | [ ] |
| 3  | [올바른 괄호 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/12909)      | 스택            | [ ] |
| 4  | [기능개발 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42586)        | 큐 / 시뮬레이션     | [ ] |

---

## 🗂️ 해시(Dictionary)

| 순서 | 문제명                                                                               | 핵심 문법              | 체크  |
| -- | --------------------------------------------------------------------------------------- | ------------------ | --- |
| 1  | [가장 가까운 같은 글자 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/142086) | `dict`             | [ ] |
| 2  | [달리기 경주 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/178871)       | `dict` + 시뮬레이션     | [ ] |
| 3  | [신고 결과 받기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/92334)      | `dict` + `set`     | [ ] |
| 4  | [성격 유형 검사하기 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/118666)   | `defaultdict(int)` | [ ] |
| 5  | [전화번호 목록 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42577)       | 해시 + 문자열           | [ ] |
| 6  | [의상 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42578)            | 해시 + 조합            | [ ] |

---

## 🗂️ 그리디

| 순서 | 문제명                                                                    | 핵심 문법    | 체크  |
| -- | -------------------------------------------------------------------------- | -------- | --- |
| 1  | [예산 (Lv1)](https://school.programmers.co.kr/learn/courses/30/lessons/12982) | 정렬 + 누적합 | [ ] |
| 2  | [저울 (Lv3)](https://school.programmers.co.kr/learn/courses/30/lessons/42886) | 정렬 + 그리디 | [ ] |

---

## 🗂️ 구현 / 완전탐색

| 순서 | 문제명                                                                               | 핵심 문법                            | 체크  |
| -- | ----------------------------------------------------------------------------------------- | -------------------------------- | --- |
| 1  | [피자 나눠 먹기 (3) (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120816) | 수학                               | [ ] |
| 2  | [캐릭터의 좌표 (Lv0)](https://school.programmers.co.kr/learn/courses/30/lessons/120861)      | 구현 + 딕셔너리                        | [ ] |
| 3  | [카펫 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42842)            | 약수 탐색                            | [ ] |
| 4  | [소수 찾기 (Lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/42839)         | `itertools.permutations` + 소수 판별 | [ ] |
