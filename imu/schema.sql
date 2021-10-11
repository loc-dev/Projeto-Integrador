DROP TABLE IF EXISTS refugiado;

CREATE TABLE refugiado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    naturalidade TEXT NOT NULL,
    senha TEXT NOT NULL
);
