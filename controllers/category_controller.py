from daos.category_dao import CategoryDao


class CategoryController():
    
    def create_category(self, name, description):
        new_category = {
            "name": name,
            "description": description
        }
        category_id = CategoryDao(new_category).create()
        return category_id

    def read_all_categories(self):
        list_categories = CategoryDao().read_all()
        return list_categories
    
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