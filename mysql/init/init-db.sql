CREATE TABLE users (
    id int AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE users_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    birthdate DATE,
    phone BIGINT,
    FOREIGN KEY (user_id)  REFERENCES users (id)
);

INSERT INTO users (username, password) VALUES ('admin', 'admin');

INSERT INTO users_info (user_id, name, surname, birthdate, phone) VALUES (1, 'Админ', 'Админович', '2022.11.27', 88005553535);