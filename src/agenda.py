# src/agenda.py - Agenda de Contactos

contactos = []
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
		if opcion == "1":
			agregar_contacto()
		elif opcion == "2":
			ver_contactos()
		elif opcion == "3":
			buscar_contacto()
		elif opcion == "4":
			eliminar_contacto()
		elif opcion == "5":
			print("\n¡Hasta luego!")
			break
		else:
			print("⚠️ Opción no válida.")

if __name__ == "__main__":
	main()
