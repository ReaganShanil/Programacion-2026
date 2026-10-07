"""Microreto: el portero del café."""

energia = int(input('Cuanta energia tienes de 0-100?: '))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == 'si'
     
mensaje = "Completa las reglas del portero."

#<30 energia y no traigo cafe
# si traigo un 30  o mas de energia o tengo cafe (dejeme pasar)
# cualquier otro escenario, portero confundido, revise las respuestas
# TODO: usa and para detectar energíabaja sin café.
if energia <30 and not(trae_cafe): #not(trae_cafe) | Trae_Cafe == False
    mensaje = 'Acceso denegado: Necesitas dormir o tomar cafe.'
# TODO: usa or para permitir energía suficiente o café.
elif energia >=30 or trae_cafe: #trae_cafe == True
    mensaje = 'Acceso permitido: Pasa, pero comparte cafe.'
# TODO: escribe mensajes claros para cada resultado.
else:
    mensaje = 'El guarda está confundido, revisa las respuestas.'
    
print(mensaje)


