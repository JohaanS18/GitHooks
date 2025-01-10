
def sumar(a, b):
	return a + b #cambiar función

res = sumar(3, 4)
print(res)

try:
    assert sumar(3, 4.) == 7
    print("La aserción pasó correctamente.")
except AssertionError:
    print("La aserción falló.")