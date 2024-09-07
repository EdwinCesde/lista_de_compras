lista_compras = []
i = 0
nombre = input("Bienvenido por favor ingrese su nombre: ")
while (i != 1):
    menu = input(f"{nombre} ¿Qué desea hacer? (a.Agregar Artículo, b.Eliminar Artículo, c.Mostrar Lista, d.Salir)")
    if(menu == "a" or menu == "A"):
        nombre_articulo = input("Ingrese el nombre del artículo: ")
        lista_compras.append(nombre_articulo)
        print(f"El articulo {nombre_articulo} ¡ha sido agregado correctamente!")
    elif(menu == "b") or (menu == "B"):
        for i, nombre_articulo in enumerate(lista_compras):
            print(f"{i}. {nombre_articulo}")
        articulo_eliminar = int(input("Cual es el índice del elemento a eliminar: "))
        if 0 <= articulo_eliminar < len(lista_compras):
            eliminar = lista_compras.pop(articulo_eliminar)
            print(f"El artículo {eliminar} ha sido eliminado de la lista")
        """del lista_compras[articulo_eliminar]
        print(f"El artículo {lista_compras[articulo_eliminar]} ha sido eliminado de la lista")
        """
    elif(menu == "c") or (menu == "C"):
        for i, nombre_articulo in enumerate(lista_compras):
            print(f"{i}. {nombre_articulo}")
    elif(menu == "d") or (menu == "D"):
        print("Proceso terminado Hasta luego")
        i = 1
    else:
        print("Opción incorrecta, intente nuevamente")

