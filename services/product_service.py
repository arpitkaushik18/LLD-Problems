from services.productCatalog_service import ProductCatalogService


class ProductService(ProductCatalogService):

    def registerProduct(self,product,pcatalog,seller):
        product.set_seller(seller)
        seller.ProductList.append(product)
        super().addProduct(pcatalog,product)


