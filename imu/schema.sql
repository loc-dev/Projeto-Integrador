DROP TABLE IF EXISTS refugiado;

CREATE TABLE refugiado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    sobrenome TEXT NULL,
    naturalidade TEXT NOT NULL,
    email TEXT NULL
);
