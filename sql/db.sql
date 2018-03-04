-- CREATE TABLE prueba_base(
--   idprueba    SERIAL PRIMARY KEY,
--   dato1       TEXT,
--   dato2       TEXT,
--   dato3       TEXT
-- );

CREATE TABLE directorio(
  iddirectorio   SERIAL PRIMARY KEY,
  nombre         TEXT,
  paterno        TEXT,
  materno        TEXT,
  fisica         BOOLEAN,
  rfc            TEXT,
  curp           TEXT,
  sexo           TEXT,
  numId          TEXT,
  direccion      TEXT
);

CREATE TABLE usuarios(
  idusuario    SERIAL PRIMARY KEY,
  iddirectorio INTEGER REFERENCES directorio,
  nickname     TEXT,
  pass         TEXT,
  activo       BOOLEAN
);

CREATE TABLE productos(
  idproducto  SERIAL PRIMARY KEY,
  nombre      TEXT,
  precio      NUMERIC,
  activo      BOOLEAN
  );
-- INSERT INTO prueba_base VALUES (DEFAULT, 'hola', 'mundo', 'prueba');
INSERT INTO directorio VALUES(DEFAULT, 'Isidro', 'Rivera', 'Monjaras', TRUE, '', '', 'M', '', '');
INSERT INTO usuarios VALUES (DEFAULT, lastval(), 'isidro', '1b01e2c0c85001ef5684bbf3a457f99e', TRUE);


-- -------------------------------------------------------------
-- Isidro Rivera Monjaras
-- Función encargada de validar usuario
-- 03/03/2018
-- --------------------------------------------------------------
CREATE OR REPLACE FUNCTION valida_user(p_usuario  TEXT, p_pass  TEXT)
  RETURNS BOOLEAN AS $$
DECLARE 
  _ok  BOOLEAN:= FALSE;
BEGIN
  PERFORM idusuario 
     FROM usuarios 
    WHERE (nickname, pass) = (p_usuario, md5(p_pass));
  RETURN FOUND;
END;$$
LANGUAGE plpgsql;
