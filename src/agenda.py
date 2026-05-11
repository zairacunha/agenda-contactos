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
	else:
		print("⚠️ Opción no implementada todavía.")

if __name__ == "__main__":
	main()