'''
* 표준 모듈 time

- time 모듈은 시간 관련 기능들을 제공합니다.

- 대표적인 함수는 time()인데, 이 함수는 현재 시간을
1970년 1월 1일 자정을 기준으로 현재까지 경과한
시간을 초단위로 표현한 유닉스 시간을 반환합니다.
'''

import time as t
print(t.time())

# time 함수를 이용한 프로그램 속도 측정 테스트
start = t.time()

sum = 0
for n in range(5000000):
    sum += n

end = t.time()

print(f'프로그램 실행 속도: {end - start:0.4f}초')

'''
- time 모듈의 sleep()함수는 cpu를 지정한 시간만큼
잠재워 아무것도 하지 않고 시간을 끌게 합니다.
'''
# print("재밌는 문제를 준비했어용~~")
# t.sleep(5)
# print("대학생이 힘이 센 이유는??")
# t.sleep(20)
# print("개강하니까~~~")
# t.sleep(3)
# print("으엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

# 페이지가 로딩이 되어야 코드가 실행되도록 해야 하므로
# 지연을 시켜야 함(크롤링 시)

'''
* 표준 모듈 datetime

- 운영체제의 현재 시간과 날짜 정보를 파이썬 내부로 읽어오는
기능을 제공하는 모듈입니다.
'''
from datetime import datetime

# 오늘 날짜와 현재 시간 정보를 가지고 있는 객체 리턴
d = datetime.today()
print(d)
# print(type(d))
print(str(d).split()[0].split('-'))
li = str(d).split()[0].split('-')
print(f'year: {li[0]}, month: {li[1]}, day: {li[2]}')
print(f'지금은 {d.year}년 {d.month}월 {d.day}일 {d.hour}시 {d.minute}분 {d.second}초 입니다.')

