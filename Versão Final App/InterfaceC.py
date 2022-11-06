import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Front_End.CadastroC import Ui_LoginCadastro
from Front_End.Princi import Ui_MainWindow2
from PyQt5 import QtCore, QtTest, QtGui, QtWidgets
import Server
import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

Server


# Janelas de Login e Cadastro
class LoginCadastro(QMainWindow, Ui_LoginCadastro):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("OCM")
        self.setFixedSize(468, 560)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.move(
            QtWidgets.QApplication.desktop().screen().rect().center()
            - self.rect().center()
        )

        # Caso o servidor esteja conectado os botões irão funcionar normalmente
        if Server.server == True:
            self.Entrarconta.clicked.connect(lambda: self.login())
            self.Criarconta.clicked.connect(
                lambda: self.Pages.setCurrentWidget(self.Cadastro)
            )
            self.CriarcontaC.clicked.connect(lambda: self.validacao())
            self.BtnVoltarCadastro.clicked.connect(
                lambda: self.Pages.setCurrentWidget(self.Login)
            )

        # Caso não o botão de entrar ira abrir a janela principal diretamente e os outros não irão executar
        else:
            self.Entrarconta.clicked.connect(lambda: self.open())

    # Função de validação da criação de conta
    def validacao(self):
        # Variaveis para identificação de erros
        no = 0  # Nome
        sobno = 0  # Sobrenome
        user = 0  # Username
        em = 0  # Email
        se = 0  # Senha
        secon = 0  # Confirmar Senha

        # Variaveis da anamnese
        pe = 0  # Peso
        alt = 0  # Altura
        hortrabsem = 0  # Horas de Trabalho por Semana
        atdesemp = 0  # Atividades desempenhadas no Trabalho
        intcirur = 0  # Intervenções Cirúrgicas
        probdiag = 0  # Problemas Diagnosticados
        histfami = 0  # Historico Familiar
        posaler = 0  # Possui Alergia
        restpatfis = 0  # Restrição para atividades físicas
        objatfis = 0  # Objetivo

        t = QtCore.QTimer()
        # Variaveis que receberão as informações da conta
        self.nome = self.LineNomeC.text()
        self.sobrenome = self.LineSobrenomeC.text()
        self.username = self.LineUsernameC.text()
        self.eemai = self.LineEmailC.text()
        self.senha = self.LineSenhaC.text()
        self.senhacon = self.LineConfirmarSenhaC.text()

        if self.nome == "":
            no = 1
        else:
            no = 5

        if self.sobrenome == "":
            sobno = 1
        else:
            sobno = 5

        if self.username == "":
            user = 1
        else:
            try:
                Server.cursor.execute(
                    f"""SELECT Username FROM conta WHERE Username='{self.username}';"""
                )
                ser = Server.cursor.fetchone()
                if ser[0] == self.username:
                    user = 2
            except:
                user = 5

        if self.eemai == "":
            em = 1
        else:
            if re.search(regex, self.eemai):
                try:
                    Server.cursor.execute(
                        f"""SELECT Email FROM conta WHERE Email='{self.eemai}';"""
                    )
                    ser = Server.cursor.fetchone()
                    if ser[0] == self.eemai:
                        em = 2
                except:
                    em = 5
            else:
                em = 3

        if self.senha == "":
            se = 1
        else:
            if self.senha == self.senhacon:
                se = 5
            else:
                se = 3

        if self.senhacon == "":
            secon = 1
        else:
            secon = 5

        # Acões que irão ocorrer caso uma variavel de erro seja diferente de 0
        if no and sobno and user and em and se and secon == 1:
            self.Erroinfo1.setText("As informações estão em branco")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif no and sobno and user == 1:
            self.Erroinfo1.setText("Os nomes da conta estão em branco")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif no and sobno == 1:
            self.Erroinfo1.setText("Nome e Sobrenome estão em branco")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif no == 1:
            self.Erroinfo1.setText("Nome está em branco")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif sobno == 1:
            self.Erroinfo1.setText("Sobrenome está em branco")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif user == 1:
            self.Erroinfo1.setText("Username está em branco")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif em and se == 1:
            self.Erroinfo1.setText("Email e senha devem ser preenchidos")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif em == 1:
            self.Erroinfo1.setText("Email deve ser preenchido")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif se == 1:
            self.Erroinfo1.setText("Senha deve ser preenchida")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")

        if em == 2:
            self.Erroinfo1.setText("Já existe uma conta com esse email")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")
        elif user == 2:
            self.Erroinfo1.setText("Este nome de usuario já está sendo usado")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")

        if se == 3:
            self.Erroinfo1.setText("Senhas estão diferentes")
            self.Erroinfo1.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Erroinfo1.setText("")
            self.Erroinfo1.setStyleSheet("background-color: #E8E8E8;")

        if no == 5 and sobno == 5 and user == 5 and em == 5 and se == 5 and secon == 5:
            self.enviar()
        else:
            pass

    # Função de envio das informações da conta
    def enviar(self):
        Server.cursor.execute(
            f"""INSERT INTO conta(id,Nome,Sobrenome,Username,Email,Senha) VALUES(default,'{self.nome}','{self.sobrenome}','{self.username}','{self.eemai}','{self.senha}');"""
        )
        Server.conexao.commit()
        self.Pages.setCurrentWidget(self.Login)
        self.Loginerror.setText("Conta criada com sucesso")
        self.Loginerror.setStyleSheet("color:green")
        QtTest.QTest.qWait(3000)
        self.Loginerror.setText("")
        self.Loginerror.setStyleSheet("background-color: #E8E8E8;")

    # Função de verificação de login
    def login(self):
        # Variaveis para a identificação
        self.lunome = self.LineUsername.text()
        self.lemail = self.LineEmail.text()
        self.lsenha = self.LineSenha.text()
        cno = 0
        cem = 0
        cse = 0

        if self.lunome == "":
            self.Loginerror.setText("Username não especificado")
            self.Loginerror.setStyleSheet("color:red")
            QtTest.QTest.qWait(3000)
            self.Loginerror.setText("")
            self.Loginerror.setStyleSheet("background-color: #E8E8E8;")
        else:
            try:
                Server.cursor.execute(
                    f"""SELECT Username FROM conta WHERE Username='{self.lunome}';"""
                )
                ser = Server.cursor.fetchone()
                if ser[0] == self.lunome:
                    cno = 1
                    if self.lemail == "":
                        self.Loginerror.setText("O Email deve ser especificado")
                        self.Loginerror.setStyleSheet("color:red")
                        QtTest.QTest.qWait(3000)
                        self.Loginerror.setText("")
                        self.Loginerror.setStyleSheet("background-color: #E8E8E8;")
                    else:
                        try:
                            Server.cursor.execute(
                                f"""SELECT Email FROM conta WHERE Username='{self.lunome}';"""
                            )
                            ser = Server.cursor.fetchone()
                            if ser[0] == self.lemail:
                                cem = 1
                                if self.lsenha == "":
                                    self.Loginerror.setText("Senha está em branco")
                                    self.Loginerror.setStyleSheet("color:red")
                                    QtTest.QTest.qWait(3000)
                                    self.Loginerror.setText("")
                                    self.Loginerror.setStyleSheet(
                                        "background-color: #E8E8E8;"
                                    )
                                else:
                                    try:
                                        Server.cursor.execute(
                                            f"""SELECT Senha FROM conta WHERE Username='{self.lunome}';"""
                                        )
                                        ser = Server.cursor.fetchone()
                                        if ser[0] == self.lsenha:
                                            cse = 1
                                        else:
                                            self.Loginerror.setText("Senha incorreta")
                                            self.Loginerror.setStyleSheet("color:red")
                                            QtTest.QTest.qWait(3000)
                                            self.Loginerror.setText("")
                                            self.Loginerror.setStyleSheet(
                                                "background-color: #E8E8E8;"
                                            )
                                    except:
                                        pass
                        except:
                            self.Loginerror.setText("Email incorreto")
                            self.Loginerror.setStyleSheet("color:red")
                            QtTest.QTest.qWait(3000)
                            self.Loginerror.setText("")
                            self.Loginerror.setStyleSheet("background-color: #E8E8E8;")
            except:
                self.Loginerror.setText("Username não cadastrado")
                self.Loginerror.setStyleSheet("color:red")
                QtTest.QTest.qWait(3000)
                self.Loginerror.setText("")
                self.Loginerror.setStyleSheet("background-color: #E8E8E8;")

        # O usuario só sera logado caso todos as variaveis de identificação estjam no 1
        if cno == 1 and cem == 1 and cse == 1:
            self.nuconfir = 1
            self.open()

    # Função de transição de janela
    def open(self):
        if Server.server == True:
            try:
                if self.nuconfir == 1:
                    self.w = MainWindow2()
                    self.w.show()
                    self.close()
                else:
                    exit()
            except:
                pass
        else:
            self.w = MainWindow2()
            self.w.show()
            self.close()


