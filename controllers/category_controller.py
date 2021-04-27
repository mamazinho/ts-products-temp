from models.product_model import ProductModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from config.database import Database

from daos.category_dao import CategoryDao
from models.category_model import CategoryModel


class CategoryController():
    
    def create_category(self, name, description):
        new_category = {
            "name": name,
            "description": description
        }
        CategoryDao(new_category).create()

    def read_all_categories(self):
        list_categories = CategoryDao().read_all()
        for item in list_categories:
            print(item)
    
    def delete_category(self, category_id):
        category = {
            "id": category_id
        }
        CategoryDao(category).delete()

    def update_category(self, category_id, name=None, description=None):
        category_update = {
        "id": category_id,
        "name": name,
        "description": description
        }
        CategoryDao(category_update).update()