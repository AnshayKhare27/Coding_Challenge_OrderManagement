import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from dao.abstractClasses import IOrderManagementRepository
from util.DB_Util import DBUtil
from entity.userDetail import UserDetail
from entity.product import Product
from exception.UserNotFound import UserNotFound
from exception.OrderNotFound import OrderNotFound


class OrderProcessor(IOrderManagementRepository):

    def __init__(self):
        self.DB_Util = DBUtil()



    def createUser(self, userDetail: UserDetail):
        try:
            conn = self.DB_Util.getDBConn()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO [UserDetail] (user_id, username, password, role) VALUES (?, ?, ?, ?)", userDetail.user_id, userDetail.username, userDetail.password, userDetail.role)
            conn.commit()
            conn.close()
            return True

        except Exception as e:
            print("Error:", e)
            return False   



    def createProduct(self, userDetail: UserDetail, product: Product):
        try:
            conn = self.DB_Util.getDBConn()
            cursor = conn.cursor()

            # Check if the user is admin
            if userDetail.role != "Admin":
                print("Only ADMINS are allowed to create products.")
                return False
            
            cursor.execute("INSERT INTO Product (product_id, product_name, description, price, quantity_in_stock, type) VALUES (?, ?, ?, ?, ?, ?)", product.product_id, product.product_name, product.description, product.price, product.quantity_in_stock, product.type)
            
            conn.commit()
            conn.close()
            return True

        except Exception as e:
            print("Error:", e)
            return False



    def createOrder(self, userDetail : UserDetail , products : list ):
        try:
            conn = self.DB_Util.getDBConn()
            cursor = conn.cursor()

            #CHECKING FOR PRE-EXISTING USER OTHERWISE INSERTING USER
            #cursor.execute("IF NOT EXIST (SELECT * FROM [UserDetail] WHERE user_id = ?), INSERT INTO [UserDetail] (user_id,username,password,role) VALUES (?,?,?,?)",userDetail.user_id,userDetail.user_id,userDetail.username,userDetail.password,userDetail.role)
            cursor.execute("SELECT COUNT(*) FROM [UserDetail] WHERE user_id = ?", userDetail.user_id)
            count = cursor.fetchone()[0]

            if count == 0:
                cursor.execute("INSERT INTO [UserDetail] (user_id,username,password,role) VALUES (?,?,?,?)", userDetail.user_id,userDetail.username,userDetail.password,userDetail.role)

            #CREATING ORDER
            cursor.execute("INSERT INTO [Orders] (user_id) OUTPUT INSERTED.order_id VALUES (?)", userDetail.get_user_id())

            order_id = cursor.fetchone()[0]

            # Insert products for the order
            for product in products:
                cursor.execute("INSERT INTO OrderProduct (order_id, product_id, quantity) VALUES (?, ?, ?)", order_id, product.product_id, product.quantity)

            conn.commit()
            conn.close()
            return True

        except Exception as e:
            print("Error:", e)
            return False    



    def cancelOrder(self, user_id: int, order_id: int):
        try:
            connection = self.DB_Util.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM [UserDetail] WHERE user_id = ?", user_id)
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    raise UserNotFound(f"User with ID {user_id} not found.")

                cursor.execute("SELECT COUNT(*) FROM [Orders] WHERE user_id = ? AND order_id = ?", user_id, order_id)
                order_count = cursor.fetchone()[0]
                if order_count == 0:
                    raise OrderNotFound(f"Order with ID {order_id} not found for user {user_id}.")

                cursor.execute("DELETE FROM OrderProduct WHERE order_id = ?", order_id)
                cursor.execute("DELETE FROM [Orders] WHERE user_id = ? AND order_id = ?", user_id, order_id)
                connection.commit()
                print("Order cancelled successfully.")
            else:
                print("Failed to connect to database.")

        except UserNotFound as e:
            print("Error :", e)

        except OrderNotFound as e:
            print("Error :", e)

        except Exception as e:
            print("Error :", e)
            
        finally:
            if connection:
                connection.close()  



    def getAllProducts(self):
        try:
            conn = self.DB_Util.getDBConn()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Product")
            products = cursor.fetchall()
            conn.close()
            return products
        except Exception as e:
            print("Error:", e)
            return None        



    def getOrderByUser(self, userDetail: UserDetail):
        try:
            conn = self.DB_Util.getDBConn()
            cursor = conn.cursor()

            # Query to retrieve order details including product name and quantity bought
            cursor.execute("SELECT * FROM [Orders] WHERE user_id = ?", (userDetail.user_id))
            orders = cursor.fetchall()  # Fetch all orders for the user
            conn.close()
            return orders  # Return the list of orders

        except Exception as e:
            print("Error:", e)
            return None        