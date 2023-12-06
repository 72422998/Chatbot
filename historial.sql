CREATE TABLE historial (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    mensaje_usuario varchar(1000),
    mensaje_bot varchar(1000),
    fecha datetime,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);