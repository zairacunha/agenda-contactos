# src/agenda.py - Agenda de Contactos
contactos = []
def buscar_contacto():
	if len(contactos) == 0:
		print("\n📋 La agenda está vacía.")
		return
	busqueda = input("Nombre a buscar: ").strip().lower()
	encontrados = []
	for c in contactos:
		if busqueda in c["nombre"].lower():
			encontrados.append(c)
	if len(encontrados) == 0:
		print(f"❌ No se encontró ningún contacto con '{busqueda}'.")
	else:
		print(f"\n🔍 Resultados para '{busqueda}':")
		for c in encontrados:
			print(f" • {c['nombre']} — {c['telefono']}")

def eliminar_contacto():
	if len(contactos) == 0:
		print("\n📋 La agenda está vacía.")
		return
	nombre = input("Nombre del contacto a eliminar: ").strip().lower()
	for c in contactos:
		if c["nombre"].lower() == nombre:
			contactos.remove(c)
			print(f"️ Contacto '{c['nombre']}' eliminado.")
			return
print(f"❌ No se encontró el contacto '{nombre}'.")
def mostrar_menu():
	print("\n===== AGENDA DE CONTACTOS =====")
	print("1. Agregar contacto")
	print("2. Ver todos los contactos")
	print("3. Buscar contacto")
	print("4. Eliminar contacto")
	print("5. Guardar y salir")
	print("================================")
def main():
	print("¡Bienvenido a la Agenda de Contactos!")
	while True:
		mostrar_menu()
		opcion = input("\nElegí una opción: ")
		if opcion == "5":
			print("\n¡Hasta luego!")
		break
	else:
		print("⚠️ Opción no implementada todavía.")

if __name__ == "__main__":
	main()
elif opcion == "3":
	buscar_contacto()
elif opcion == "4":
	eliminar_contacto()