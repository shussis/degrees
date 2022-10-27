#ПЕРЕВОД ГРАДУСОВ

celsius = int(input())

def conv(c):
    gr = (9/5 * celsius + 32)
    return gr

fahrenheit = conv(celsius)
print(fahrenheit)