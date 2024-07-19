CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    UNIQUE(username)
);

-- Additional table definitions go here
