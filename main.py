from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class DeskTop:
    
    @staticmethod
    def validedacion(vezes, userId, window):
        from bot import AutomationBot
        AutomationBot.startAutomation(vezes, userId)
        if vezes == "" or userId == "":
            QMessageBox.critical(window, "Erro", "Por favor, insira valores válidos.")
            return
        
      
        QMessageBox.information(window, "Informação", "Script iniciado.")
    
    @staticmethod 
    def App():
       
        app = QApplication([])


        window = DeskTop.screenHomeCreate()


        window.show()
        app.exec_()

    @staticmethod 
    def screenHomeCreate():
        window = QWidget()
        window.setWindowTitle('Tela de Entrada')

       
        layout = QVBoxLayout()

      
      
        input_vezes = QLineEdit()
        input_userId = QLineEdit()

       
        button_start = QPushButton('Start')

     
        def on_click():
            vezes = input_vezes.text()
            userId = input_userId.text()
            DeskTop.validedacion(vezes, userId, window)

        button_start.clicked.connect(on_click)

       
        layout.addWidget(input_vezes)
        layout.addWidget(input_userId)
        layout.addWidget(button_start)

      
        window.setLayout(layout)

        return window


DeskTop.App()
