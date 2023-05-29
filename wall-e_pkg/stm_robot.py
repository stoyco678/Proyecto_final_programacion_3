from transitions import Machine
from wally import *
import tkinter as tk
window=tk.Tk()

robo=Robot_ai()

states=['selecting_category','home','category_botellas','category_latas','category_recipientes','category_papeles_carton',
        'reporting_category_completion','scaning_terrain','looking_for_object','scaning_orientations_object',
        'adjusting_trayectory','going_to_the_object','measuring_distance','grabbing_the_object','failed_mision',
        'stoped','informing_problem','waiting_for_help','going_to_the_container','unloading']
transitions=[{'trigger': 'iniciar', 'source': 'home', 'dest': 'scaning_terrain'},
             {'trigger': 'escaneo_de_terreno_completado', 'source': 'scaning_terrain', 'dest': 'selecting_category'},
             {'trigger': 'categoria_inicial_botellas_plasticas', 'source': 'selecting_category', 'dest': 'category_botellas'},
             {'trigger': 'empieza_busqueda', 'source': 'category_botellas', 'dest': 'looking_for_object'},
             {'trigger': 'empieza_busqueda', 'source': 'category_latas', 'dest': 'looking_for_object'},
             {'trigger': 'empieza_busqueda', 'source': 'category_recipientes', 'dest': 'looking_for_object'},
             {'trigger': 'empieza_busqueda', 'source': 'category_papel_carton', 'dest': 'looking_for_object'},
             {'trigger': 'objeto_encontrado', 'source': 'looking_for_object', 'dest': 'scaning_orientations_object'},
             {'trigger': 'escaneo_de_objeto_completado', 'source': 'scaning_orientations_object', 'dest': 'adjusting_trayectory'},
             {'trigger': 'objeto_movido', 'source': 'adjusting_trayectory', 'dest': 'scaning_orientations_object'},
             {'trigger': 'escaneo_de_objeto_completado_nuevamente', 'source': 'scaning_orientations_object', 'dest': 'adjusting_trayectory'},
             {'trigger': 'trayectoria_calculada', 'source': 'adjusting_trayectory', 'dest': 'going_to_the_object'},
             {'trigger': 'objeto_cercano', 'source': 'going_to_the_object', 'dest': 'measuring_distance'},
             {'trigger': 'todo_preparado', 'source': 'measuring_distance', 'dest': 'grabbing_the_object'},
             {'trigger': 'error_inesperado', 'source': 'grabbing_the_object', 'dest': 'informing_problem'},
             {'trigger': 'recogido_exitosamente', 'source': 'grabbing_the_object', 'dest': 'going_to_the_container'},
             {'trigger': 'finalizar_tarea', 'source': 'going_to_the_container', 'dest': 'unloading'},
             {'trigger': 'empieza_busqueda', 'source': 'unloading', 'dest': 'looking_for_object'},
             {'trigger': 'objeto_soltado', 'source': 'going_to_the_container', 'dest': 'looking_for_object'},
             {'trigger': 'cambiar_categoria1', 'source': '*', 'dest': 'category_latas'},
             {'trigger': 'cambiar_categoria2', 'source': '*', 'dest': 'category_recipientes'},
             {'trigger': 'cambiar_categoria3', 'source': '*', 'dest': 'category_papeles_carton'},
             {'trigger': 'no_hay_mas_botellas', 'source': 'unloading', 'dest': 'reporting_category_completion'},
             {'trigger': 'categoria_terminada', 'source': 'reporting_category_completion', 'dest': 'category_latas'},
             {'trigger': 'no_hay_mas_latas', 'source': 'category_latas', 'dest': 'reporting_category_completion'},
             {'trigger': 'categoria_terminada', 'source': 'reporting_category_completion', 'dest': 'category_recipientes'},
             {'trigger': 'mo_hay_mas_recipientes', 'source': 'category_recipientes', 'dest': 'reporting_category_completion'},
             {'trigger': 'categoria_terminada', 'source': 'reporting_category_completion', 'dest': 'category_papeles_carton'},
             {'trigger': 'no_hay_mas_papeles_carton', 'source': 'reporting_category_completion', 'dest': 'unloading'},
             {'trigger': 'parada_de_emergencia', 'source': '*', 'dest': 'stoped'},
             {'trigger': 'continuar', 'source': 'stoped', 'dest': '*'},
             {'trigger': 'problema_mecanico', 'source': '*', 'dest': 'informing_problem'},
             {'trigger': 'no_fue_posible_agarrar_el_objeto', 'source': 'grabbing_the_object', 'dest': 'informing_problem'},
             {'trigger': 'esperar', 'source': 'informing_problem', 'dest': 'waiting_for_help'}]
robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
def caso1():
    robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
    txt=tk.Label(text='Se suelta un objeto de la garra del robot')
    txt.pack()
    e1 = tk.Label(text=robo.state)
    robo.iniciar()
    e2 = tk.Label(text=robo.state)
    robo.escaneo_de_terreno_completado()
    robo.categoria_inicial_botellas_plasticas()
    e3 = tk.Label(text=robo.state)
    robo.empieza_busqueda()
    e4 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e5 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e6 = tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e7 = tk.Label(text=robo.state)
    robo.objeto_cercano()
    e8 = tk.Label(text=robo.state)
    robo.todo_preparado()
    e9 = tk.Label(text=robo.state)
    robo.recogido_exitosamente()
    e10 = tk.Label(text=robo.state)
    robo.objeto_soltado()
    e11= tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e12= tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e13= tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e14= tk.Label(text=robo.state)
    robo.objeto_cercano()
    e15= tk.Label(text=robo.state)
    robo.todo_preparado()
    e16= tk.Label(text=robo.state)
    robo.recogido_exitosamente()
    e17= tk.Label(text=robo.state)
    robo.finalizar_tarea()
    e18= tk.Label(text=robo.state)
    labels1=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18]
    def start1():
        for label1 in labels1:
            label1.pack()
    start_button=tk.Button(text='Iniciar',width=18,height=2,bg="lightgreen",command=start1)
    start_button.pack()
def caso2():
    robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
    txt=tk.Label(text='Se mueve y/o cambia la posición u orientación de un objeto mientras se intenta agarrar')
    txt.pack()
    e19 = tk.Label(text=robo.state)
    robo.iniciar()
    e20 = tk.Label(text=robo.state)
    robo.escaneo_de_terreno_completado()
    e21 = tk.Label(text=robo.state)
    robo.categoria_inicial_botellas_plasticas()
    e22 = tk.Label(text=robo.state)
    robo.empieza_busqueda()
    e23 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e24 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e25 = tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e26 = tk.Label(text=robo.state)
    robo.objeto_cercano()
    e27 = tk.Label(text=robo.state)
    robo.todo_preparado()
    e28 = tk.Label(text=robo.state)
    robo.recogido_exitosamente()
    e29 = tk.Label(text=robo.state)
    robo.objeto_soltado()
    e30 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e31 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e32= tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e33= tk.Label(text=robo.state)
    robo.objeto_cercano()
    e34= tk.Label(text=robo.state)
    robo.todo_preparado()
    e35= tk.Label(text=robo.state)
    robo.recogido_exitosamente()
    e36= tk.Label(text=robo.state)
    robo.finalizar_tarea()
    e37= tk.Label(text=robo.state)
    labels2=[e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37]
    
    def start2():
        for label2 in labels2:
            label2.pack()
    start2_button=tk.Button(text='Iniciar',width=18,height=2,bg="lightgreen",command=start2)
    start2_button.pack()
