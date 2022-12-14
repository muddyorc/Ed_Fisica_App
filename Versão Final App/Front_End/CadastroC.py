# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginCadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 598)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setWindowIcon(QtGui.QIcon("Icons/Logo.png"))
        MainWindow.setStyleSheet("background-color:#E8E8E8;\n"
"border:none;\n"
"color: rgb(0, 0, 0);\n"
"")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.Pages.setMinimumSize(QtCore.QSize(450, 500))
        self.Pages.setMaximumSize(QtCore.QSize(450, 500))
        self.Pages.setObjectName("Pages")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Login)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.Login)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("Icons/Logo.png"))
        self.Logo.setObjectName("Logo")
        self.verticalLayout_4.addWidget(self.Logo, 0, QtCore.Qt.AlignHCenter)
        self.Titulo = QtWidgets.QLabel(self.frame)
        self.Titulo.setStyleSheet("")
        self.Titulo.setObjectName("Titulo")
        self.verticalLayout_4.addWidget(self.Titulo)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.Login)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LineUsername = QtWidgets.QLineEdit(self.frame_2)
        self.LineUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.LineUsername.setObjectName("LineUsername")
        self.verticalLayout_3.addWidget(self.LineUsername)
        self.LineEmail = QtWidgets.QLineEdit(self.frame_2)
        self.LineEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.LineEmail.setObjectName("LineEmail")
        self.verticalLayout_3.addWidget(self.LineEmail)
        self.LineSenha = QtWidgets.QLineEdit(self.frame_2)
        self.LineSenha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.LineSenha.setObjectName("LineSenha")
        self.verticalLayout_3.addWidget(self.LineSenha)
        self.Entrarconta = QtWidgets.QPushButton(self.frame_2)
        self.Entrarconta.setMinimumSize(QtCore.QSize(100, 30))
        self.Entrarconta.setMaximumSize(QtCore.QSize(100, 30))
        self.Entrarconta.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"QPushButton{\n"
