#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

import os
from psycopg2 import *
from yaml     import load, dump

class dbase(object):
  """Clase encargada de realizar la conexión entre sistema & base de datos"""
  def __init__(self, base):
    # self.DNS  = dns # Se relizara la conexion mediante dns con formato "dbname=test user=postgres password=secret host=localhost port=5432"
    self.DNS = self.getDataBase(base)

  def rawQuery(self, query):
    try:
      with connect(self.DNS) as conn:
        with conn.cursor() as curs:
          curs.execute(query)
          _res = curs.fetchall()
    except DatabaseError as e:
      _res = (e.diag.severity, e.diag.message_primary, e.diag.message_hint)
      if (e.diag.severity is None and e.diag.message_primary is None):
        _res = ('Error', 'Error de conexión')
    return _res

  def rawQueryOne(self, query):
    try:
      with connect(self.DNS) as conn:
        with conn.cursor() as curs:
          curs.execute(query)
          _res = curs.fetchone()
    except DatabaseError as e:
      _res = (e.diag.severity, e.diag.message_primary, e.diag.message_hint)
      if (e.diag.severity is None and e.diag.message_primary is None):
        _res = ('Error', 'Error de conexión')
    return _res
  
  def rawQueryMany(self, query, num):
    try:
      with connect(self.DNS) as conn:
        with conn.cursor() as curs:
          curs.execute(query)
          _res = curs.fetchmany(num)
    except DatabaseError as e:
      _res = (e.diag.severity, e.diag.message_primary, e.diag.message_hint)
      if (e.diag.severity is None and e.diag.message_primary is None):
        _res = ('Error', 'Error de conexión')
    return _res

  def getDataBase(self, base):
    try:
      if (os.path.isfile('./.base.yaml')):
        with open(r'.base.yaml') as file:
          data = load(file)
      else:
        data = {"baseProduccion" : { "url"    : 'localhost',
                                     "nombre" : 'Base Produccion',
                                     "usuario": 'isidro',
                                     "pass"   : '1q2w3e4r5T'}
               }
        with open('./.base.yaml', 'w') as file:
          file.write(dump(data))
      datosDb = data[base]
    except Exception as e:
      print(e) 
    return "dbname={0} user={1} password={2} host={3}".format(base, datosDb["usuario"], datosDb["pass"], datosDb["url"])


"""
Usar en DNS
dbname   – the database name (database is a deprecated alias)
user     – user name used to authenticate
password – password used to authenticate
host     – database host address (defaults to UNIX socket if not provided)
port     – connection port number (defaults to 5432 if not provided)
"""
