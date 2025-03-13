#1. Привести строку к нижнему регистру.
#2. Удалить все пробелы (если требуется).
#3. Сравнить исходную строку с перевернутой.

def is_palindrome(s):
    # Очищаем строку от небуквенно-цифровых символов и приводим к нижнему регистру
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    # Сравниваем очищенную строку с ее обратным вариантом
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))                         # True
print(is_palindrome("Madam"))                           # True
print(is_palindrome("Hello"))                           # False
print(is_palindrome("zerocoder"))                       # False