diff --git a/reverse_string.py b/reverse_string.py
index 46c4badbfee27ac642693630f5ba5c8e6754aacd..a614d442469bf5f4ab3312630d7b8dfb26efdcc6 100644
--- a/reverse_string.py
+++ b/reverse_string.py
@@ -1,13 +1,16 @@
-# 문자열을 거꾸로 뒤집어 출력하는 프로그램
+"""반복적으로 문자열을 입력받아 뒤집어 출력하는 프로그램."""
 
-# 문자열 입력 받기
-text = input("문자열을 입력하세요: ")
+def main() -> None:
+    """문자열을 입력받아 거꾸로 출력하고 'exit' 입력 시 종료한다."""
+    while True:
+        text = input("문자열을 입력하세요 (종료하려면 'exit' 입력): ")
 
-# 문자열 뒤집기
-reversed_text = text[::-1]
+        if text.lower() == "exit":
+            print("프로그램을 종료합니다.")
+            break
 
-# 결과 출력
-print("뒤집은 문자열:", reversed_text)
+        print("뒤집은 문자열:", text[::-1])
 
-# 창이 바로 닫히지 않게 하기
-input("엔터 키를 누르면 프로그램을 종료합니다...")
+
+if __name__ == "__main__":
+    main()
