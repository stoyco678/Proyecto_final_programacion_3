# PROYECTO FINAL

En este documento se presentara la explicacion correspondiente al proyecto final de programación 3
# Nombres

Daniel Alberto Peña Diaz 7004098

Gabriel Eduardo Gonzalez Tellez 7004080

# Explicación

`stm_robot.py` Modulo del codigo de la maquina de estados junto con la GUI
`diagrama_de_clases.py` Modulo del codigo en python del diagrama de clases 

# Historia de usuario

Para seleccionar un objeto Wally parte de una posición inicial "home", y luego siguiendo una trayectoria definida explora el terreno buscando un objeto. Wally busca objetos con una trayectoria que sigue su cámara ubicada al lado de su garra, por lo tanto la exploración inicial se hace siguiendo una trayectoria de la camera,  su actividad inteligente o AI procesa la imagen, buscando por algún objeto en la imagen, entonces cuando encuentra un objeto Wally ajusta la trayectoria de su camara para que el objeto quede justo en el centro de la imagen, aquí es más fácil determinar la orientación del objeto y la categoría con su AI, adicionalmente un sensor al lado de la garra también determina la distancia al objeto. Wally reinterpreta la información del objeto para saber el punto en el espacio y la orientación que debe tener su garra para tomar el objeto, entonces se mueve al objeto e intenta agarrarlo, si lo logra con éxito entonces lleva ese objeto a la posición del contenedor (que se encuentra a al alcance de su garra) y deposita el objeto allí. Finalmente vuelve a su posición inicial home para continuar su exploración en busca de más objetos. Si no logra encontrar más objetos en el espacio de alcance de su garra/camara entonces se mueve completamente a otro lugar para realizar otra exploración.
