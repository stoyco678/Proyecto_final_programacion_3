class RobotActivity(object):
    def __init__(self):
        self.__Observación = ""
        
        self.robotwally = None
        
    # Start of user code -> properties/constructors for RobotActivity class

    # End of user code
    def Encendido(self):
        # Start of user code protected zone for Encendido function body
        return False
        # End of user code	
    def VisualizarTerreno(self, parameter, parameter2):
        # Start of user code protected zone for VisualizarTerreno function body
        return None
        # End of user code	
    def Avanzar(self, parameter):
        # Start of user code protected zone for Avanzar function body
        return None
        # End of user code	
    def Retroceder(self, parameter, parameter2):
        # Start of user code protected zone for Retroceder function body
        return None
        # End of user code	
    def GirarIzquierda(self, parameter, parameter2):
        # Start of user code protected zone for GirarIzquierda function body
        return None
        # End of user code	
    def GirarDerecha(self, parameter, parameter2):
        # Start of user code protected zone for GirarDerecha function body
        return None
        # End of user code	
    def RotaciónGarra(self, parameter):
        # Start of user code protected zone for RotaciónGarra function body
        return None
        # End of user code	
    def RotaciónCamara(self, parameter):
        # Start of user code protected zone for RotaciónCamara function body
        return None
        # End of user code	
    def RotaciónBrazo(self, parameter):
        # Start of user code protected zone for RotaciónBrazo function body
        return None
        # End of user code	
    def IdentificarObjeto(self, parameter):
        # Start of user code protected zone for IdentificarObjeto function body
        return None
        # End of user code	
    def AgarrarObjeto(self, parameter, parameter2, parameter3, parameter4, parameter5):
        # Start of user code protected zone for AgarrarObjeto function body
        return None
        # End of user code	
    def SoltarObjeto(self, parameter, parameter2, parameter3):
        # Start of user code protected zone for SoltarObjeto function body
        return None
        # End of user code	
    def AcercamientoObjeto(self, parameter, parameter2):
        # Start of user code protected zone for AcercamientoObjeto function body
        return None
        # End of user code	
    def MediciónObjeto(self, parameter):
        # Start of user code protected zone for MediciónObjeto function body
        return None
        # End of user code	
    # Start of user code -> methods for RobotActivity class

    # End of user code


class ObjetoReciclable(object):
    def __init__(self):
        self.__Orientación = None
        self.__Dimensión = None
        self.__Reciclable = False
        self.__Color = ""
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for ObjetoReciclable class

    # End of user code
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    def getDimensión(self):
        # Start of user code protected zone for getDimensión function body
        return None
        # End of user code	
    def setDimensión(self):
        # Start of user code protected zone for setDimensión function body
        return None
        # End of user code	
    def getReciclable(self):
        # Start of user code protected zone for getReciclable function body
        return False
        # End of user code	
    def setReciclable(self):
        # Start of user code protected zone for setReciclable function body
        return False
        # End of user code	
    def getColor(self):
        # Start of user code protected zone for getColor function body
        return ""
        # End of user code	
    def getColor(self):
        # Start of user code protected zone for getColor function body
        return ""
        # End of user code	
    # Start of user code -> methods for ObjetoReciclable class

    # End of user code

class Orientación(object):
    def __init__(self):
        self.__Avanzar = 0.
        self.__Agarrar = 0.
        self.__Observar = 0.
        
        self.garra = None
        self.brazo = None
        self.base_piernas = None
        self.cámara = None
        
    # Start of user code -> properties/constructors for Orientación class

    # End of user code
    def getAvanzar(self):
        # Start of user code protected zone for getAvanzar function body
        return 0.
        # End of user code	
    def setAvanzar(self):
        # Start of user code protected zone for setAvanzar function body
        return 0.
        # End of user code	
    def getAgarra(self):
        # Start of user code protected zone for getAgarra function body
        return 0.
        # End of user code	
    def setAgarra(self):
        # Start of user code protected zone for setAgarra function body
        return 0.
        # End of user code	
    def getObservar(self):
        # Start of user code protected zone for getObservar function body
        return 0.
        # End of user code	
    def serObservar(self):
        # Start of user code protected zone for serObservar function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Orientación class

    # End of user code

