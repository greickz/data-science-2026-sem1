lista = [2,1,3,4,5]
par = []
impar = []

for num in lista:
    if num % 2 == 0:
        par.append(num)        
    else:
        impar.append(num)
print(f"Par: {par}, Impar: {impar}")     