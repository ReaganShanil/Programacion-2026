"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""


ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para centro.

# TODO: calcula promedio, rango, diferencia y porcentaje para centro.

total_centro = sum(ventas_centro) #Total de ventas semanal
cantidad_centro = len(ventas_centro) #Cantidad de días registrados

promedio_centro = total_centro / cantidad_centro #Promedio de ventas diario
menor_centro = min(ventas_centro) #Venta minima de la tienda del centro
mayor_centro = max(ventas_centro) #Venta maxima de la tienda del centro

porcentaje_centro = (total_centro * 100 / meta_centro)
#print(total_centro)
#print(porcentaje_centro)

#Se repiten los indicadores para Norte.
total_norte = sum(ventas_norte) #Total de ventas semanal
cantidad_norte = len(ventas_norte) #Cantidad de días registrados

promedio_norte = total_norte / cantidad_norte #Promedio de ventas diario
menor_norte = min(ventas_norte) #Venta minima de la tienda del norte
mayor_norte = max(ventas_norte) #Venta maxima de la tienda del norte

porcentaje_norte = (total_norte * 100 / meta_norte)
#print(total_norte)
#print(porcentaje_norte)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro= 'meta superada'
elif total_centro == meta_centro:
        estado_norte = 'meta alcanzada exactamente'
else:
    estado_centro = 'meta NO alcanzada'
    
if total_norte > meta_norte:
    estado_norte= 'meta superada'
elif total_norte == meta_norte:
        estado_norte = 'meta alcanzada exactamente'
else:
    estado_norte = 'meta NO alcanzada'

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_mayor_ventas = 'Tienda del centro'
elif total_norte > total_centro:
    tienda_mayor_venta = 'Tienda del norte'
else:
    tienda_mayor_venta = 'Ambas tiendas tienen el mismo total'

# TODO: presenta un reporte con etiquetas claras y f-strings.

print ('COMPARACION SEMANAL DE TIENDAS')
print(f'Centro | total: ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento %{porcentaje_centro:.0f}')
print(f'Centro logro: {estado_centro}')
print(f'Norte | total: ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento %{porcentaje_norte:.0f}')
print(f'Norte logro: {estado_norte}')


# TODO: escribe las tres conclusiones solicitadas en la guía.
