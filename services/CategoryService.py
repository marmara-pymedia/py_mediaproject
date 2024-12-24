import json
from entities.Category import Category

class CategoryService:
    def __init__(self):
        pass

    def add_user(self,category:Category):
        categories=self.get_all()
        category.id=categories[-1].id+1 if len(categories)!=0 else 1
        categories.append(category)
        with open("data/categories.json","w") as file:
            file.write(json.dumps([category.__dict__ for category in categories]))

    def get_user_by_id(self,id:int):
        categories=self.get_all()
        for category in categories:
            if category.id==id:
                return category
        return None
    
    def get_all(self):
        with open("data/categories.json","r") as file:
            categories=json.load(file)
        return [Category(**category) for category in categories]
    
    def update_user(self,category:Category):
        categories=self.get_all()
        for i in categories:
            if(i.id==category.id):
                i.name=category.name
        
        with open("data/categories.json","w") as file:
            file.write(json.dumps([category.__dict__ for category in categories]))
    
    def delete_user(self,category:Category):
        categories=self.get_all()
        for i in categories:
            if(i.id==category.id):
                categories.remove(i)
                break
            
        with open("data/categories.json","w") as file:
            file.write(json.dumps([category.__dict__ for category in categories]))