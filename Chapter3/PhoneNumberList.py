phone_book = ["119", "97674223", "1195524421"]
answer = True

phone_book.sort()

for i in range(len(phone_book) - 1):

    if len(phone_book) == 1:
        break;

    str1 = ''
    str2 = ''
    if len(phone_book[i]) >= len(phone_book[i+1]):
        str1 = phone_book[i+1]
        str2 = phone_book[i]
    else:
        str1 = phone_book[i]
        str2 = phone_book[i+1]

    if str1 == str2[:len(str1)]:
        answer = False