from .conexion import Conexion
class UsuarioDAO:
    def validarLogin(self,user,pwd):
        cn=Conexion()
        ban='false'
        SQL="select nombre, nombrecompleto, clave from usuarios where nombre=%s and clave=%s and estatus='A'"
        db=cn.getDb()
        cursor=db.cursor()
        login=(user,pwd)
        cursor.execute(SQL,login)
        result=cursor.fetchall()
        for x in result:
            if x[0]==user and x[2]==pwd:
                ban='true'
        return ban
