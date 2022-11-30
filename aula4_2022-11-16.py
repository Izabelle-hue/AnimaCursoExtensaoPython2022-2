#1 importação da biblioteca sqlite3
import sqlite3

#2 conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3 criando  objeto do tipo cursor
cursor = conexao.cursor()

#4 Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5 Execução de comando SQL no SQLlite (no cursor)
cursor.execute(sql)

#6 consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")

