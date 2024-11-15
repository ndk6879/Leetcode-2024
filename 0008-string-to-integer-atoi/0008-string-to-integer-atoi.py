class Solution:
    def myAtoi(self, s):
        i, n = 0, len(s)
        sign = 1
        result = 0
        started = False  # 숫자 시작 여부를 추적하기 위한 변수

        while i < n:
            # 1. 공백 제거 (아직 숫자가 시작되지 않았을 때만)
            if s[i] == ' ' and not started:
                i += 1
                continue
            
            # 2. 부호 확인 (아직 숫자가 시작되지 않았을 때만)
            if s[i] in ('+', '-') and not started:
                sign = -1 if s[i] == '-' else 1
                started = True  # 이제 숫자가 시작되었다고 표시
                i += 1
                continue
            
            # 3. 숫자 추출
            if s[i].isdigit():
                result = result * 10 + int(s[i])
                started = True  # 숫자 시작을 기록
            else:
                break  # 숫자가 아닌 문자가 나오면 종료
            
            i += 1

        # 4. 정수 범위 제한
        result *= sign
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result