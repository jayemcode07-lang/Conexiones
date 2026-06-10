-- Base de datos: DB_prueba
CREATE DATABASE DB_prueba;

CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE
);

