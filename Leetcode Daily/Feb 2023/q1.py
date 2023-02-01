def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1+str2 == str2+str1:
        return (str1+str2)[:gcd(len(str1),len(str2))]
    else:
        return ""
        