

def mostrar_menu():
    print('\nAgenda de contactos')
    print(' ')
    print('1. Agregar nuevo contacto')
    print('2. Eliminar contacto')
    print('3. Buscar contacto')
    print('4. Lista de contactos')
    print('5. Salir del programa')
    
def agregar_contacto(agenda):
    #Guardamos la entrada por teclado en variables
    nombre = input('Por favor introduzca el nombre completo del contacto: ')
    telefono= input('Por favor introduzca el telefono del contacto: ')
    email= input('Por favor introduzca el email del contacto: ')
    agenda[nombre] = {'telefono': telefono, 'email': email} #Guardamos toda la información en un diccionario
    print(' ')
    print(f'Se ha creado el contacto {nombre} exitosamente')
    
def eliminar_contacto(agenda):
    nombre = input('Ingrese el nombre del contacto que desea eliminar: ')
    
    if nombre in agenda:
        del agenda[nombre]
        print(' ')
        print(f'El contacto de {nombre} ha sido eliminado correctamente')
    else:
        print(f'No se ha encontrado un contacto con el nombre {nombre}')
        
def buscar_contacto(agenda):
    nombre = input('Ingrese el nombre del contacto que esta buscado: ')
    
    if nombre in agenda:
        print(' ')
        print(f'nombre: {nombre}')
        print(f"telefono: {agenda[nombre]['telefono']}")
        print(f"email: {agenda[nombre]['email']}")
    else:
        print(' ')
        print(f'el contacto {nombre} no ha sido encontrado en la agenda')
        
def lista_contactos(agenda):
    if agenda:
        print('\n Lista e contactos: ')
        for nombre, info in agenda.items():
            print(f'nombre: {nombre}') 
            print(f"telefono: {info['telefono']}") 
            print(f"email: {info['email']}")
            print('-' * 20)
    else:
        
        print(' ')
        print('La agenda esta vacia')

    
def agenda_contactos():
    agenda = {} #Diccionario que recibira las entradas por teclado
           
    while True:
        mostrar_menu()
        print(' ')
        opcion = input('Por fvor elija una opción: ')
            
        if opcion == '1':
            agregar_contacto(agenda) #LLamamos la función y le pasamos como parametro el diccionario agenda
        elif opcion == '2':
            eliminar_contacto(agenda)
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            lista_contactos(agenda)
        elif opcion == '5':
            print('Saliendo de la agenda, hasta luego')
            break
        else:
            print('por favor, seleccione una opción valida')
                
agenda_contactos()