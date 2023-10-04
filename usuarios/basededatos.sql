CREATE DATABASE IF NOT EXISTS chat_bot;
use chat_bot;

CREATE TABLE usuarios(
id          int(25) auto_increment not null,
nombre      varchar(100),
apellidos   varchar(255),
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

