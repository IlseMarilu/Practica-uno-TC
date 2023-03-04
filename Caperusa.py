#TITULO: Contero de letras, parejas y tercias
#Descripción: En este codigo lo que nos solicitarón es hacer, un conteo de letras en un archivo 
#txt en tres diferentes idiomas ,contar cuantas letras tiene, parejas ytercias,de igual forma
#sacar la probabilidad y por ende la entropia. 
#UEA : Teoria de la decodificación 
#Autor: López Elías Ilse Marilu     2203026744
#Docente: Mario Alberto Ramirez Reyna 


import funciones
import re 

######################################################################
print("Ingrese el libro en formato .txt")
txt = input()

# Se abre el .txt y se asigna a una variable llamada libro para ser leído
with open(txt, encoding = "utf-8") as libro:
    a= libro.read()   # La variable 'a', leemos los caracteres de 'libro' 
    b = funciones.sinacento(a) # La variable b le quitamos los acentos


a = input("Que letra del texto te gustaria contar: ")
print("El numero de letra es:", b.count(a))#Cuenta el numero de letra que existe en el texto, con la funcion count

#Empieza la funcion para contar los espacios del texto
c = 0  

for i in b:
    if i == " ":
        c += 1

print("Numero de espacios del texto:", c ,"\n")

###########################################################################
#Codigo para contar el numero de todas la letras existentes en el texto.

patron = '[\W]+'  #Se quitan espacios y signos de puntuación
regex = re.compile(patron) #Secuencia de caracteres que forma un patron de busqueda

out = regex.sub("",b)#.sub se remplazan coincidencias con una cadena 
#print(out)

conteo  = {"espacios":c}  #Se crea un diccionario 

for letra in out:      #Ciclo for para el conteo de cada letra 
    if letra not in conteo:
        conteo[letra] = 1
    else: 
            conteo[letra] +=1

print("El conteo de las letras del texto son:")
for k, v in conteo.items(): #.items devuelve un objeto de vista (clave- valor)
 print("{}:{}".format(k, v))
#print(conteo)

############################PROBABILIDAD#####################################
#Recorrer diccionario 
e = 0
for valor in conteo.values():   #Se recorre el diccionario solo para tomar el valor conteo de las letras 
    #print(valor), verificar que lo que se imprima si es lo que busco hacer
    e = e+valor #Se hace la suma de todas las letras,para poder realizar su prbabilidad
print("\nLa suma de todas las letras es:" ,e, "\n")


for letra in conteo:
    conteo[letra] = (conteo[letra])/e #Operación de probabilidad.

    print("Probabilidad de las letras\t", end="")

    print(f"{conteo[letra]:.5f} ") #Se imprimen todas la probabilidades de cada una de las letras 
    print(f"La informacion es:\t{funciones.informacion(conteo[letra])}")
    #Se manda a llamar el scrip funciones entropia para realizar la operacion.

print("\nProbabilidad de la letra que solicitaste anteriormente ", b.count(a)/e ,"=", b.count(a)*100/e,"%" )

####################Entropia###########################

# El diccionario se hace una lista, para sacar la entropia de todo el conteo de letras.
lista_ejemplo = list(conteo.values())
entropia_lista_ejemplo = funciones.entropy(lista_ejemplo)
print("La entropía de la lista es:", entropia_lista_ejemplo)

##########Contar las parejas y tercias de letras#############

patron1 = r'[^\w\s]+' #Se colocan los espacios al texto quitando los signos de puntuación
regex = re.compile(patron1) 

out1 = regex.sub('',b)
#print(out1)

parejas = {}#Diccionario parejas
tercias = {}#Diccionario tercias 

for i in range(len(out1)-1):  #Función para contar las parejas de todo el texto
    pareja = out1[i:i+2]
    if pareja in parejas:
        parejas[pareja] += 1
    else:
        parejas[pareja] = 1
    
    if i < len(out1)-2:     #Funcion para contar las tecias de todo el texto 
        tercia = out1[i:i+3]
        if tercia in tercias:
            tercias[tercia] += 1
        else:
            tercias[tercia] = 1

# Imprimir los resultados de la parejas
a= input ("Que pareja del texto te gustaria contar:")
print("El numero de la pareja que esxiste en el texto es: ", out1.count(a))
print("Probabilidad de la pareja que solicitaste anteriormente ", out1.count(a)*100/e)


############ENTROPIA#################################
#Esta entropia es de todas las parejas
lista_ejemplo = list(parejas.values())
entropia_lista_ejemplo = funciones.entropy(lista_ejemplo)
print("La entropía de todas las parejas es:", entropia_lista_ejemplo)


# Imprimir resultados de las tercias
a = input("Que tercia del texto te gustaria contar:")
print("El numero de la tercia que esxiste en el texto es: ", out1.count(a))
print("Probabilidad de la pareja que solicitaste anteriormente ", out1.count(a)*100/e) 


############ENTROPIA#######################
#Entropia de todas las tercias
lista_ejemplo = list(tercias.values())
entropia_lista_ejemplo = funciones.entropy(lista_ejemplo)
print("La entropía de todas las tercias es:", entropia_lista_ejemplo)



