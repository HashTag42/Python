import palindrome

def test_palyndrome(str):
    print(f"Is [{str}] a palindrome? = {palindrome.is_palindrome(str)}")

test_palyndrome("radar!")
test_palyndrome("Hello")
