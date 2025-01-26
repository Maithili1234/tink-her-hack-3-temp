CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    color TEXT,
    size TEXT,
    image_path TEXT,
    availability INTEGER  -- 0: Not available, 1: Available
);

CREATE TABLE store_locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    product_id INTEGER,  -- Foreign key to Products
    FOREIGN KEY (product_id) REFERENCES products(id)
);
