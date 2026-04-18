
num = int(input('Digite um número: '))
def fatorial(num):
    r = 1
    for x in range(1, num + 1):
        r *= x
    return(r)
print(fatorial(num))