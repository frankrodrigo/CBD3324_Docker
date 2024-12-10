CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    cellphone VARCHAR(15) NOT NULL
);

-- Insert test values
INSERT INTO users (username, cellphone) VALUES ('John Doe', '1234567890');
INSERT INTO users (username, cellphone) VALUES ('Jane Smith', '9876543210');
