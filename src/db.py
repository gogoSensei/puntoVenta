#!/usr/bin/python3

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

from psycopg2 import *

class dbase(object):
  """Clase encargada de realizar la conexión entre sistema & base de datos"""
  def __init__(self, dns):
    self.DNS = dns # Se relizara la conexion mediante dns con formato "dbname=test user=postgres password=secret host=localhost port=5432"

  def rawQuery(self, query):
    _res = {"ok"     : False,
            "result" : None,
    }
    try:
      with connect(self.DNS) as conn:
        with conn.cursor() as curs:
          curs.execute(query)
          _res["result"] = curs.fetchall()
      _res["ok"]=True
    except DatabaseError as e:
      _res["result"] = (e.diag.severity, e.diag.message_primary, e.diag.message_hint)
      if (e.diag.severity is None and e.diag.message_primary is None):
          _res = ('Error', 'Error de conexión')
    return _res



"""
Usar en DNS
dbname   – the database name (database is a deprecated alias)
user     – user name used to authenticate
password – password used to authenticate
host     – database host address (defaults to UNIX socket if not provided)
port     – connection port number (defaults to 5432 if not provided)
"""
