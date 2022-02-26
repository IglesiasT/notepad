CREATE DATABASE IF NOT EXISTS notepad;
use notepad;

CREATE TABLE IF NOT EXISTS users(
    id int(25) auto_increment not null,
    first_name varchar(100),
    last_name varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    created_date date not null,
    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notes(
    id int(25) auto_increment not null,
    user_id int(25) not null,
    title varchar(100) not null,
    content MEDIUMTEXT,
    created_date date not null,
    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT fk_user_note FOREIGN KEY (user_id) REFERENCES users (id)
)ENGINE=InnoDb;
