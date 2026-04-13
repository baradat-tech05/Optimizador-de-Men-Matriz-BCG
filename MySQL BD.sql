create table Ingredientes (
	ID Int auto_increment primary key,
	nombre varchar(100) not null,
	unidad_de_medida enum ('kg' , 'gr', 'lt', 'ml', 'unidades') not null,
	Precio_costo_unitario decimal (10, 2) not null comment'Costo por unidad de medida'
) ;
 
select * from Ingredientes;

create table Platos (
	ID int auto_increment primary key,
    nombre varchar(100)not null,
    precio_venta decimal (10, 2) not null,
    categoria enum ('Entrante', 'Principal', 'Postre', 'Bebida') default 'principal'
) ;
    
select * from Platos;
    
create table Recetas (
	ID int auto_increment primary key,
    Platos_ID int not null,
    Ingredientes_id int not null,
    cantidad_necesaria decimal (10, 3) not null comment 'Cantidad usada en el plato',
    
    constraint fk_Platos foreign key (Platos_ID)
		references Platos(ID) on delete cascade,
        
	constraint fk_Ingredientes foreign key (Ingredientes_ID)
		references Ingredientes(Id) on delete restrict
	);
    
select * from Recetas;
    
create table ventas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    plato_id INT NOT NULL,
    cantidad_vendida INT NOT NULL,
    fecha_venta DATE DEFAULT (CURRENT_DATE),
    
    CONSTRAINT fk_plato_venta FOREIGN KEY (plato_id) 
        REFERENCES platos(id) ON DELETE CASCADE
);

select * from ventas;

SELECT 
    p.nombre AS plato,
    SUM(r.cantidad_necesaria * i.precio_costo_unitario) AS costo_total,
    p.precio_venta,
    (p.precio_venta - SUM(r.cantidad_necesaria * i.precio_costo_unitario)) AS margen_ganancia
FROM platos p
JOIN recetas r ON p.ID = r.Platos_ID
JOIN Ingredientes i ON r.Ingredientes_ID = i.ID
GROUP BY p.ID, p.nombre, p.precio_venta;

alter table ventas change id ID int auto_increment;

alter table rcetas change Ingredientes_id Ingredientes_ID int not null;

SELECT 
    p.nombre AS plato,
    -- 1. Eje X: Popularidad (Suma de cantidades vendidas)
    SUM(v.cantidad_vendida) AS total_ventas,
    -- 2. Cálculo del Costo Total (Escandallo)
    SUM(r.cantidad_necesaria * i.Precio_costo_unitario) AS costo_elaboracion,
    -- 3. Eje Y: Rentabilidad (Precio Venta - Costo)
    (p.precio_venta - SUM(r.cantidad_necesaria * i.Precio_costo_unitario)) AS margen_unitario
FROM platos p
JOIN recetas r ON p.ID = r.Platos_ID
JOIN ingredientes i ON r.Ingredientes_ID = i.ID
LEFT JOIN ventas v ON p.ID = v.plato_ID
GROUP BY p.ID, p.nombre, p.precio_venta;