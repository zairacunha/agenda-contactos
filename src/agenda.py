# src/agenda.py - Agenda de Contactos
contactos = []
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
		if opcion == "1":
			agregar_contacto()
		elif opcion == "2":
			ver_contactos()
		elif opcion == "5":
			print("\n¡Hasta luego!")
			break
		else:
			print("⚠️ Opción no implementada todavía.")

if __name__ == "__main__":
	main()
def agregar_contacto():
	nombre = input("Nombre del contacto: ").strip()
	if nombre == "":
		print("⚠️ El nombre no puede estar vacío.")
		return
	telefono = input("Teléfono: ").strip()
	if telefono == "":
		print("⚠️ El teléfono no puede estar vacío.")
		return
	contactos.append({"nombre": nombre, "telefono": telefono})
	print(f"✅ Contacto '{nombre}' agregado correctamente.")
def ver_contactos():
	if len(contactos) == 0:
		print("\n📋 La agenda está vacía.")
		return
	print("\n📋 LISTA DE CONTACTOS:")
	print("-" * 30)
	for i, c in enumerate(contactos, 1):
		print(f" {i}. {c['nombre']} — {c['telefono']}")
	print("-" * 30)
	print(f"Total: {len(contactos)} contacto(s)")