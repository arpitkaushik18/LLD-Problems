from services.productCatalog_service_interface import ProductCatalogServiceInterface

class ProductCatalogService(ProductCatalogServiceInterface):

    def updateCategoryProductMap(self,pcatalog,prod):
        pass

    def updateProductQuantity(self, prod, quant):
        prod.set_quantity(quant)

    def updateSimilarProductsMap(self,pcatalog,prod):
        if prod.name is pcatalog.similarProducts.keys():
            pcatalog.similarProducts[prod.name].append(prod)
        else:
            pcatalog.similarProducts[prod.name] = []


    def updateProductSellerMap(self,pcatalog,prod):
        if prod.seller is pcatalog.productSellerMap.keys():
            pcatalog.productSellerMap[prod.seller].append(prod)
        else:
            pcatalog.similarProducts[prod.seller] = []


    def addProduct(self,pcataloge,product):
        pcataloge.products.append(product)
        self.updateCategoryProductMap(pcataloge,product)
        self.updateSimilarProductsMap(pcataloge,product)
        self.updateProductSellerMap(pcataloge,product)


    def addCatagory(self, pcatalog,catagory):
        pcatalog.categories.append(catagory)
        self.updateCategoryProductMap(pcatalog,catagory)

