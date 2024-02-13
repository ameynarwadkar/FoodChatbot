CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    food_item_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    order_status_id INT NOT NULL,
    FOREIGN KEY (food_item_id) REFERENCES food_items(item_id),
    FOREIGN KEY (order_status_id) REFERENCES order_tracking(order_id)
);