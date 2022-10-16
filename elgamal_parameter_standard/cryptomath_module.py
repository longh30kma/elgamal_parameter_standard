def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1: #nếu ước chung lớn nhất a và m là khác 1 thì bỏ
        return None
    u1, u2, u3 = 1, 0, a #gán u1 =1 u2 = 0 u3 = a
    v1, v2, v3 = 0, 1, m # tương tự bên trên
    while v3 != 0: #trong khi v3 khác 0
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q *v3), v1, v2, v3
    return u1 % m     