# 공백 제거
#1. 문자열 앞 뒤 공백 제거
#    -> strip
s = ' x '
print(s.strip()) # => 'x'
#2. 왼쪽 문자열만 제거 -> s.lstrip()
#3. 오른쪽 문자열만 제거 -> s.rstrip()

#정규식 사용
"""
참고 :
https://wikidocs.net/4308

# 문자열 추출 참고 
https://ponyozzang.tistory.com/279?category=800537

#자주쓰이는 사용자 정보 정규식
https://developsd.tistory.com/55

import re
- match(pattern, string) || 문자열의 시작부분부터 매칭이 되는지 검색.

-  search(pattern, string) || 문자열에 패턴과 매칭되는 곳이 있는지 검색.

-  findall(pattern, string) || 정규식과 매치되는 모든 문자열을 리스트로 반환.

-  finditer(pattern, string) ||  정규식과 매치되는 모든 문자열을 iterator 
"""
"""
자주쓰이는 정규식
1) 숫자만 : ^[0-9]*$
2) 영문자만 : ^[a-zA-Z]*$
3) 한글만 : ^[가-힣]*$
4) 영어 & 숫자만 : ^[a-zA-Z0-9]*$
5) E-Mail : ^[a-zA-Z0-9]+@[a-zA-Z0-9]+$
6) 휴대폰 : ^01(?:0|1|[6-9]) - (?:\d{3}|\d{4}) - \d{4}$
7) 일반전화 : ^\d{2,3} - \d{3,4} - \d{4}$
8) 주민등록번호 : \d{6} \- [1-4]\d{6}
9) IP 주소 : ([0-9]{1,3}) \. ([0-9]{1,3}) \. ([0-9]{1,3}) \. ([0-9]{1,3})

"""

"""
랜덤 값 생성
http://pythonstudy.xyz/python/article/509-%EB%82%9C%EC%88%98-random
"""