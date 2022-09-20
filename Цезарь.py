alfavit = 'abcdefghijklmnopqrstuvwxyz'
key = 2
n = len(alfavit)
 
text = input("Введите слово: ")
 
result = ""
for symbol in text:
    index1 = alfavit.index(symbol)
    index2 = index1+key
    if index2>n:
        index2=index2-n
    symbol_2 = alfavit[index2]
    result = result + symbol_2
 
print("Результат: ",result)    
