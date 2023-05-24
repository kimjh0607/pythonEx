var = '' #boolean타입으로는 True
print(var)
print(type(var))

var = bool(var)
print(var)
print(type(var))

var = ' ' #boolean타입으로는 False
print(var)
print(type(var))

var = bool(var)
print(var)
print(type(var))

var1 = 'True'
var2 = 'False'
print(var1)
print(var2)
print(type(var1))
print(type(var2))

var1 = bool(var1)
var2 = bool(var2)
print(var1)
print(var2)
print(type(var1))
print(type(var2))

print(var1+var2)

var1 = 'True'
var2 = 'False'

var1 = bool(var1)
var2 = bool(var2)
print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1 / var2)