print("Sequência de Fibonacci")
termos = int(input('Quantos termos mostrar?: '))
pt = 1
st = 1
f = 0
i = 0
while i < termos - 1:
     i = i + 1
     if i == 1:
         print(pt)
         print(st)
     else:    
         f = pt + st 
         print (f)
         pt = st
         st = f
    	
    
    
