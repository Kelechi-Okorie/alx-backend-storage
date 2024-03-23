-- creates a trigger that decreases the quantity of an item after adding a new order
-- Quantity in the table items can be negative
CREATE TRIGGER decreas_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		UPDATE ITEMS
		SET quantity = quantity = NEW.quantity_ordered
		WHERE item_id = NEW.item_id
	END
