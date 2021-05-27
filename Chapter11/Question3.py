s = input()

zeroCount = s.count("10")
oneCount = s.count("01")
if s[:1] == "0":
    zeroCount += 1
else:
    oneCount += 1

result = min(zeroCount, oneCount)
print(result)