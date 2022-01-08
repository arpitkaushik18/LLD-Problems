from services.user_service import UserService
from services.product_service import ProductService
from models.Category import Category
from models.ProductsCatalog import ProductsCatalog
from services.productCatalog_service import ProductCatalogService
from models.Product import Product

user1 = UserService()
piyush = user1.addCustomer("Piyush",99443)

dailyneed = user1.addSeller("Daily Needs Groceries",987654)

cat1 = Category('groceries')

prodcata = ProductsCatalog()

prodserv = ProductCatalogService()
prodserv.addCatagory(prodcata,cat1)

prodserv1 = ProductService()
prodserv1.registerProduct(prodcata,Product('Sugar','Fine quality',40.00,'grocery',1000))







prod1 = ProductService()

