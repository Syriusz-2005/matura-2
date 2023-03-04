
def silnia(n):
    if n == 1: return 1
    return silnia(n - 1) * n



def CzySilna(n = 7):
    if n == 0: return False
    for i in range(1, n):
        if silnia(i) > n: break
        if silnia(i) == n: return True

    return CzySilna(n - 1)


print(CzySilna(120))
print(CzySilna(7))
print(CzySilna(4))
print(CzySilna(5))
print(CzySilna(6))
print(CzySilna(9))
print(CzySilna(25))


print(silnia(4))