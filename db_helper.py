import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password = 'root',
    database = 'italian_eatery'
)

def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()

        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
                        
        cnx.commit()

        cursor.close()

        print("Order item inserted successfully!")

        return 1
    
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occured: {e}")
              
        cnx.rollback()
                                    
        return -1                


def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    cnx.commit()

    cursor.close()


def get_total_order_price(order_id):
    cursor = cnx.cursor()

    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    result = cursor.fetchone()[0]

    cursor.close()

    return result


def get_next_order_id():
    cursor = cnx.cursor()

    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    result = cursor.fetchone()[0]

    cursor.close()
    
    print(result)

    if result is None:
        return 1
        
    else:
        return result + 1


def get_order_status(order_id):

    cursor = cnx.cursor()

    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()

    if result:
        return result[0]
    else:
        return None 
    
if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Margherita Pizza', 3, 99)
    # insert_order_item('Risotto', 1, 99)
    # insert_order_tracking(99, "in progress")
    print(get_next_order_id())    