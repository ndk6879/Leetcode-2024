class Solution:
    def myAtoi(self, s: str) -> int:
        # 초기 설정
        i, n = 0, len(s)
        sign = 1
        result = 0
        
        # 1. 공백 제거
        while i < n and s[i] == ' ':
            i += 1

        # 2. 부호 확인
        if i < n and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. 숫자 추출
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])  # 현재 숫자를 결과에 추가
            i += 1

        # 4. 정수 범위 제한
        result *= sign
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result