"   color:rgb(255, 255, 255);\n"
"    background-color: rgb(164, 0, 0);\n"
"   border-radius:15px;\n"
"   \n"
"}")
        self.Entrarconta.setObjectName("Entrarconta")
        self.verticalLayout_3.addWidget(self.Entrarconta, 0, QtCore.Qt.AlignHCenter)
        self.Esqueceusenha = QtWidgets.QPushButton(self.frame_2)
        self.Esqueceusenha.setMinimumSize(QtCore.QSize(100, 20))
        self.Esqueceusenha.setMaximumSize(QtCore.QSize(150, 20))
        self.Esqueceusenha.setStyleSheet("QPushButton:hover{\n"
"    color: rgb(114, 159, 207);\n"
"   \n"
"}\n"
"\n"
"QPushButton{\n"
"   \n"
"    border:none\n"
"}")
        self.Esqueceusenha.setObjectName("Esqueceusenha")
        self.verticalLayout_3.addWidget(self.Esqueceusenha, 0, QtCore.Qt.AlignHCenter)
        self.Criarconta = QtWidgets.QPushButton(self.frame_2)
        self.Criarconta.setMinimumSize(QtCore.QSize(150, 20))
        self.Criarconta.setMaximumSize(QtCore.QSize(150, 20))
        self.Criarconta.setStyleSheet("QPushButton:hover{\n"
"    color: rgb(114, 159, 207);\n"
"   \n"
"}\n"
"\n"
"QPushButton{\n"
"   ;\n"
"    border:none\n"
"}")
        self.Criarconta.setObjectName("Criarconta")
        self.verticalLayout_3.addWidget(self.Criarconta, 0, QtCore.Qt.AlignHCenter)
        self.Loginerror = QtWidgets.QLabel(self.frame_2)
        self.Loginerror.setText("")
        self.Loginerror.setAlignment(QtCore.Qt.AlignCenter)
        self.Loginerror.setObjectName("Loginerror")
        self.verticalLayout_3.addWidget(self.Loginerror)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.Pages.addWidget(self.Login)
        self.Cadastro = QtWidgets.QWidget()
        self.Cadastro.setObjectName("Cadastro")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Cadastro)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.Cadastro)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 432, 482))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 400, 2173))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.LineConfirmarSenhaC = QtWidgets.QLineEdit(self.frame_3)
        self.LineConfirmarSenhaC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineConfirmarSenhaC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineConfirmarSenhaC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineConfirmarSenhaC.setObjectName("LineConfirmarSenhaC")
        self.gridLayout.addWidget(self.LineConfirmarSenhaC, 10, 0, 1, 1)
        self.LineSenhaC = QtWidgets.QLineEdit(self.frame_3)
        self.LineSenhaC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineSenhaC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineSenhaC.setText("")
        self.LineSenhaC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineSenhaC.setObjectName("LineSenhaC")
        self.gridLayout.addWidget(self.LineSenhaC, 9, 0, 1, 1)
        self.LineUsernameC = QtWidgets.QLineEdit(self.frame_3)
        self.LineUsernameC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineUsernameC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineUsernameC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineUsernameC.setObjectName("LineUsernameC")
        self.gridLayout.addWidget(self.LineUsernameC, 7, 0, 1, 1)
        self.LineEmailC = QtWidgets.QLineEdit(self.frame_3)
        self.LineEmailC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineEmailC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEmailC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineEmailC.setObjectName("LineEmailC")
        self.gridLayout.addWidget(self.LineEmailC, 8, 0, 1, 1)
        self.TituloC = QtWidgets.QLabel(self.frame_3)
        self.TituloC.setAlignment(QtCore.Qt.AlignCenter)
        self.TituloC.setObjectName("TituloC")
        self.gridLayout.addWidget(self.TituloC, 3, 0, 1, 1)
        self.LineNomeC = QtWidgets.QLineEdit(self.frame_3)
        self.LineNomeC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineNomeC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineNomeC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineNomeC.setObjectName("LineNomeC")
        self.gridLayout.addWidget(self.LineNomeC, 5, 0, 1, 1)
        self.LineSobrenomeC = QtWidgets.QLineEdit(self.frame_3)
        self.LineSobrenomeC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineSobrenomeC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineSobrenomeC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineSobrenomeC.setObjectName("LineSobrenomeC")
        self.gridLayout.addWidget(self.LineSobrenomeC, 6, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Tituloficha = QtWidgets.QLabel(self.frame_4)
        self.Tituloficha.setObjectName("Tituloficha")
        self.verticalLayout_8.addWidget(self.Tituloficha)
        self.TituloImc = QtWidgets.QLabel(self.frame_4)
        self.TituloImc.setStyleSheet("")
        self.TituloImc.setObjectName("TituloImc")
        self.verticalLayout_8.addWidget(self.TituloImc)
        self.LinePesoC = QtWidgets.QLineEdit(self.frame_4)
        self.LinePesoC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LinePesoC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LinePesoC.setAlignment(QtCore.Qt.AlignCenter)
        self.LinePesoC.setObjectName("LinePesoC")
        self.verticalLayout_8.addWidget(self.LinePesoC, 0, QtCore.Qt.AlignHCenter)
        self.LineAlturaC = QtWidgets.QLineEdit(self.frame_4)
        self.LineAlturaC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LineAlturaC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineAlturaC.setAlignment(QtCore.Qt.AlignCenter)
        self.LineAlturaC.setObjectName("LineAlturaC")
        self.verticalLayout_8.addWidget(self.LineAlturaC, 0, QtCore.Qt.AlignHCenter)
        self.Titulodiario = QtWidgets.QLabel(self.frame_4)
        self.Titulodiario.setObjectName("Titulodiario")
        self.verticalLayout_8.addWidget(self.Titulodiario)
        self.TituloTrabalho = QtWidgets.QLabel(self.frame_4)
        self.TituloTrabalho.setStyleSheet("")
        self.TituloTrabalho.setObjectName("TituloTrabalho")
        self.verticalLayout_8.addWidget(self.TituloTrabalho)
        self.bt20 = QtWidgets.QCheckBox(self.frame_4)
        self.bt20.setStyleSheet("")
        self.bt20.setObjectName("bt20")
        self.Btn_Htrabalho = QtWidgets.QButtonGroup(MainWindow)
        self.Btn_Htrabalho.setObjectName("Btn_Htrabalho")
        self.Btn_Htrabalho.addButton(self.bt20)
        self.verticalLayout_8.addWidget(self.bt20)
        self.bt40 = QtWidgets.QCheckBox(self.frame_4)
        self.bt40.setStyleSheet("")
        self.bt40.setObjectName("bt40")
        self.Btn_Htrabalho.addButton(self.bt40)
        self.verticalLayout_8.addWidget(self.bt40)
        self.bt60 = QtWidgets.QCheckBox(self.frame_4)
        self.bt60.setStyleSheet("")
        self.bt60.setObjectName("bt60")
        self.Btn_Htrabalho.addButton(self.bt60)
        self.verticalLayout_8.addWidget(self.bt60)
        self.btnaoTrabalhar = QtWidgets.QCheckBox(self.frame_4)
        self.btnaoTrabalhar.setStyleSheet("")
        self.btnaoTrabalhar.setObjectName("btnaoTrabalhar")
        self.Btn_Htrabalho.addButton(self.btnaoTrabalhar)
        self.verticalLayout_8.addWidget(self.btnaoTrabalhar)
        self.Titulofuncao = QtWidgets.QLabel(self.frame_4)
        self.Titulofuncao.setObjectName("Titulofuncao")
        self.verticalLayout_8.addWidget(self.Titulofuncao)
        self.btficarsentado = QtWidgets.QCheckBox(self.frame_4)
        self.btficarsentado.setStyleSheet("")
        self.btficarsentado.setObjectName("btficarsentado")
        self.verticalLayout_8.addWidget(self.btficarsentado)
        self.btcarregarpeso = QtWidgets.QCheckBox(self.frame_4)
        self.btcarregarpeso.setStyleSheet("")
        self.btcarregarpeso.setObjectName("btcarregarpeso")
        self.verticalLayout_8.addWidget(self.btcarregarpeso)
        self.btcaminhar = QtWidgets.QCheckBox(self.frame_4)
        self.btcaminhar.setStyleSheet("")
        self.btcaminhar.setObjectName("btcaminhar")
        self.verticalLayout_8.addWidget(self.btcaminhar)
        self.btficarempe = QtWidgets.QCheckBox(self.frame_4)
        self.btficarempe.setStyleSheet("")
        self.btficarempe.setObjectName("btficarempe")
        self.verticalLayout_8.addWidget(self.btficarempe)
        self.btOutros1 = QtWidgets.QCheckBox(self.frame_4)
        self.btOutros1.setStyleSheet("")
        self.btOutros1.setObjectName("btOutros1")
        self.verticalLayout_8.addWidget(self.btOutros1)
        self.desempenho = QtWidgets.QLabel(self.frame_4)
        self.desempenho.setObjectName("desempenho")
        self.verticalLayout_8.addWidget(self.desempenho)
        self.infor_desempenho = QtWidgets.QLineEdit(self.frame_4)
        self.infor_desempenho.setMinimumSize(QtCore.QSize(0, 50))
        self.infor_desempenho.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_desempenho.setObjectName("infor_desempenho")
        self.verticalLayout_8.addWidget(self.infor_desempenho)
        self.TituloMedico = QtWidgets.QLabel(self.frame_4)
        self.TituloMedico.setObjectName("TituloMedico")
        self.verticalLayout_8.addWidget(self.TituloMedico)
        self.Titulocirurgias = QtWidgets.QLabel(self.frame_4)
        self.Titulocirurgias.setObjectName("Titulocirurgias")
        self.verticalLayout_8.addWidget(self.Titulocirurgias)
        self.btcoluna = QtWidgets.QCheckBox(self.frame_4)
        self.btcoluna.setStyleSheet("")
        self.btcoluna.setObjectName("btcoluna")
        self.verticalLayout_8.addWidget(self.btcoluna)
        self.btrim = QtWidgets.QCheckBox(self.frame_4)
        self.btrim.setStyleSheet("")
        self.btrim.setObjectName("btrim")
        self.verticalLayout_8.addWidget(self.btrim)
        self.btcoracao = QtWidgets.QCheckBox(self.frame_4)
        self.btcoracao.setStyleSheet("")
        self.btcoracao.setObjectName("btcoracao")
        self.verticalLayout_8.addWidget(self.btcoracao)
        self.btpulmao = QtWidgets.QCheckBox(self.frame_4)
        self.btpulmao.setStyleSheet("")
        self.btpulmao.setObjectName("btpulmao")
        self.verticalLayout_8.addWidget(self.btpulmao)
        self.btNenhum1 = QtWidgets.QCheckBox(self.frame_4)
        self.btNenhum1.setStyleSheet("")
        self.btNenhum1.setObjectName("btNenhum1")
        self.verticalLayout_8.addWidget(self.btNenhum1)
        self.btOutros2 = QtWidgets.QCheckBox(self.frame_4)
        self.btOutros2.setStyleSheet("")
        self.btOutros2.setObjectName("btOutros2")
        self.verticalLayout_8.addWidget(self.btOutros2)
        self.cirurgia = QtWidgets.QLabel(self.frame_4)
        self.cirurgia.setObjectName("cirurgia")
        self.verticalLayout_8.addWidget(self.cirurgia)
        self.infor_cirurgia = QtWidgets.QLineEdit(self.frame_4)
        self.infor_cirurgia.setMinimumSize(QtCore.QSize(0, 50))
        self.infor_cirurgia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_cirurgia.setObjectName("infor_cirurgia")
        self.verticalLayout_8.addWidget(self.infor_cirurgia)
        self.Titulodiagnostico = QtWidgets.QLabel(self.frame_4)
        self.Titulodiagnostico.setObjectName("Titulodiagnostico")
        self.verticalLayout_8.addWidget(self.Titulodiagnostico)
        self.btAlcool = QtWidgets.QCheckBox(self.frame_4)
        self.btAlcool.setStyleSheet("")
        self.btAlcool.setObjectName("btAlcool")
        self.verticalLayout_8.addWidget(self.btAlcool)
        self.btArtrite = QtWidgets.QCheckBox(self.frame_4)
        self.btArtrite.setStyleSheet("")
        self.btArtrite.setObjectName("btArtrite")
        self.verticalLayout_8.addWidget(self.btArtrite)
        self.btDiabete = QtWidgets.QCheckBox(self.frame_4)
        self.btDiabete.setStyleSheet("")
        self.btDiabete.setObjectName("btDiabete")
        self.verticalLayout_8.addWidget(self.btDiabete)
        self.btRenal = QtWidgets.QCheckBox(self.frame_4)
        self.btRenal.setStyleSheet("")
        self.btRenal.setObjectName("btRenal")
        self.verticalLayout_8.addWidget(self.btRenal)
        self.btNenhum2 = QtWidgets.QCheckBox(self.frame_4)
        self.btNenhum2.setStyleSheet("")
        self.btNenhum2.setObjectName("btNenhum2")
        self.verticalLayout_8.addWidget(self.btNenhum2)
        self.btOutros3 = QtWidgets.QCheckBox(self.frame_4)
        self.btOutros3.setStyleSheet("")
        self.btOutros3.setObjectName("btOutros3")
        self.verticalLayout_8.addWidget(self.btOutros3)
        self.diagnostico = QtWidgets.QLabel(self.frame_4)
        self.diagnostico.setObjectName("diagnostico")
        self.verticalLayout_8.addWidget(self.diagnostico)
        self.infor_diagnostico = QtWidgets.QLineEdit(self.frame_4)
        self.infor_diagnostico.setMinimumSize(QtCore.QSize(0, 50))
        self.infor_diagnostico.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_diagnostico.setObjectName("infor_diagnostico")
        self.verticalLayout_8.addWidget(self.infor_diagnostico)
        self.TituloFamiliar = QtWidgets.QLabel(self.frame_4)
        self.TituloFamiliar.setObjectName("TituloFamiliar")
        self.verticalLayout_8.addWidget(self.TituloFamiliar)
        self.btmae = QtWidgets.QCheckBox(self.frame_4)
        self.btmae.setStyleSheet("")
        self.btmae.setObjectName("btmae")
        self.verticalLayout_8.addWidget(self.btmae)
        self.btpai = QtWidgets.QCheckBox(self.frame_4)
        self.btpai.setStyleSheet("")
        self.btpai.setObjectName("btpai")
        self.verticalLayout_8.addWidget(self.btpai)
        self.btirmao = QtWidgets.QCheckBox(self.frame_4)
        self.btirmao.setObjectName("btirmao")
        self.verticalLayout_8.addWidget(self.btirmao)
        self.btavo = QtWidgets.QCheckBox(self.frame_4)
        self.btavo.setObjectName("btavo")
        self.verticalLayout_8.addWidget(self.btavo)
        self.familia = QtWidgets.QLabel(self.frame_4)
        self.familia.setObjectName("familia")
        self.verticalLayout_8.addWidget(self.familia)
        self.infor_familiahisto = QtWidgets.QLineEdit(self.frame_4)
        self.infor_familiahisto.setMinimumSize(QtCore.QSize(0, 50))
        self.infor_familiahisto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_familiahisto.setObjectName("infor_familiahisto")
        self.verticalLayout_8.addWidget(self.infor_familiahisto)
        self.Ttuloalergia = QtWidgets.QLabel(self.frame_4)
        self.Ttuloalergia.setObjectName("Ttuloalergia")
        self.verticalLayout_8.addWidget(self.Ttuloalergia)
        self.btsimalergia = QtWidgets.QCheckBox(self.frame_4)
        self.btsimalergia.setStyleSheet("")
        self.btsimalergia.setObjectName("btsimalergia")
        self.Btn_Alergia = QtWidgets.QButtonGroup(MainWindow)
        self.Btn_Alergia.setObjectName("Btn_Alergia")
        self.Btn_Alergia.addButton(self.btsimalergia)
        self.verticalLayout_8.addWidget(self.btsimalergia)
        self.btnaoalergia = QtWidgets.QCheckBox(self.frame_4)
        self.btnaoalergia.setStyleSheet("")
        self.btnaoalergia.setObjectName("btnaoalergia")
        self.Btn_Alergia.addButton(self.btnaoalergia)
        self.verticalLayout_8.addWidget(self.btnaoalergia)
        self.alergia = QtWidgets.QLabel(self.frame_4)
        self.alergia.setObjectName("alergia")
        self.verticalLayout_8.addWidget(self.alergia)
        self.infor_alergia = QtWidgets.QLineEdit(self.frame_4)
        self.infor_alergia.setMinimumSize(QtCore.QSize(0, 50))
        self.infor_alergia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_alergia.setObjectName("infor_alergia")
        self.verticalLayout_8.addWidget(self.infor_alergia)
        self.Titulorestricao = QtWidgets.QLabel(self.frame_4)
        self.Titulorestricao.setObjectName("Titulorestricao")
        self.verticalLayout_8.addWidget(self.Titulorestricao)
        self.btsimrestri = QtWidgets.QCheckBox(self.frame_4)
        self.btsimrestri.setStyleSheet("")
        self.btsimrestri.setObjectName("btsimrestri")
        self.Btn_Rfisico = QtWidgets.QButtonGroup(MainWindow)
        self.Btn_Rfisico.setObjectName("Btn_Rfisico")
        self.Btn_Rfisico.addButton(self.btsimrestri)
        self.verticalLayout_8.addWidget(self.btsimrestri)
        self.btnaorestri = QtWidgets.QCheckBox(self.frame_4)
        self.btnaorestri.setStyleSheet("")
        self.btnaorestri.setObjectName("btnaorestri")
        self.Btn_Rfisico.addButton(self.btnaorestri)
        self.verticalLayout_8.addWidget(self.btnaorestri)
        self.restricao = QtWidgets.QLabel(self.frame_4)
        self.restricao.setObjectName("restricao")
        self.verticalLayout_8.addWidget(self.restricao)
        self.infor_restricao = QtWidgets.QLineEdit(self.frame_4)
        self.infor_restricao.setMinimumSize(QtCore.QSize(0, 50))
        self.infor_restricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_restricao.setText("")
        self.infor_restricao.setObjectName("infor_restricao")
        self.verticalLayout_8.addWidget(self.infor_restricao)
        self.Tituloideal = QtWidgets.QLabel(self.frame_4)
        self.Tituloideal.setObjectName("Tituloideal")
        self.verticalLayout_8.addWidget(self.Tituloideal)
        self.Tituloobjetivo = QtWidgets.QLabel(self.frame_4)
        self.Tituloobjetivo.setObjectName("Tituloobjetivo")
        self.verticalLayout_8.addWidget(self.Tituloobjetivo)
        self.btestetica = QtWidgets.QCheckBox(self.frame_4)
        self.btestetica.setStyleSheet("")
        self.btestetica.setObjectName("btestetica")
        self.Btn_Objfisico = QtWidgets.QButtonGroup(MainWindow)
        self.Btn_Objfisico.setObjectName("Btn_Objfisico")
        self.Btn_Objfisico.addButton(self.btestetica)
        self.verticalLayout_8.addWidget(self.btestetica)
        self.btlazer = QtWidgets.QCheckBox(self.frame_4)
        self.btlazer.setStyleSheet("")
        self.btlazer.setObjectName("btlazer")
        self.Btn_Objfisico.addButton(self.btlazer)
        self.verticalLayout_8.addWidget(self.btlazer)
        self.btemagrecer = QtWidgets.QCheckBox(self.frame_4)
        self.btemagrecer.setStyleSheet("")
        self.btemagrecer.setObjectName("btemagrecer")
        self.Btn_Objfisico.addButton(self.btemagrecer)
        self.verticalLayout_8.addWidget(self.btemagrecer)
        self.btcondicionamento = QtWidgets.QCheckBox(self.frame_4)
        self.btcondicionamento.setStyleSheet("")
        self.btcondicionamento.setObjectName("btcondicionamento")
        self.Btn_Objfisico.addButton(self.btcondicionamento)
        self.verticalLayout_8.addWidget(self.btcondicionamento)
        self.btterapeu = QtWidgets.QCheckBox(self.frame_4)
        self.btterapeu.setStyleSheet("")
        self.btterapeu.setObjectName("btterapeu")
        self.Btn_Objfisico.addButton(self.btterapeu)
        self.verticalLayout_8.addWidget(self.btterapeu)
        self.btOutros4 = QtWidgets.QCheckBox(self.frame_4)
        self.btOutros4.setStyleSheet("")
        self.btOutros4.setObjectName("btOutros4")
        self.Btn_Objfisico.addButton(self.btOutros4)
        self.verticalLayout_8.addWidget(self.btOutros4)
        self.objetivo = QtWidgets.QLabel(self.frame_4)
        self.objetivo.setObjectName("objetivo")
        self.verticalLayout_8.addWidget(self.objetivo)
        self.Infor_objetivo = QtWidgets.QLineEdit(self.frame_4)
        self.Infor_objetivo.setMinimumSize(QtCore.QSize(0, 50))
        self.Infor_objetivo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Infor_objetivo.setObjectName("Infor_objetivo")
        self.verticalLayout_8.addWidget(self.Infor_objetivo)
        self.Titulogeral = QtWidgets.QLabel(self.frame_4)
        self.Titulogeral.setObjectName("Titulogeral")
        self.verticalLayout_8.addWidget(self.Titulogeral)
        self.infor_geral = QtWidgets.QLineEdit(self.frame_4)
        self.infor_geral.setMinimumSize(QtCore.QSize(0, 60))
        self.infor_geral.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.infor_geral.setObjectName("infor_geral")
        self.verticalLayout_8.addWidget(self.infor_geral)
        self.CriarcontaC = QtWidgets.QPushButton(self.frame_4)
        self.CriarcontaC.setMinimumSize(QtCore.QSize(100, 30))
        self.CriarcontaC.setMaximumSize(QtCore.QSize(100, 30))
        self.CriarcontaC.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"QPushButton{\n"
"   color:rgb(255, 255, 255);\n"
"    background-color: rgb(164, 0, 0);\n"
"    border-radius:15px;\n"
"   \n"
"}")
        self.CriarcontaC.setObjectName("CriarcontaC")
        self.verticalLayout_8.addWidget(self.CriarcontaC, 0, QtCore.Qt.AlignHCenter)
        self.BtnVoltarCadastro = QtWidgets.QPushButton(self.frame_4)
        self.BtnVoltarCadastro.setStyleSheet("QPushButton:hover{\n"
"    color: rgb(114, 159, 207);\n"
"   \n"
"}\n"
"\n"
"QPushButton{\n"
"   \n"
"    border:none\n"
"}")
        self.BtnVoltarCadastro.setObjectName("BtnVoltarCadastro")
        self.verticalLayout_8.addWidget(self.BtnVoltarCadastro)
        self.Erroinfo1 = QtWidgets.QLabel(self.frame_4)
        self.Erroinfo1.setText("")
        self.Erroinfo1.setObjectName("Erroinfo1")
        self.verticalLayout_8.addWidget(self.Erroinfo1)
        self.Erroinfo = QtWidgets.QLabel(self.frame_4)
        self.Erroinfo.setText("")
        self.Erroinfo.setObjectName("Erroinfo")
        self.verticalLayout_8.addWidget(self.Erroinfo)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.Pages.addWidget(self.Cadastro)
        self.verticalLayout.addWidget(self.Pages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Oficina do Corpo em Movimento</span></p></body></html>"))
        self.LineUsername.setPlaceholderText(_translate("MainWindow", "Username"))
        self.LineEmail.setPlaceholderText(_translate("MainWindow", "Email"))
        self.LineSenha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.Entrarconta.setText(_translate("MainWindow", "Entrar"))
        self.Esqueceusenha.setText(_translate("MainWindow", "Esqueceu sua senha?"))
        self.Criarconta.setText(_translate("MainWindow", "Criar conta"))
        self.LineConfirmarSenhaC.setPlaceholderText(_translate("MainWindow", "Confirmar Senha"))
        self.LineSenhaC.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.LineUsernameC.setPlaceholderText(_translate("MainWindow", "Username"))
        self.LineEmailC.setPlaceholderText(_translate("MainWindow", "Email"))
        self.TituloC.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Conta</span></p></body></html>"))
        self.LineNomeC.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.LineSobrenomeC.setPlaceholderText(_translate("MainWindow", "Sobrenome"))
        self.Tituloficha.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; \">Ficha de Anamnese</span></p></body></html>"))
        self.TituloImc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">IMC Corporal</span></p></body></html>"))
        self.LinePesoC.setPlaceholderText(_translate("MainWindow", "Peso"))
        self.LineAlturaC.setPlaceholderText(_translate("MainWindow", "Altura"))
        self.Titulodiario.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Atividades da Vida D??aria</span></p></body></html>"))
        self.TituloTrabalho.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">N??mero de Horas de Trabalho por Semana?</span></p></body></html>"))
        self.bt20.setText(_translate("MainWindow", "Menos de 20"))
        self.bt40.setText(_translate("MainWindow", "20 a 40"))
        self.bt60.setText(_translate("MainWindow", "41 a 60"))
        self.btnaoTrabalhar.setText(_translate("MainWindow", "N??o Trabalho"))
        self.Titulofuncao.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Atividades desempenhadas no Trabalho?</span></p></body></html>"))
        self.btficarsentado.setText(_translate("MainWindow", "Ficar Sentado"))
        self.btcarregarpeso.setText(_translate("MainWindow", "Carregar Peso"))
        self.btcaminhar.setText(_translate("MainWindow", "Caminhar"))
        self.btficarempe.setText(_translate("MainWindow", "Ficar em P??"))
        self.btOutros1.setText(_translate("MainWindow", "Outros"))
        self.desempenho.setText(_translate("MainWindow", "Qual(is):"))
        self.TituloMedico.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; \">Hist??rico M??dico</span></p></body></html>"))
        self.Titulocirurgias.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Interven????es Cir??rgicas?</span></p></body></html>"))
        self.btcoluna.setText(_translate("MainWindow", "Coluna"))
        self.btrim.setText(_translate("MainWindow", "Rim"))
        self.btcoracao.setText(_translate("MainWindow", "Cora????o "))
        self.btpulmao.setText(_translate("MainWindow", "Pulm??o"))
        self.btNenhum1.setText(_translate("MainWindow", "Nenhum"))
        self.btOutros2.setText(_translate("MainWindow", "Outros"))
        self.cirurgia.setText(_translate("MainWindow", "Qual(is):"))
        self.Titulodiagnostico.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Problemas Diagnosticados?</span></p></body></html>"))
        self.btAlcool.setText(_translate("MainWindow", "Alcoolismo"))
        self.btArtrite.setText(_translate("MainWindow", "Artrite"))
        self.btDiabete.setText(_translate("MainWindow", "Diabetes"))
        self.btRenal.setText(_translate("MainWindow", "Problema Renal"))
        self.btNenhum2.setText(_translate("MainWindow", "Nenhum"))
        self.btOutros3.setText(_translate("MainWindow", "Outros"))
        self.diagnostico.setText(_translate("MainWindow", "Qual(is):"))
        self.TituloFamiliar.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Hist??rico Familiar? </span></p></body></html>"))
        self.btmae.setText(_translate("MainWindow", "M??e"))
        self.btpai.setText(_translate("MainWindow", "Pai"))
        self.btirmao.setText(_translate("MainWindow", "Irm??o(??)"))
        self.btavo.setText(_translate("MainWindow", "Av??/Av??"))
        self.familia.setText(_translate("MainWindow", "Qual(is):"))
        self.Ttuloalergia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; ;\">Possui Alergia?</span></p></body></html>"))
        self.btsimalergia.setText(_translate("MainWindow", "Sim"))
        self.btnaoalergia.setText(_translate("MainWindow", "N??o"))
        self.alergia.setText(_translate("MainWindow", "Qual(is):"))
        self.Titulorestricao.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Possui restri????o para atividades f??sicas?</span></p></body></html>"))
        self.btsimrestri.setText(_translate("MainWindow", "Sim"))
        self.btnaorestri.setText(_translate("MainWindow", "N??o"))
        self.restricao.setText(_translate("MainWindow", "Qual(is):"))
        self.Tituloideal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Plano Ideal</span></p></body></html>"))
        self.Tituloobjetivo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Objetivo em rela????o a atividade f??sica?</span></p></body></html>"))
        self.btestetica.setText(_translate("MainWindow", "Est??tica"))
        self.btlazer.setText(_translate("MainWindow", "Lazer"))
        self.btemagrecer.setText(_translate("MainWindow", "Emagrecimento"))
        self.btcondicionamento.setText(_translate("MainWindow", "Condicionamento f??sico"))
        self.btterapeu.setText(_translate("MainWindow", "Terap??utico"))
        self.btOutros4.setText(_translate("MainWindow", "Outros"))
        self.objetivo.setText(_translate("MainWindow", "Qual:"))
        self.Titulogeral.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; \">Coment??rios Gerais</span></p></body></html>"))
        self.CriarcontaC.setText(_translate("MainWindow", "Criar"))
        self.BtnVoltarCadastro.setText(_translate("MainWindow", "Voltar"))

