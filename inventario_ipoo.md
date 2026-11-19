```mysql
CREATE DATABASE inventario_ipoo;
USE inventario_ipoo;

CREATE TABLE productos (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) NOT NULL,
descripcion VARCHAR(255),
precio DECIMAL(10,2) NOT NULL,
stock INT NOT NULL,
categoria VARCHAR(50) NOT NULL
);


INSERT INTO productos
    (nombre, descripcion, precio, stock, categoria)
VALUES(
'Cámara ZWO ASI585MC', 'Cámara astronómica para fotografía planetaria', 485000.00, 8, 'Cámaras'),
('Filtro Optolong L-eXtreme', 'Filtro de doble banda para nebulosas', 325000.00, 12, 'Filtros'),
('Montura Sky-Watcher EQ6-R Pro', 'Montura ecuatorial motorizada con seguimiento', 2450000.00, 3, 'Monturas'),
('Telescopio William Optics RedCat 51', 'Refractor apocromático para cielo profundo', 1890000.00, 5, 'Telescopios'),
('Enfocador ZWO EAF', 'Motor de enfoque automático para telescopios', 295000.00, 15, 'Accesorios'),
('Mini PC ZWO ASIAIR Plus', 'Controlador para automatizar sesiones astronómicas', 410000.00, 7, 'Controladores'),
('Máscara Bahtinov 150 mm', 'Máscara para conseguir enfoque preciso en estrellas', 28500.00, 24, 'Herramientas'),
('Batería Celestron PowerTank Lithium', 'Fuente portátil para equipos astronómicos', 375000.00, 9, 'Alimentación');

```

