import pymysql

try:
    conexao = pymysql.connect(host="127.0.0.1", user=" ", passwd=" ")

    cursor = conexao.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro;")
    cursor.execute("USE cadastro;")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS conta(
                    id int(6) NOT NULL PRIMARY KEY auto_increment,
                    Nome varchar(15) not null,
                    Sobrenome varchar(30) not null,
                    Username varchar (15) not null,
                    Email varchar(40) not null,
                    Senha varchar(15) not null
                    );"""
    )
    cursor.execute(
        """INSERT INTO conta(id,Nome,Sobrenome,Username,Email,Senha) Values('1','Admin','Admin','Admin','Admin','Admin');"""
    )
    server = True
except:
    try:
        conexao = pymysql.connect(host="localhost", user="root", passwd="")

        cursor = conexao.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro;")
        cursor.execute("USE cadastro;")
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS conta(
                        id int(6) NOT NULL PRIMARY KEY auto_increment,
                        Nome varchar(15) not null,
                        Sobrenome varchar(30) not null,
                        Username varchar (15) not null,
                        Email varchar(40) not null,
                        Senha varchar(15) not null
                        );"""
        )

        server = True
    except:
        print("Servidor não conectado")
        server = False
