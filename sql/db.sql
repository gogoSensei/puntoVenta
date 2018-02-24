CREATE TABLE prueba_base(
  idprueba    SERIAL PRIMARY KEY,
  dato1       TEXT,
  dato2       TEXT,
  dato3       TEXT
);

INSERT INTO prueba_base VALUES (DEFAULT, 'hola', 'mundo', 'prueba');
