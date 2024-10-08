import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod 
from entity.userDetail import UserDetail
from entity.product import Product

class IOrderManagementRepository(ABC):

    @abstractmethod
    def createOrder(self, userDetail : UserDetail , products : list ):
        pass

    @abstractmethod
    def cancelOrder(self, user_id : int , order_id : int  ):
        pass

    @abstractmethod
    def createProduct(self, userDetail : UserDetail , product : Product ):
        pass

    @abstractmethod
    def createUser(self, userDetail : UserDetail ):
        pass     

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, userDetail : UserDetail ):
        pass      