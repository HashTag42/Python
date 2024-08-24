def cleanStr(str, ignorelist):
    result = ""
    for i in str:
        if i not in ignorelist:
            result = result + i.lower()
    return result

def reverseStr(str):
    result = ""
    l = len(str)
    for i in range(l):
        result = result + str[l-i-1]
    return result

def is_palindrome(teststr):
    # Your code goes here.
    ignorelist = "!?'., "
    cs = cleanStr(teststr, ignorelist)
    rs = reverseStr(cs)
    # print(teststr, "->", cs, "->", rs)
    if cs == rs:
        return True
    else:
        return False