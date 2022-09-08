
def addBinary(a, b):
    res = ''
    a = a[::-1]
    b = b[::-1]
    carry = 0
    for i in range(max(len(a), len(b))):
        da = int(a[i]) if i < len(a) else 0
        db = int(b[i]) if i < len(b) else 0

        total = da + db + carry
        chr = str(total % 2)
        res = chr + res
        carry = total//2

    if carry == 1:
        res = "1" + res
    return res


print(addBinary('11', '1'))
