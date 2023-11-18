#Hora de las comidas
hora = input("Por favor ingrese la hora en formmato HH:MM :")
horas, minutos = map(int, hora.split(":"))
hora_float = (horas + minutos/60)

if 7.0<=hora_float <= 8.0:
    print("Hora de desayunar")
elif 12.0<=hora_float<=13.0:
    print("Hora de almorzar")
elif 18.0<=hora_float<= 19.0:
    print("Hora de cenar")
else: 
    print("No es hora de comer")