def caso3():
    robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
    txt=tk.Label(text='El robot no consigue llegar a la posición del objeto')
    txt.pack()
    e38 = tk.Label(text=robo.state)
    robo.iniciar()
    e39 = tk.Label(text=robo.state)
    robo.escaneo_de_terreno_completado()
    e40 = tk.Label(text=robo.state)
    robo.categoria_inicial_botellas_plasticas()
    e41 = tk.Label(text=robo.state)
    robo.empieza_busqueda()
    e42 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e43 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e44 = tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e45 = tk.Label(text=robo.state)
    robo.objeto_cercano()
    e46 = tk.Label(text=robo.state)
    robo.todo_preparado()
    e47 = tk.Label(text=robo.state)
    robo.no_fue_posible_agarrar_el_objeto()
    e48 = tk.Label(text=robo.state)
    robo.esperar()
    e49 = tk.Label(text=robo.state)
    labels=[e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
    def start3():
        for label in labels:
            label.pack()
    start3_button=tk.Button(text='Iniciar',width=18,height=2,bg="lightgreen",command=start3)
    start3_button.pack()
def caso4():
    robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
    txt=tk.Label(text='El robot llega a la posición donde se debe depositar el objeto, ')
    txt.pack()
    e50 = tk.Label(text=robo.state)
    robo.iniciar()
    e51 = tk.Label(text=robo.state)
    robo.escaneo_de_terreno_completado()
    e52 = tk.Label(text=robo.state)
    robo.categoria_inicial_botellas_plasticas()
    e53 = tk.Label(text=robo.state)
    robo.empieza_busqueda()
    e54 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e55 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e56 = tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e57 = tk.Label(text=robo.state)
    robo.objeto_cercano()
    e58 = tk.Label(text=robo.state)
    robo.todo_preparado()
    e59 = tk.Label(text=robo.state)
    robo.recogido_exitosamente()
    e60= tk.Label(text=robo.state)
    robo.finalizar_tarea()
    e61= tk.Label(text=robo.state)
    labels=[e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61]
    def start4():
        for label in labels:
            label.pack()
    start4_button=tk.Button(text='Iniciar',width=18,height=2,bg="lightgreen",command=start4)
    start4_button.pack()
def caso5():
    robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
    txt=tk.Label(text='Se cambia la categoría de los objetos que se quieren recoger. ')
    txt.pack()
    def categoria1():
        robo.cambiar_categoria1()
        h = tk.Label(text=robo.state)
        h.pack()
        labels=[e69,e71,e72,e73,e74,e75,e76]
        for label in labels:
            label.pack()    
    def categoria2():
        robo.cambiar_categoria2()
        h = tk.Label(text=robo.state)
        h.pack()
        labels=[e69,e71,e72,e73,e74,e75,e76]
        for label in labels:
            label.pack()
    def categoria3():
        robo.cambiar_categoria3()
        h = tk.Label(text=robo.state)
        h.pack()
        labels=[e69,e71,e72,e73,e74,e75,e76]
        for label in labels:
            label.pack()
    e62 = tk.Label(text=robo.state)
    robo.iniciar()
    e63 = tk.Label(text=robo.state)
    robo.escaneo_de_terreno_completado()
    e64 = tk.Label(text=robo.state)
    robo.categoria_inicial_botellas_plasticas()
    e65 = tk.Label(text=robo.state)
    e66=tk.Button(text='Cambiar Categoria a latas',width=24,height=2,bg="green",command=categoria1)
    e67=tk.Button(text='Cambiar Categoria a recipientes',width=24,height=2,bg="green",command=categoria2)
    e68=tk.Button(text='Cambiar Categoria a papeles o carton',width=24,height=2,bg="green",command=categoria3)
    
    robo.empieza_busqueda()
    e69 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e70 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e71 = tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e72 = tk.Label(text=robo.state)
    robo.objeto_cercano()
    e73 = tk.Label(text=robo.state)
    robo.todo_preparado()
    e74 = tk.Label(text=robo.state)
    robo.recogido_exitosamente()
    e75= tk.Label(text=robo.state)
    robo.finalizar_tarea()
    e76= tk.Label(text=robo.state)
    labels=[e62,e63,e64,e65,e66,e67,e68]
    
    def start5():
        for label in labels:
            label.pack()
    start5_button=tk.Button(text='Iniciar',width=18,height=2,bg="lightgreen",command=start5)
    start5_button.pack()
def caso6():
    robo.machine = Machine(model=robo, states=states ,transitions=transitions, initial='home')
    txt=tk.Label(text='Fallos Técnicos ')
    txt.pack()
    e77 = tk.Label(text=robo.state)
    robo.iniciar()
    e78 = tk.Label(text=robo.state)
    robo.escaneo_de_terreno_completado()
    e79 = tk.Label(text=robo.state)
    robo.categoria_inicial_botellas_plasticas()
    e80 = tk.Label(text=robo.state)
    robo.empieza_busqueda()
    e81 = tk.Label(text=robo.state)
    robo.objeto_encontrado()
    e82 = tk.Label(text=robo.state)
    robo.escaneo_de_objeto_completado()
    e83 = tk.Label(text=robo.state)
    robo.trayectoria_calculada()
    e84 = tk.Label(text=robo.state)
    robo.problema_mecanico()
    e85 = tk.Label(text=robo.state)
    robo.esperar()
    e86 = tk.Label(text=robo.state)
    labels=[e77,e78,e79,e80,e81,e82,e83,e84,e85,e86]
    def start6():
        for label in labels:
            label.pack()
    start6_button=tk.Button(text='Iniciar',width=18,height=2,bg="lightgreen",command=start6)
    start6_button.pack()
menu = tk.Menu(window)
# Crear el menú "Archivo" con algunas opciones
menu_archivo = tk.Menu(menu, tearoff=0)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=window.quit)
# Crear el menú "Opciones" con una opción
menu_opciones = tk.Menu(menu, tearoff=0)
menu_opciones.add_command(label="Opción 1", command=caso1)
menu_opciones.add_command(label="Opción 2", command=caso2)
menu_opciones.add_command(label="Opción 3", command=caso3)
menu_opciones.add_command(label="Opción 4", command=caso4)
menu_opciones.add_command(label="Opción 5", command=caso5)
menu_opciones.add_command(label="Opción 6", command=caso6)
# Agregar los menús al objeto Menu principal
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu.add_cascade(label="Opciones", menu=menu_opciones)
# Asignar el menú a la ventana principal
window.config(menu=menu)
window.mainloop()