class Objetos(object):
    def __init__(self):
        self.__Imagen = None
        self.__Dimensión = None
        self.__Coordenadas = None
        self.__Reciclable = False
        self.__Orientación = None
        self.__distancia = 0.
        self.__Detección = None
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Objetos class

    # End of user code
    def setImagen(self):
        # Start of user code protected zone for setImagen function body
        return None
        # End of user code	
    def getImagen(self):
        # Start of user code protected zone for getImagen function body
        return None
        # End of user code	
    def getDimensión(self):
        # Start of user code protected zone for getDimensión function body
        return None
        # End of user code	
    def setDimensión(self):
        # Start of user code protected zone for setDimensión function body
        return None
        # End of user code	
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getReciclable(self):
        # Start of user code protected zone for getReciclable function body
        return False
        # End of user code	
    def setReciclable(self):
        # Start of user code protected zone for setReciclable function body
        return False
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    def getDistancia(self):
        # Start of user code protected zone for getDistancia function body
        return 0.
        # End of user code	
    def setDistancia(self):
        # Start of user code protected zone for setDistancia function body
        return 0.
        # End of user code	
    def getDetección(self):
        # Start of user code protected zone for getDetección function body
        return None
        # End of user code	
    def setDetección(self):
        # Start of user code protected zone for setDetección function body
        return None
        # End of user code	
    # Start of user code -> methods for Objetos class

    # End of user code

class Recolección(object):
    def __init__(self):
        self.__Coordenadas = None
        self.__Garra = None
        self.__Orientación = None
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Recolección class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getGarra(self):
        # Start of user code protected zone for getGarra function body
        return None
        # End of user code	
    def setGarra(self):
        # Start of user code protected zone for setGarra function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    # Start of user code -> methods for Recolección class

    # End of user code



class Almacenamiento_Contenedor(object):
    def __init__(self):
        self.__Coordenadas = None
        self.__Orientación = None
        self.__Reciclable = False
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Almacenamiento/Contenedor class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    def getReciclable(self):
        # Start of user code protected zone for getReciclable function body
        return False
        # End of user code	
    def setReciclable(self):
        # Start of user code protected zone for setReciclable function body
        return False
        # End of user code	
    # Start of user code -> methods for Almacenamiento/Contenedor class

    # End of user code




class Detección(object):
    def __init__(self):
        self.__Cámara = None
        self.__Imagen = None
        self.__Dimensión = None
        self.__Apto = False
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Detección class

    # End of user code
    def getCámara(self):
        # Start of user code protected zone for getCámara function body
        return None
        # End of user code	
    def setCámara(self):
        # Start of user code protected zone for setCámara function body
        return None
        # End of user code	
    def setImagen(self):
        # Start of user code protected zone for setImagen function body
        return None
        # End of user code	
    def getImagen(self):
        # Start of user code protected zone for getImagen function body
        return None
        # End of user code	
    def getDimensión(self):
        # Start of user code protected zone for getDimensión function body
        return None
        # End of user code	
    def setDimensión(self):
        # Start of user code protected zone for setDimensión function body
        return None
        # End of user code	
    def getApto(self):
        # Start of user code protected zone for getApto function body
        return False
        # End of user code	
    def setApto(self):
        # Start of user code protected zone for setApto function body
        return False
        # End of user code	
    # Start of user code -> methods for Detección class

    # End of user code

class Robot (object):
    def __init__(self):
        
        self.robotActivity = None
        
    # Start of user code -> properties/constructors for Robot Wally class

    # End of user code
    # Start of user code -> methods for Robot Wally class

    # End of user code





class Exploración(object):
    def __init__(self):
        self.__Cordenadas = None
        self.__Orientación = None
        self.__Cámara = None
        self.__Imagen = None
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Exploración class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    def getCámara(self):
        # Start of user code protected zone for getCámara function body
        return None
        # End of user code	
    def setCámara(self):
        # Start of user code protected zone for setCámara function body
        return None
        # End of user code	
    def setImagen(self):
        # Start of user code protected zone for setImagen function body
        return None
        # End of user code	
    def getImagen(self):
        # Start of user code protected zone for getImagen function body
        return None
        # End of user code	
    # Start of user code -> methods for Exploración class

    # End of user code

class ZonaRecarga(object):
    def __init__(self):
        self.__Coordenadas = None
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for ZonaRecarga class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    # Start of user code -> methods for ZonaRecarga class

    # End of user code

