#Solución Misión Kit Seguro
#Autor: Fecha: 2026/10/06

nombre = input('Nombre: ').strip().upper()
kit = input('Tipo de kit: ').strip().lower()
autorizacion =input('Tiene autorización (si/no)?: ').lower().strip() == 'si'

try:
    cantidad = int(input('Ingrese la cantidad: '))
except ValueError:
    print('Error: cantidad invalida, asignada -1')
    cantidad = -1
try:
    dias = int(input('Dias de prestamo: '))
except ValueError:
    print('Error cantidad invalida, asignada -1')
    dias = -1
    
resultado = ''
if not nombre or kit == '' or cantidad < 1 or dias < 1:
    resultado = 'Registro rechazado: datos inválidos! '
elif autorizacion and cantidad <= 3 and not dias > 7:  #not dias > 7 | dias <=7
    resultado = f'Solicitud aprodaba para {nombre}: {cantidad} kit(s)'
elif cantidad > 3 or dias > 7:
    resultado = 'Solicitud enviada a revisión!'
else:
    resultado = 'Solicitud rechazada: se requiere autorizacion'
  


