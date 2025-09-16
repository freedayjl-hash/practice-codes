# 문자열을 여러 번 입력받아 거꾸로 뒤집어 출력하는 프로그램
# 'exit'를 입력하면 프로그램 종료

while True:
    text = input("문자열을 입력하세요 (종료하려면 'exit' 입력): ")
    
    if text.lower() == "exit":
        print("프로그램을 종료합니다.")
        break
    
    reversed_text = text[::-1]
    print("뒤집은 문자열:", reversed_text)
