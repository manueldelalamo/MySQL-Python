
import pymysql
miConexion = pymysql.connect( host='localhost', user= 'root', passwd='admin', db='sys' )
cur = miConexion.cursor()
cur.execute( "SELECT * FROM clientes" )
for nombre in cur.fetchall() :
    print (nombre)
miConexion.close()