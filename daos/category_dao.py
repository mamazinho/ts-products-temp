from config.database import Database
from models.category_model import CategoryModel


class CategoryDao:

    def __init__(self, category: dict= {}):
        self.category = category
    
    def create(self):
        with Database() as session:
            category = CategoryModel(
                name = self.category["name"],
                description = self.category["description"]
            )
            session.add(category)
            session.flush()
            session.commit()
            return category.id

    def read_all(self):
        with Database() as session:
            result = session.query(CategoryModel).all()
            return result

    def update(self):
        if not 'id' in self.category or not self.category['id']:
            return self.create()
        with Database() as session:
            category_update = session.query(CategoryModel).filter_by(id=self.category['id']).first()
            category_update.update({
                "id": self.category['id'],
                "name": self.category.get('name', category_update.name),
                "description": self.category.get('description', category_update.description),
            })
            session.commit()
    
    def delete(self):
        with Database() as session:
            result = session.query(CategoryModel).filter_by(id=self.category['id']).delete()
            session.commit()
