# como conectar com o pgADMIN banco = python_crud_streamlit
import psycopg2 as db


conn = db.connect(user="postgres", password="An0025322", host="127.0.0.1", port="5432", database="python_crud_streamlit")

curs = conn.cursor()

sqlSelect = "select * from cliente"
curs.execute(sqlSelect)
registros = curs.fetchall()
print(registros)
curs.close()
conn.close()