# Janela Principal do Aplicativo
class MainWindow2(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("OCM")
        self.showFullScreen()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Menu Expansivo
        self.ABTN.clicked.connect(self.MLeft)
        self.Mensagem_Email.clicked.connect(self.Mmeils)
        self.btselecionaralimento.clicked.connect(self.Mcomida)
        self.bteditartreino.clicked.connect(self.MMenutreinar)

        # Caixas de Escolha da Janela de Treino
        self.comboBox.currentTextChanged.connect(self.Treino_explicacao)
        self.comboBox_2.currentTextChanged.connect(self.Treino_explicacao)
        self.comboBox_3.currentTextChanged.connect(self.Treino_explicacao)
        self.btsalvaralimento.clicked.connect(self.Dieta_recomendado)
        self.btsalvartreino.clicked.connect(self.Treino_salvar)

        # Botões de mudança de tela
        self.btn_Home.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgHome)
        )
        self.btn_Config.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgConfiguracao)
        )
        self.btn_Lembrete.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgLembretes)
        )
        self.btn_relatorio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgRelatorio)
        )
        self.btn_Dieta.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgAlimentar)
        )
        self.btn_chat.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgChat)
        )
        self.btn_Perfil.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgConta)
        )
        self.btn_treino.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgTreino)
        )
        self.btn_SeuTreino.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgSeuTreino)
        )
        self.btn_academia.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgAcademia)
        )
        self.btn_Alonga.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgAlonga)
        )
        self.btn_casa.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgCasa)
        )
        self.btn_Anae.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgAerobicos)
        )
        self.btn_VoltarAcademia.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgTreino)
        )
        self.btn_VoltarCasa.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgTreino)
        )
        self.btn_voltarAero.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgTreino)
        )
        self.btn_VoltarAlonga.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgTreino)
        )
        self.btvoltartreino.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.PgTreino)
        )
        self.btn_Sair.clicked.connect(lambda: exit())

    # Função do Menu Expansivo
    def MLeft(self):

        width = self.Left.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.Left, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # Função do Menu Expansivo da Janela de Treino

    def MMenutreinar(self):

        Altura = self.Menutreinar.height()

        if Altura == 0:
            novaaltura = 200
        else:
            novaaltura = 0

        self.animation = QtCore.QPropertyAnimation(self.Menutreinar, b"maximumHeight")
        self.animation.setDuration(600)
        self.animation.setStartValue(Altura)
        self.animation.setEndValue(novaaltura)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        if not self.comboBox:
            self.comboBox.addItems(['',
                                    'Flexão de braço',
                                    'Rosca martelo',
                                    'Rosca direta',
                                    'Prancha de antebraço',
                                    'Leg Press 45°',
                                    'Afundo',
                                    'Agachamento',
                                    'Extensora',
                                    'Supino reto com barra',
                                    'Crossover com pega alta',
                                    'Crucifixo reto',
                                    'Abdominal Reto',
                                    'Abdominal Bicicleta',
                                    'Barra Fixa',
                                    'Remada Curvada',
                                    'Remada Unilateral',
                                    'Puxada com Barra Pulley'])

            self.comboBox_2.addItems([' ',
                                      '2',
                                      '3',
                                      '4',
                                      '5',
                                      '6',
                                      '7',
                                      '8',
                                      '9'])

            self.comboBox_3.addItems([' ',
                                      '5',
                                      '10',
                                      '15',
                                      '20',
                                      '25'])

    def Treino_salvar(self):

        if self.comboBox.currentText() == " ":
            pass
        else:
            informacoes4 = self.comboBox.currentText()

        if self.comboBox_2.currentText() == " ":
            pass
        else:
            informacoes5 = self.comboBox_2.currentText()

        if self.comboBox_3.currentText() == " ":
            pass
        else:
            informacoes6 = self.comboBox_3.currentText()

        list_treino = f'{informacoes4}  \n{informacoes5} x {informacoes6}'

        a = self.Exercicios_list1.text()
        b = self.Exercicios_list2.text()
        c = self.Exercicios_list3.text()
        d = self.Exercicios_list4.text()
        e = self.Exercicios_list5.text()
        f = self.Exercicios_list6.text()
        g = self.Exercicios_list7.text()
        h = self.Exercicios_list8.text()
        i = self.Exercicios_list9.text()


        if not a:
            self.Exercicios_list1.setText(list_treino)

        elif not b:
            self.Exercicios_list2.setText(list_treino)
        elif not c:
            self.Exercicios_list3.setText(list_treino)
        elif not d:
            self.Exercicios_list4.setText(list_treino)
        elif not e:
            self.Exercicios_list5.setText(list_treino)
        elif not f:
            self.Exercicios_list6.setText(list_treino)
        elif not g:
            self.Exercicios_list7.setText(list_treino)
        elif not h:
            self.Exercicios_list8.setText(list_treino)
        elif not i:
            self.Exercicios_list9.setText(list_treino)
        elif a:
            self.Exercicios_list1.setText("")
            self.Exercicios_list2.setText("")
            self.Exercicios_list3.setText("")
            self.Exercicios_list4.setText("")
            self.Exercicios_list5.setText("")
            self.Exercicios_list6.setText("")
            self.Exercicios_list7.setText("")
            self.Exercicios_list8.setText("")
            self.Exercicios_list9.setText("")



    def Mcomida(self):

        Altura = self.Menucomida.height()

        if Altura == 0:
            novaaltura = 200
        else:
            novaaltura = 0

        self.animation = QtCore.QPropertyAnimation(self.Menucomida, b"maximumHeight")
        self.animation.setDuration(600)
        self.animation.setStartValue(Altura)
        self.animation.setEndValue(novaaltura)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        if not self.comboBox_4:
            self.comboBox_4.addItems(['',
                                      'Café da Manhã',
                                      'Lanche da Manhã',
                                      'Almoço',
                                      'Lanche da Tarde',
                                      'Jantar',
                                      'Ceia'])

            self.comboBox_5.addItems(['',
                                      '7:00',
                                      '8:00',
                                      '9:00',
                                      '10:00',
                                      '12:00',
                                      '12:30',
                                      '13:00',
                                      '14:00',
                                      '15:00',
                                      '16:00',
                                      '17:00',
                                      '18:00',
                                      '19:00',
                                      '20:00',
                                      '21:00',
                                      '22:00'])

    def Mmeils(self):

        width = self.Menu_Email.width()

        if width == 0:
            newWidth = 230
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.Menu_Email, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # Função das Caixas de Seleção
    def Treino_explicacao(self):
        # Ao clicar em uma opção da caixa uma explicação do exercicio aparecera
        if self.comboBox.currentText() == '':
            self.ImagemTreino.setStyleSheet("background-color: rgb(255, 255, 255);")



    def Dieta_recomendado(self):
        if self.comboBox_4.currentText() == " ":
            pass
        else:
            informacoes = self.comboBox_4.currentText()

        if self.comboBox_5.currentText() == " ":
            pass
        else:
            informacoes2 = self.comboBox_5.currentText()

        if self.Alimentocomentario == '':
            pass
        else:
            informacoes3 = self.Alimentocomentario.text()

        list_dieta = f'{informacoes}  \n{informacoes2} \n{informacoes3}'

        if informacoes == "Café da Manhã":
            self.Alimento1.setText(list_dieta)
        elif informacoes == "Lanche da Manhã":
            self.Alimento2.setText(list_dieta)
        elif informacoes == "Almoço":
            self.Alimento3.setText(list_dieta)
        elif informacoes == "Lanche da Tarde":
            self.Alimento4.setText(list_dieta)
        elif informacoes == "Jantar":
            self.Alimento5.setText(list_dieta)
        elif informacoes == "Ceia":
            self.Alimento6.setText(list_dieta)


def main():
    app = QApplication(sys.argv)
    form = LoginCadastro()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