class Coordenadas(object):
    def __init__(self):
        self.__X = 0.
        self.__Y = 0.
        self.__Z = 0.
        
        self.almacenamiento_Contenedor = None
        self.brazo = None
        self.objetos = None
        self.cámara = None
        self.imagen = None
        self.exploración = None
        self.garra = None
        self.dimensión = None
        self.base_piernas = None
        self.recolección = None
        self.zonaRecarga = None
        self.detección = None
        self.objetoReciclable = None
        
    # Start of user code -> properties/constructors for Coordenadas class

    # End of user code
    def getX(self):
        # Start of user code protected zone for getX function body
        return 0.
        # End of user code	
    def getY(self):
        # Start of user code protected zone for getY function body
        return 0.
        # End of user code	
    def getZ(self):
        # Start of user code protected zone for getZ function body
        return 0.
        # End of user code	
    def setX(self):
        # Start of user code protected zone for setX function body
        return 0.
        # End of user code	
    def setY(self):
        # Start of user code protected zone for setY function body
        return 0.
        # End of user code	
    def setZ(self):
        # Start of user code protected zone for setZ function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Coordenadas class

    # End of user code





class Dimensión(object):
    def __init__(self):
        self.__Largo = 0.
        self.__Alto = 0.
        self.__Ancho = 0.
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Dimensión class

    # End of user code
    def getLargo(self):
        # Start of user code protected zone for getLargo function body
        return 0.
        # End of user code	
    def setLargo(self):
        # Start of user code protected zone for setLargo function body
        return 0.
        # End of user code	
    def getAlto(self):
        # Start of user code protected zone for getAlto function body
        return 0.
        # End of user code	
    def setAlto(self):
        # Start of user code protected zone for setAlto function body
        return 0.
        # End of user code	
    def getAncho(self):
        # Start of user code protected zone for getAncho function body
        return 0.
        # End of user code	
    def setAncho(self):
        # Start of user code protected zone for setAncho function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Dimensión class

    # End of user code


class Imagen(object):
    def __init__(self):
        self.__Largo = 0.
        self.__Alto = 0.
        self.__Volumen = 0.
        self.__Color = ""
        
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Imagen class

    # End of user code
    def getLargo(self):
        # Start of user code protected zone for getLargo function body
        return 0.
        # End of user code	
    def setLargo(self):
        # Start of user code protected zone for setLargo function body
        return 0.
        # End of user code	
    def getAlto(self):
        # Start of user code protected zone for getAlto function body
        return 0.
        # End of user code	
    def setAlto(self):
        # Start of user code protected zone for setAlto function body
        return 0.
        # End of user code	
    def getVolumen(self):
        # Start of user code protected zone for getVolumen function body
        return 0.
        # End of user code	
    def setVolumen(self):
        # Start of user code protected zone for setVolumen function body
        return 0.
        # End of user code	
    def getColor(self):
        # Start of user code protected zone for getColor function body
        return ""
        # End of user code	
    def setColor(self):
        # Start of user code protected zone for setColor function body
        return ""
        # End of user code	
    # Start of user code -> methods for Imagen class

    # End of user code

class Base_piernas(Robot):
    def __init__(self):
        self.__Cordenadas = None
        self.__Orientación = None
        
        self.orientación = None
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Base/piernas class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    # Start of user code -> methods for Base/piernas class

    # End of user code

class Cámara(Robot):
    def __init__(self):
        self.__Coordenadas = None
        self.__Orientación = None
        
        self.orientación = None
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Cámara class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    # Start of user code -> methods for Cámara class

    # End of user code

class Garra(Robot):
    def __init__(self):
        self.__Coordenadas = None
        self.__Orientación = None
        self.__Condición = False
        
        self.orientación = None
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Garra class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOritentación(self):
        # Start of user code protected zone for setOritentación function body
        return None
        # End of user code	
    def getCondición(self):
        # Start of user code protected zone for getCondición function body
        return False
        # End of user code	
    def setCondición(self):
        # Start of user code protected zone for setCondición function body
        return False
        # End of user code	
    # Start of user code -> methods for Garra class

    # End of user code

class Brazo(Robot):
    def __init__(self):
        self.__Coordenadas = None
        self.__Orientación = None
        
        self.orientación = None
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Brazo class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self):
        # Start of user code protected zone for setCoordenadas function body
        return None
        # End of user code	
    def getOrientación(self):
        # Start of user code protected zone for getOrientación function body
        return None
        # End of user code	
    def setOrientación(self):
        # Start of user code protected zone for setOrientación function body
        return None
        # End of user code	
    # Start of user code -> methods for Brazo class

    # End of user code


# Start of user code -> functions/methods for Robot Story And Especifications package

# End of user code