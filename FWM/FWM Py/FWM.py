from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import subprocess
import os
import webbrowser
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FormWithMe")
        
        #-------------------------------------Menus--------------------------------------------
        bMenu = self.menuBar()
        menu = bMenu.addMenu("FWM")
        
        aLO = QAction("Log out", self)
        aLO.triggered.connect(self.hLogOut)
        aLO.setWhatsThis("Hacer LogOut de tu cuenta y volver")
        menu.addAction(aLO)


        wt = QAction("¿Ayuda?", self)
        wt.triggered.connect(self.mwhatsthis)
        wt.setWhatsThis("Haciendo click se le mostrará información sobre algunos campos que necesite ayuda")
        menu.addAction(wt)
        
        iGH = QAction("GitHub", self)
        iGH.triggered.connect(self.irGitHub)
        iGH.setWhatsThis("Se le llevará al GITHUB del proyecto/código")
        menu.addAction(iGH)
        
        #-------------------------------------Inicio---------------------------------------------
        layoutP = QVBoxLayout()
        VP = QWidget()
        VP.setLayout(layoutP)
        self.setCentralWidget(VP)
        
        layoutInicio = QVBoxLayout()
        inicio = QWidget()
        inicio.setLayout(layoutInicio)
        
        self.bienvenida = QLabel("BIENVENIDO!", self)
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
        layoutInicio.addWidget(self.bienvenida)
        
        self.texto = QLabel("Con nosotros, podrá crear su formulario deseado en unos pocos sencillos pasos", self)
        self.texto.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layoutInicio.addWidget(self.texto)

        self.botonIniciar = QPushButton("Go!")
        self.botonIniciar.setFixedSize(200, 20)
        layoutInicio.addWidget(self.botonIniciar)
        layoutInicio.setAlignment(self.botonIniciar, Qt.AlignHCenter | Qt.AlignVCenter)
        self.botonIniciar.clicked.connect(self.iniciar)
        
        #-----------------------------------------Acceso--------------------------------------------------
        layoutPRE = QFormLayout()
        Pre = QWidget()
        Pre.setLayout(layoutPRE)
        
        self.textoIniciar = QLabel("¿Cómo desea entrar a la aplicación?",self)
        self.textoRelleno = QLabel("")
        layoutPRE.addRow(self.textoIniciar)
        layoutPRE.addRow(self.textoRelleno)
        
        self.botonIR = QPushButton("Registrarse")
        layoutPRE.addRow(self.botonIR)
        self.botonIR.setWhatsThis("Se deberá ingresar un usuario y una contrasña que desea para introducirlo en la base de datos")
        self.botonIR.clicked.connect(self.irRegistro)
        
        self.botonIL = QPushButton("Loguearse")
        layoutPRE.addRow(self.botonIL)
        self.botonIL.setWhatsThis("Ingrese el usuario y la contraseña válida para prodecer a loguearse y tener algunas ventajas")
        self.logedin = False
        self.botonIL.clicked.connect(self.irLogueo)
    
        
        self.botonIG = QPushButton("Entrar como Guest")
        layoutPRE.addRow(self.botonIG)
        self.botonIG.setWhatsThis("Entrará sin necesidad de registro o inicio de sesión, pero se le limitará algunas acciones")
        self.botonIG.clicked.connect(self.irCreacion)
        
        self.premium = QLabel("¿Cuál es la diferencia? Habilite la ayuda proporcionada en el menú o F1 para averiguarlo")
        layoutPRE.addRow(self.premium)
        self.premium.setWhatsThis("Al iniciar con el Guest, se le limitará algunas acciones tales como: No podrá implementar mas de 4 campos; No tendrá acceso a las plantillas ya hechas de DNI y TELF")
        
        #---------------------------------------------Registro------------------------------------
        layoutFormR = QFormLayout()
        register = QWidget()
        register.setLayout(layoutFormR)
        expl = QLabel("Introduce los datos para registrarse", self)
        layoutFormR.addRow(expl)
        usuario = QLabel("Usuario R: ", self)
        clave = QLabel("Contraseña R: ", self)
        self.usuarioQLr = QLineEdit()
        layoutFormR.addRow(usuario, self.usuarioQLr)
        self.passwordr = QLineEdit()
        self.passwordr.setEchoMode(QLineEdit.Password)
        layoutFormR.addRow(clave, self.passwordr)
        
        self.botonR = QPushButton("Registar")
        layoutFormR.addRow(self.botonR)
        self.botonR.clicked.connect(self.registrar)
        
        #----------------------------------------------Login---------------------------------------------
        layoutFormL = QFormLayout()
        login = QWidget()
        login.setLayout(layoutFormL)
        usuario = QLabel("Usuario: ", self)
        clave = QLabel("Contraseña: ",self)
        self.usuarioQL = QLineEdit("")
        layoutFormL.addRow(usuario, self.usuarioQL)
        self.password = QLineEdit("")
        self.password.setEchoMode(QLineEdit.Password)
        layoutFormL.addRow(clave, self.password)

        self.botonL = QPushButton("Login")
        layoutFormL.addRow(self.botonL)
        self.botonL.clicked.connect(self.comprobar)        
        
        #-------------------------------------------------Recogida de datos-----------------------------------------------
        layoutPCantidad = QFormLayout()
        cantidad = QWidget()
        cantidad.setLayout(layoutPCantidad)
        layoutPCantidad.setSpacing(1)
        layoutPCantidad.setContentsMargins(0, 0, 0, 0)
        
        self.textoIniciar2 = QLabel("¿Cúantos campos desea ingresar?",self)
        layoutPCantidad.addRow(self.textoIniciar2)

        
        self.cantidadItems = QComboBox()
        layoutPCantidad.addRow(self.cantidadItems)
        self.cantidadItems.setFixedSize(60,20)
        self.cantidadItems.setCurrentIndex(200)
        self.cantidadItems.addItems(["None","1", "2", "3", "4", "5", "6", "7"])

        self.cantidadItems.currentIndexChanged.connect(self.setvalue)
                    #--------------------------------------------------
                                    #CAMPOS
                    #----------------------1----------------------------
        layoutPC1 = QFormLayout()
        self.cantidad1 = QWidget()
        self.cantidad1.setLayout(layoutPC1)
        
        self.nombreC1 = QLabel("Nombre1: ", self)
        self.tipoC1 = QLabel("Campo1: ", self)
        self.nombreC1L = QLineEdit()
        layoutPC1.addRow(self.nombreC1, self.nombreC1L)  
        self.tipoC1L = QComboBox()
        layoutPC1.addRow(self.tipoC1L)
        self.tipoC1L.setFixedSize(100,20)
        self.tipoC1L.setCurrentIndex(200)
        self.tipoC1L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        layoutPC1.addRow(self.tipoC1, self.tipoC1L)

        self.cantidad1.hide()        

        layoutPCantidad.addRow(self.cantidad1)
                    #--------------------------------------------------
                  #------------------------2--------------------------
        layoutPC2 = QFormLayout()
        self.cantidad2 = QWidget()
        self.cantidad2.setLayout(layoutPC2)
        
        self.nombreC2 = QLabel("Nombre2: ", self)
        self.tipoC2 = QLabel("Campo2: ", self)
        self.nombreC2L = QLineEdit()
        layoutPC2.addRow(self.nombreC2, self.nombreC2L)  
        self.tipoC2L = QComboBox()
        layoutPC2.addRow(self.tipoC2L)
        self.tipoC2L.setFixedSize(100,20)
        self.tipoC2L.setCurrentIndex(200)
        self.tipoC2L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        self.tipoC2L.currentIndexChanged.connect(self.setvalue)
        layoutPC2.addRow(self.tipoC2, self.tipoC2L)
        
        self.cantidad2.hide()        

        layoutPCantidad.addRow(self.cantidad2)
                    #--------------------------------------------------
                  #-------------------------3-------------------------
        layoutPC3= QFormLayout()
        self.cantidad3 = QWidget()
        self.cantidad3.setLayout(layoutPC3)
        
        self.nombreC3 = QLabel("Nombre3: ", self)
        self.tipoC3 = QLabel("Campo3: ", self)
        self.nombreC3L = QLineEdit()
        layoutPC3.addRow(self.nombreC3, self.nombreC3L)  
        self.tipoC3L = QComboBox()
        layoutPC3.addRow(self.tipoC3L)
        self.tipoC3L.setFixedSize(100,20)
        self.tipoC3L.setCurrentIndex(200)
        self.tipoC3L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        self.tipoC3L.currentIndexChanged.connect(self.setvalue)
        layoutPC3.addRow(self.tipoC3, self.tipoC3L)
        
        self.cantidad3.hide()        

        layoutPCantidad.addRow(self.cantidad3)
                    #--------------------------------------------------
                  #-------------------------4-------------------------
        layoutPC4 = QFormLayout()
        self.cantidad4 = QWidget()
        self.cantidad4.setLayout(layoutPC4)
                  
        self.nombreC4 = QLabel("Nombre4: ", self)
        self.tipoC4 = QLabel("Campo4: ", self)
        self.nombreC4L = QLineEdit()
        layoutPC4.addRow(self.nombreC4, self.nombreC4L)  
        self.tipoC4L = QComboBox()
        layoutPC4.addRow(self.tipoC4L)
        self.tipoC4L.setFixedSize(100,20)
        self.tipoC4L.setCurrentIndex(200)
        self.tipoC4L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        self.tipoC4L.currentIndexChanged.connect(self.setvalue)
        layoutPC4.addRow(self.tipoC4, self.tipoC4L)
        
        self.cantidad4.hide()        

        layoutPCantidad.addRow(self.cantidad4)
                    #--------------------------------------------------
                  #------------------------5--------------------------
        layoutPC5 = QFormLayout()
        self.cantidad5 = QWidget()
        self.cantidad5.setLayout(layoutPC5)
                  
        self.nombreC5 = QLabel("Nombre5: ", self)
        self.tipoC5 = QLabel("Campo5: ", self)
        self.nombreC5L = QLineEdit()
        layoutPC5.addRow(self.nombreC5, self.nombreC5L)  
        self.tipoC5L = QComboBox()
        layoutPC5.addRow(self.tipoC5L)
        self.tipoC5L.setFixedSize(100,20)
        self.tipoC5L.setCurrentIndex(200)
        self.tipoC5L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        self.tipoC5L.currentIndexChanged.connect(self.setvalue)
        layoutPC5.addRow(self.tipoC5, self.tipoC5L)
        
        self.cantidad5.hide()        

        layoutPCantidad.addRow(self.cantidad5)
                    #--------------------------------------------------
                  #-----------------------6---------------------------
        layoutPC6 = QFormLayout()
        self.cantidad6 = QWidget()
        self.cantidad6.setLayout(layoutPC6)                  
                  
        self.nombreC6 = QLabel("Nombre6: ", self)
        self.tipoC6 = QLabel("Campo6: ", self)
        self.nombreC6L = QLineEdit()
        layoutPC6.addRow(self.nombreC6, self.nombreC6L)  
        self.tipoC6L = QComboBox()
        layoutPC6.addRow(self.tipoC6L)
        self.tipoC6L.setFixedSize(100,20)
        self.tipoC6L.setCurrentIndex(200)
        self.tipoC6L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        self.tipoC6L.currentIndexChanged.connect(self.setvalue)
        layoutPC6.addRow(self.tipoC6, self.tipoC6L)
        
        self.cantidad6.hide()        

        layoutPCantidad.addRow(self.cantidad6)
                    #--------------------------------------------------
                  #----------------------7----------------------------
        layoutPC7 = QFormLayout()
        self.cantidad7 = QWidget()
        self.cantidad7.setLayout(layoutPC7)                  
                  
        self.nombreC7 = QLabel("Nombre7: ", self)
        self.tipoC7 = QLabel("Campo7: ", self)
        self.nombreC7L = QLineEdit()
        layoutPC7.addRow(self.nombreC7, self.nombreC7L)  
        self.tipoC7L = QComboBox()
        layoutPC7.addRow(self.tipoC7L)
        self.tipoC7L.setFixedSize(100,20)
        self.tipoC7L.setCurrentIndex(200)
        self.tipoC7L.addItems(["Texto", "Números", "DNI/NIE", "Núm Tel +34"])

        self.tipoC7L.currentIndexChanged.connect(self.setvalue)
        layoutPC7.addRow(self.tipoC7, self.tipoC7L)
        
        self.cantidad7.hide()        

        layoutPCantidad.addRow(self.cantidad7)
                    #--------------------------------------------------
                    
        self.botonGF = QPushButton("Generar Formulario")
        layoutPCantidad.addRow(self.botonGF)
        self.botonGF.clicked.connect(self.recogidaDatos)            
        
        #---------------------------------------Formulario Final----------------------------------------------
        layoutFormFf = QFormLayout()
        final = QWidget()
        final.setLayout(layoutFormFf)
        
        self.text1QLF = QLabel("Se ha generado el formulario")
        layoutFormFf.addRow(self.text1QLF)
        self.text2QLF = QLabel("¿Desea que se le muestre el código, o el fichero .html?")
        layoutFormFf.addRow(self.text2QLF)
        self.botonMC = QPushButton("Mostrar Código")
        layoutFormFf.addRow(self.botonMC)
        self.botonMC.clicked.connect(self.mostrarCodigo) 
        self.botonMF = QPushButton("Mostrar fichero")
        layoutFormFf.addRow(self.botonMF)
        self.botonMF.clicked.connect(self.mostrarFichero) 
        
        
        self.dock = QDockWidget()
        self.dock.setWindowTitle("Código:")
        self.campoC = QTextEdit("")
        self.dock.setWidget(self.campoC)
        self.dock.setHidden(True)
        layoutFormFf.addRow(self.dock)
        
        #-----------------------------------------Stacked Layout---------------------------------------
        self.capa = QStackedLayout()
        self.capa.addWidget(inicio)
        self.capa.addWidget(Pre)
        self.capa.addWidget(cantidad)
        self.capa.addWidget(register)
        self.capa.addWidget(login)
        self.capa.addWidget(final)

        layoutP.addLayout(self.capa)
        
    def mwhatsthis(self):
        QWhatsThis.enterWhatsThisMode()
        
    def hLogOut(self):
        self.logedin = False
        self.capa.setCurrentIndex(0)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F1:
            self.mwhatsthis()
    
    def irGitHub(self):
        webbrowser.open('https://github.com/TitoGHub/TFG')
    
    def mostrarCodigo(self):
        rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        rutaC = rutaEF + "/formulario.html"
        with open(rutaC, "r") as archivo:
            lineas = archivo.readlines()
    
        lineas_deseadas = lineas[8:-3]
    
        for lineas in lineas_deseadas:
            contenido = ''.join(lineas_deseadas) #solución encontrada en internet || lee cada linea y con el join lo añade..
        self.campoC.setText(contenido)
        self.dock.setHidden(False)
        
    def mostrarFichero(self):
        rutaF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        archivoF = 'formulario.html'
        print(rutaF)
        rutaFC = os.path.join(rutaF, archivoF)
        subprocess.Popen(['explorer', '/select,', rutaFC])
        
    def recogidaDatos(self):
        getvalue = self.cantidadItems.currentIndex()
        if getvalue > 4 and self.logedin == False:
            QMessageBox.critical(self, "Demasiados campos seleccionados", "Los guest, no pueden crear mas de 4 campos. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
        else:
            contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formulario</title>
    </head>
    <body>
        <h1>FORMULARIO</h1>
        <form>
            """
            rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(contenido_html)                    
                        
            for i in range(getvalue):
                if i == 0:
                    campo1 = self.nombreC1L.text()
                    textF1 = '<p>' + campo1 + ": </p>"
                    
                    tipo1 = self.tipoC1L.currentIndex()
                    if tipo1 == 0:
                        tipo1campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo1 == 1:
                        tipo1campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo1 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo1campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo1 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo1campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF1)
                        archivo.write("\n")
                        archivo.write(tipo1campo)
                        archivo.write("\n")
                        archivo.close()
                if i == 1:
                    campo2 = self.nombreC2L.text()
                    textF2 = '<p>' + campo2 + ": </p>"
                    
                    tipo2 = self.tipoC2L.currentIndex()
                    if tipo2 == 0:
                        tipo2campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo2 == 1:
                        tipo2campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo2 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo2campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo2 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo2campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF2)
                        archivo.write("\n")
                        archivo.write(tipo2campo)
                        archivo.write("\n")
                        archivo.close()
                if i == 2:
                    campo3 = self.nombreC3L.text()
                    textF3 = '<p>' + campo3 + ": </p>"
                    
                    tipo3 = self.tipoC3L.currentIndex()
                    if tipo3 == 0:
                        tipo3campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo3 == 1:
                        tipo3campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo3 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo3campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo3 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo3campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF3)
                        archivo.write("\n")
                        archivo.write(tipo3campo)
                        archivo.write("\n")
                        archivo.close()
                if i == 3:
                    campo4 = self.nombreC4L.text()
                    textF4 = '<p>' + campo4 + ": </p>"
                    
                    tipo4 = self.tipoC4L.currentIndex()
                    if tipo4 == 0:
                        tipo4campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo4 == 1:
                        tipo4campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo4 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo4campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo4 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo4campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF4)
                        archivo.write("\n")
                        archivo.write(tipo4campo)
                        archivo.write("\n")
                        archivo.close()
                if i == 4:
                    campo5 = self.nombreC5L.text()
                    textF5 = '<p>' + campo5 + ": </p>"
                    
                    tipo5 = self.tipoC5L.currentIndex()
                    if tipo5 == 0:
                        tipo5campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo5 == 1:
                        tipo5campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo5 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo5campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo5 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo5campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF5)
                        archivo.write("\n")
                        archivo.write(tipo5campo)
                        archivo.write("\n")
                        archivo.close()
                if i == 5:
                    campo6 = self.nombreC6L.text()
                    textF6 = '<p>' + campo6 + ": </p>"
                    
                    tipo6 = self.tipoC6L.currentIndex()
                    if tipo6 == 0:
                        tipo6campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo6 == 1:
                        tipo6campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo6 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo6campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo6 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo6campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF6)
                        archivo.write("\n")
                        archivo.write(tipo6campo)
                        archivo.write("\n")
                        archivo.close()
                if i == 6:
                    campo7 = self.nombreC7L.text()
                    textF7 = '<p>' + campo7 + ": </p>"
                    
                    tipo7 = self.tipoC7L.currentIndex()
                    if tipo7 == 0:
                        tipo1campo = '        <input type="text" id="campo" name="campo" pattern="[A-Za-z]+" placeholder="Ingrese solo letras" required><br>'
                    elif tipo7 == 1:
                        tipo7campo = '        <input type="number" id="campo" name="campo" pattern="[0-9]+" placeholder="Ingrese solo números" required><br>'
                    elif tipo7 == 2:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo7campo = '        <input type="text" pattern="^\d{8}[A-HJ-NP-TV-Za-hj-np-tv-z]$" placeholder="Ingrese un DNI válido (8 digitos + letra)" required><br>'
                    elif tipo7 == 3:
                        if self.logedin == False:
                            QMessageBox.critical(self, "Campo inválido", "Los guest, no pueden seleccionar esta plantilla. Mejore su cuenta registrandose.",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
                        else:
                            tipo7campo = '        <input type="tel" pattern="^\d{9}$" placeholder= "Ingrese un Número de telefono" required><br>'
                    else: 
                        print("metaestable")
                        
                    rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    with open(rutaEF +"/formulario.html", "a") as archivo:
                        archivo.write(textF7)
                        archivo.write("\n")
                        archivo.write(tipo7campo)
                        archivo.write("\n")
                        archivo.close()
                        
            contenido_html_final = """
            <br>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
                """
            rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            with open(rutaEF +"/formulario.html", "a") as archivo:
                    archivo.write(contenido_html_final)
                    
            self.capa.setCurrentIndex(5)
            
    def setvalue(self):
       getvalue = self.cantidadItems.currentIndex()

       if getvalue == 0:
        self.cantidad1.hide()
        self.cantidad2.hide() 
        self.cantidad3.hide() 
        self.cantidad4.hide() 
        self.cantidad5.hide() 
        self.cantidad6.hide() 
        self.cantidad7.hide()             
        
       elif getvalue == 1:
        self.cantidad1.show()
        self.cantidad2.hide() 
        self.cantidad3.hide() 
        self.cantidad4.hide() 
        self.cantidad5.hide() 
        self.cantidad6.hide() 
        self.cantidad7.hide()   
        
       elif getvalue == 2:
        self.cantidad1.show()
        self.cantidad2.show() 
        self.cantidad3.hide() 
        self.cantidad4.hide() 
        self.cantidad5.hide() 
        self.cantidad6.hide() 
        self.cantidad7.hide()   
       elif getvalue == 3:
        self.cantidad1.show()
        self.cantidad2.show()
        self.cantidad3.show()
        self.cantidad4.hide() 
        self.cantidad5.hide() 
        self.cantidad6.hide() 
        self.cantidad7.hide()   
       elif getvalue == 4:
        self.cantidad1.show()
        self.cantidad2.show()
        self.cantidad3.show()
        self.cantidad4.show()
        self.cantidad5.hide() 
        self.cantidad6.hide() 
        self.cantidad7.hide()   
       elif getvalue == 5:
        self.cantidad1.show()
        self.cantidad2.show()
        self.cantidad3.show() 
        self.cantidad4.show()
        self.cantidad5.show()
        self.cantidad6.hide() 
        self.cantidad7.hide()   
        
       elif getvalue == 6:
        self.cantidad1.show()
        self.cantidad2.show()
        self.cantidad3.show()
        self.cantidad4.show()
        self.cantidad5.show()
        self.cantidad6.show()
        self.cantidad7.hide()   
       else:
        self.cantidad1.show()
        self.cantidad2.show()
        self.cantidad3.show()
        self.cantidad4.show() 
        self.cantidad5.show() 
        self.cantidad6.show() 
        self.cantidad7.show() 
       
    def iniciar(self):
        self.capa.setCurrentIndex(1)
    
    def irRegistro(self):
        self.capa.setCurrentIndex(3)
        
    def irLogueo(self):
        self.capa.setCurrentIndex(4)
          
    def irCreacion(self):
        self.capa.setCurrentIndex(2)
        
    def registrar(self):
        registros = open ('usuariosRegistrados.txt', "a")
        textR =  self.usuarioQLr.text() + ";" + self.passwordr.text()  
        registros.write(textR)
        registros.write("\n")
        registros.close()
        self.capa.setCurrentIndex(1)
        
    def comprobar(self):
        comprobar = 0
        registros = open ('usuariosRegistrados.txt', "r+")
        registros.seek(0)
        
        #comprobación
        for linea in registros:
            name, passwd = linea.split(';') 
            if self.usuarioQL.text() == name and self.password.text() + "\n" == passwd : 
                comprobar = 1
                
        #If para seguir adelante o recibir un mensaje de Error
        if comprobar == 1:
                print("Usuario_login_correcto")
                self.logedin = True
                self.capa.setCurrentIndex(2)
        else:
                QMessageBox.critical(self, "Error Usuario/Contraseña", "El usuario y/o contraseña no se encuentra en nuestra base de datos",
                buttons=QMessageBox.Discard , defaultButton=QMessageBox.Discard)
        registros.close()

    def closeEvent(self, event):
        event.ignore()
        
        botones = QMessageBox.Yes | QMessageBox.No
        
        respuesta = QMessageBox.question(self, "¿Desea cerrar la aplicación?", "Al cerrar, se borrará el archivo .html, por lo que se recomienda guardarlo.", botones, QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            try:
                rutaEF = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                
                os.remove(rutaEF + "/formulario.html")
            except OSError as error:
              print("")
            event.accept()
        else:
            event.ignore()

        
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    favicon = QIcon("FWM.ico")
    ventana1.setWindowIcon(favicon)
    ventana1.resize(500, 600)
    ventana1.show()
    app.exec()