-- Create users table
CREATE TABLE IF NOT EXISTS users1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    dob TEXT NOT NULL,
    hometown TEXT NOT NULL
);


-- Insert initial data
INSERT INTO users (name, email, phone, dob, hometown) 
VALUES 
('John Doe', 'john.doe@example.com', '1234567890', '1990-01-01', 'New York'),
('Jane Smith', 'jane.smith@example.com', '0987654321', '1985-05-05', 'Los Angeles');
	
