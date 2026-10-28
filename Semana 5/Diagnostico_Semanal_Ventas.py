"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""


ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# Calcula total, cantidad, promedio, mayor, menor y rango para centro.
total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
promedio_centro = total_centro / cantidad_centro
menor_centro = min(ventas_centro)
mayor_centro = max(ventas_centro)
rango_centro = mayor_centro - menor_centro
diferencia_centro = total_centro - meta_centro
porcentaje_centro = (total_centro * 100 / meta_centro) if meta_centro else 0

# Se repiten los indicadores para Norte.
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
promedio_norte = total_norte / cantidad_norte
menor_norte = min(ventas_norte)
mayor_norte = max(ventas_norte)
rango_norte = mayor_norte - menor_norte
diferencia_norte = total_norte - meta_norte
porcentaje_norte = (total_norte * 100 / meta_norte) if meta_norte else 0

# Decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = 'meta superada'
elif total_centro == meta_centro:
    estado_centro = 'meta alcanzada exactamente'
else:
    estado_centro = 'meta NO alcanzada'

if total_norte > meta_norte:
    estado_norte = 'meta superada'
elif total_norte == meta_norte:
    estado_norte = 'meta alcanzada exactamente'
else:
    estado_norte = 'meta NO alcanzada'

# Compara los totales y los rangos.
if total_centro > total_norte:
    tienda_mayor_ventas = 'Tienda del centro'
elif total_norte > total_centro:
    tienda_mayor_ventas = 'Tienda del norte'
else:
    tienda_mayor_ventas = 'Ambas tiendas tienen el mismo total'

# Presenta un reporte con etiquetas claras y f-strings.
print('COMPARACION SEMANAL DE TIENDAS')
print(f'Centro | total: ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento %{porcentaje_centro:.0f}')
print(f'Centro logro: {estado_centro}')
print(f'Norte | total: ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento %{porcentaje_norte:.0f}')
print(f'Norte logro: {estado_norte}')
print(f'Rango centro: ₡{rango_centro:,.2f} | diferencia frente a meta: ₡{diferencia_centro:,.2f}')
print(f'Rango norte: ₡{rango_norte:,.2f} | diferencia frente a meta: ₡{diferencia_norte:,.2f}')

# Tres conclusiones del análisis.
if total_centro > total_norte:
    conclusion_1 = 'La tienda del centro tuvo un total semanal mayor que la del norte.'
elif total_norte > total_centro:
    conclusion_1 = 'La tienda del norte tuvo un total semanal mayor que la del centro.'
else:
    conclusion_1 = 'Ambas tiendas registraron el mismo total semanal.'

conclusion_2 = f'La tienda del centro promedió ₡{promedio_centro:,.2f} por día y tuvo un rango de ₡{rango_centro:,.2f}.'
conclusion_3 = f'La tienda del norte promedió ₡{promedio_norte:,.2f} por día y tuvo un rango de ₡{rango_norte:,.2f}.'

print(conclusion_1)
print(conclusion_2)
print(conclusion_3)

