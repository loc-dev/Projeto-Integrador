DROP TABLE IF EXISTS refugiado;
DROP TABLE IF EXISTS voluntario;

CREATE TABLE refugiado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    naturalidade TEXT NOT NULL,
    senha TEXT NOT NULL
);


CREATE TABLE voluntario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    naturalidade TEXT NOT NULL,
    senha TEXT NOT NULL
);