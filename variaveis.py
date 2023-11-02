nome = "Mateus"
sobrenome = "Henrique"
idade = 18
altura = 1.87
estudante = True
print(nome + " " + sobrenome)
print(type(nome))       #str
print(type(idade))      #int
print(type(altura))     #float
print(type(estudante))  #boll

x = 4       # x é int
print(type(x))
x = "Sally" # x agora é string
print(type(x))

a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0

#consigo atribuit varios valores

f, g, h , = 'Banana','Maça',"Pera"
print(f,g,h)    #f = Banana   g = Maça  h = Pera
f = g = h  = 'Banana'
print(f,g,h)    # f recebe g que recebe h  = 'Banana

#descompactando


frutas = ['Maça','Pera','Uva']

a, b, c = frutas
print(a)  #Maça
print(b)  #Pera
print(c)  #Uva


#variaveis globais

x = "incrivel"

def myfunc():
  x = "fantastico"
  print("Python é " + x)     #fantastico

myfunc()

print("Python é " + x)     #incrivel

#palavra chave global torna global

def outraFunc():
    global x
    x = "Palavra"  
    outraFunc()     
  
print(x) 

