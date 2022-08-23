def ComprobarArray(Array,Base):
  BaseD = Base-1
  for i in range(len(Array)):
    if Array[i]>BaseD:
      return False
  return True
  
def PasarArray(string):
  Array=[0,]*len(string)
  for i in range(len(string)):
    try:
      Array[i]=int(string[i])
    except ValueError:
      if ord(string[i])>64 and ord(string[i])<91:
        Array[i]=ord(string[i])-55
      elif ord(string[i])>96 and ord(string[i])<123:
        Array[i]=ord(string[i])-87
      else:
        Array[i]=100
  return Array
  
def ConvertirDecimal(Base,ArrayNumero):
  Numero=0
  for i in range(len(ArrayNumero)):
    Numero=Numero+((Base**i)*ArrayNumero[(len(ArrayNumero)-1)-i])
  return Numero
def Decimal_Base(Numero,Base):
  Array=[]
  while True:
    Array.append(int(Numero%Base))
    Numero=(Numero/Base)-((Numero%Base)/Base)
    if Numero<Base:
      Array.append(int(Numero))
      break
  Array=Array[::-1]
  return Array
  
def Mostrar_Resultados(ArrayF):
  print ("El el numero convertido es ", end="")
  for i in range(len(ArrayF)):
    if ArrayF[i]!=0 or i!=0:
      if ArrayF[i]>9:
        ArrayF[i]=chr(ArrayF[i]+55)
      print(ArrayF[i], end="")
    

while True:
  BaseM=int(input("Ingrese base inicial: "))
  if BaseM>16 or BaseM<2:
    print("La base que colocaste no esta entre 2 y 16")
  else:
    break

while True:
  Numero=str(input("Ingrese numero en la base inicial: "))
  Lista=PasarArray(Numero)
  if ComprobarArray(Lista,BaseM)==False:
    print("El numero no pertenece la base")
  else:
    break

while True:
  BaseN=int(input("Ingresa la base de cambio: "))
  if BaseM>16 or BaseM<2:
    print("La base que colocaste no esta entre 2 y 16")
  else:
    break

Resultado=Decimal_Base(int(ConvertirDecimal(BaseM,Lista)),BaseN)
Mostrar_Resultados(Resultado)

print("\n")
