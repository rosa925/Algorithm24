def find_substring(text, substring):
    # 주어진 텍스트에서 부분 문자열의 인덱스를 반환
    # 텍스트에서 부분 문자열을 찾지 못한 경우 -1을 반환
    
    # 텍스트와 부분 문자열의 길이
    text_length = len(text)
    substring_length = len(substring)
    
    # 텍스트의 각 문자를 반복하면서 부분 문자열과 비교
    for i in range(text_length - substring_length + 1):
        # 텍스트에서 현재 위치부터 부분 문자열과 같은지 확인
        if text[i:i+substring_length] == substring:
            # 부분 문자열을 찾았으므로 해당 인덱스를 반환
            return i
    # 부분 문자열을 찾지 못했으므로 -1을 반환
    return -1

# 예제
text = "Hello, world!"
substring = "world"
index = find_substring(text, substring)
if index != -1:
    print(f"부분 문자열 '{substring}'을(를) 찾았습니다. 인덱스: {index}")
else:
    print(f"부분 문자열 '{substring}'을(를) 찾을 수 없습니다.")
