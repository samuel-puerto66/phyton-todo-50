def es_primo(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def primos_hasta(n):
    return [i for i in range(2, n+1) if es_primo(i)]

if __name__ == "__main__":
    print(primos_hasta(30))
