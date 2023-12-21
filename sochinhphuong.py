v = int(input())
a = int(v**0.5)**2
b = int(v**0.5 + 1)**2 
print(a if v - a < b - v else b)