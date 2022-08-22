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
      if string[i] == "A" or string[i] == "a":
        Array[i]=10
      elif string[i] == "B" or string[i] == "b":
        Array[i]=11
      elif string[i] == "C" or string[i] == "c":
        Array[i]=12
      elif string[i] == "D" or string[i] == "d":
        Array[i]=13
      elif string[i] == "E" or string[i] == "e":
        Array[i]=14
      elif string[i] == "F" or string[i] == "f":
        Array[i]=15
      else:
        Array[i]=16
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
    if ArrayF[i] == 10:
      ArrayF[i]="A"
    if ArrayF[i] == 11:
      ArrayF[i]="B"
    if ArrayF[i] == 12:
      ArrayF[i]="C"
    if ArrayF[i] == 13:
      ArrayF[i]="D"
    if ArrayF[i] == 14:
      ArrayF[i]="E"
    if ArrayF[i] == 15:
      ArrayF[i]="F"
    if ArrayF[i]!=0 or i!=0:
      print(ArrayF[i], end="")

while True:
  BaseM=int(input("Ingrese base inicial: "))
  Numero=str(input("Ingrese numero en la base inicial: "))
  Lista=PasarArray(Numero)

  if BaseM>16 or BaseM<2:
    print("La base que colocaste no esta entre 2 y 16")
  elif ComprobarArray(Lista,BaseM)==False:
    print("El numero no pertenece la base")
  else:
    break
BaseN=int(input("Ingresa la base de cambio: "))

Resultado=Decimal_Base(int(ConvertirDecimal(BaseM,Lista)),BaseN)
Mostrar_Resultados(Resultado)

print("\n")
