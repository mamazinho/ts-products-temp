from models.product_model import ProductModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from config.database import Database

from daos.category_dao import CategoryDao
from models.category_model import CategoryModel


class Controller():
    
    def create(self):
        new_category = {
            "name": f"{input('Name category: ')}",
            "description": int(input('Description: '))
        }
        CategoryDao(new_category).create()

    def read_all(self):
        list_categories = CategoryDao().read_all()
        for item in list_categories:
            print(item)
    
    def delete(self):
        category = {
            "id": int(input('Código para deletar: '))
        }
        CategoryDao(category).delete()
        self.read_all()

    def update(self):
        category_update = {
        "id": int(input("Código da categoria: ")),
        "name": f"{input('name: ')}",
        "description": f"{input('description: ')}"
        }
        CategoryDao(category_update).update()
        self.read_all()

# Controller().create()
Controller().read_all()
# Controller().delete()
Controller().update()