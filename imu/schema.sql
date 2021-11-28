DROP TABLE IF EXISTS refugiado;
DROP TABLE IF EXISTS voluntario;

CREATE TABLE refugiado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NULL,
    nacionalidade TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);


CREATE TABLE voluntario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);