# Programa con lenguaje Python, aplicando la Programación Orientada a Objetos, a través de un listado de tareas

class Listado:
    # Clase padre
    # En el construcctor se define la clase

    def __init__(self):
        # se instancia un array donde se van a ir añadiendo las tareas
        self.tasks = []



# Atributos y métodos de la clase.
# En pyhthon no se escribe getter y setter, en otros lenguajes sí es obligatorio

    def añadir_tarea(self, task):
        # Se añade una nueva tarea al final de la lista con el método "append" y se le añade un literal en el print como resultado
        self.tasks.append({"task": task, "completed": False})
        print(f"Tarea añadida: {task}")

    def check_tarea_completada(self, index):
        #Se marca una tarea como completada teniendo en cuenta el index
        # se aplica excepción de los requerimientos
        try:
            if not self.tasks[index]["completed"]:
                self.tasks[index]["completed"] = True
                print(f"Tarea '{self.tasks[index]['task']}' completada.")
            else:
                print("Esta tarea ya estaba completada.")
        except IndexError:
            print("No existe la tarea en esa posición.")

    def mostrar_tarea(self):
        # se muestra todas las tareas con su estado, para poder hacer el recorrido, se utiliza un bucle for donde iterar cada una de las tareas
        # por defecto las tareas se muestran como pendientes hasta que el usuario modifica el estado a completada
        if self.tasks:
            for i, task in enumerate(self.tasks):
                status = "Completada" if task["completed"] else "Pendiente"
                print(f"{i + 1}. {task['task']} - {status}")
        else:
            print("En este momento no tienes tareas pendientes.")

    def borrar_tarea(self, index):
        # En este caso, Se borra una tarea de la lista en una posición específica. Para conseguir esto, se utiliza el método "pop" 
        try:
            removed_task = self.tasks.pop(index)
            print(f"Tarea borrada: {removed_task['task']}")
        except IndexError:
            print("No existe la tarea en esa posición.")

# En el programa se dan las opciones al usuario para añadir, eliminar tareas, así cmo marcar las que estén completadas o la opción de eliminarlas.

listado = Listado()# En el construcctor se define
while True:
        print("Elige la opción:")
        print("1. Añadir tarea nueva")
        print("2. Seleccionar tarea como completada")
        print("3. Mostrar el listado de todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")
        

        # añadimos los condicionales, en función de la opción que elige el usuario (1,2,3,4 ó 5) se mostrará un resultado u otro. Añadiendo un error en caso de que ninguna opción del try sea correcta.
        # añado int() para convertir datos a enteros.
        try:
            select = int(input("Selecciona una opción: "))
            if select == 1:
                task = input("Qué tarea quieres agregar: ")
                listado.añadir_tarea(task)
            elif select == 2:
                #se añade -1 para ajustar el orden que escribe el usuario con el index del array
                index = int(input("Qué posición ocupa la tarea completada: ")) - 1
                listado.check_tarea_completada(index)
            elif select == 3:
                listado.mostrar_tarea()
            elif select == 4:
                index = int(input("Qué posición ocupa la tarea que se va a eliminar: ")) - 1
                listado.borrar_tarea(index)
            elif select == 5:
                print("Cerrar programa de tareas.")
                break
            else:
                print("Opción no válida. Elije otra opción.")
        except ValueError:
            print("Por favor, escribe un número válido.")

