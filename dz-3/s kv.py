n = int(input())
if n > 100:
    print("Нельзя числа такие")
    quit()
s = 0
for i in range(1 , n+1):
    s+=i**2
print(s)