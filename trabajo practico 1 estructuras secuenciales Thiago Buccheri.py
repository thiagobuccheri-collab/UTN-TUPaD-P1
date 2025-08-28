#1
print ("Hola mundo") 
#2
nombre1= input("Ingrese su nombre: ") 
print (f"hola {nombre1}") 
#3
nombre=input("Ingrese su nombre: ") 
apellido= input("Ingrese su apellido: ") 
edad= input("Ingrese su edad: ") 
residencia= input("Ingrese su lugar de residencia: ") 
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") 
#4
import math 
print ("Este programa le va a permitir sacar el area y perimetro de un circulo") 
radio= float(input("Ingrese el radio del circulo ")) 
area= round(math.pi*radio**2 , 2) 
perimetro= round(2*math.pi*radio ,2) 
print(f"El area es de {area} y el perimetro es de {perimetro}") 
#5
print("El programa le va a permitir sacar la hora con los segundos ingresados.") 
segundos= int(input("Ingrese una cantidad de segundos: ")) 
horas=round(segundos/ 3600) 
minutos=round((segundos%3600)/60) 
seg= round((segundos%3600)%60) 
print (f"{segundos} segundos son {horas} horas y {minutos} minutos con {seg} segundos") 
#6
print("El programa le va a permitir saber la tabla de multiplicar del numero ingresado") 
num= int(input("Ingrese un numero: ")) 
ite=1 
for ite in range (0, 11, 1): 

    print (num*ite) 
#7
print("El programa le va a permitir saber la suma, resta, multiplicacion y division de 2 numeros") 
num1= int(input("Ingrese su primero numero: ")) 
num2= int(input("Ingrese su segundo numero: ")) 
suma= num1 + num2 
resta= num1 - num2 
multiplicacion= num1 * num2 
division= num1 / num2 
print(f"La suma de {num1} y {num2} es {suma}") 
print(f"La resta de {num1} y {num2} es {resta}") 
print(f"La multiplicacion de {num1} y {num2} es {multiplicacion}") 
print(f"La division de {num1} y {num2} es {division}") 
#8
print("El programa le va a permitir sacar la masa corporal") 
peso= float(input("Ingrese su peso en kg: ")) 
altura= float(input("Ingrese su altura en m: ")) 
masa= round(peso / altura**2 ,2) 
print (f"La masa corporal es de {masa}") 
#9
print("Convertidor de grados celcius a fahrenheit") 
celcius= float(input("Ingrese los grados celcius: ")) 
fahrenheit= (9/5) * celcius + 32 
print (f"{celcius}° grados celcius son {fahrenheit}° grados fahrenheit") 
#10
print("Promedio") 
num1= int(input("Ingrese su primer numero: ")) 
num2= int(input("Ingrese su segundo numero: ")) 
num3= int(input("Ingrese su tercer numero: ")) 
promedio= round((num1 + num2 + num3) / 3) 
print(f"El promdio de los 3 numeros es {promedio}")