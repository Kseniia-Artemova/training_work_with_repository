def is_palindrome(word):
    prepared_string = list(word.replace(" ", "").strip().lower())
    if prepared_string[:] == prepared_string[::-1]:
        return True
    return False


try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")