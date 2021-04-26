class Product:
    
    try:
        categories = []
        for id_category in categories_list:
            categories.append(filter_category(id_category))
        product_object = Product(name=name, value=value, description=description)
        product_object.categories.extend(categories)
        session = Session()
        session.add(product_object)
        session.commit()
    except:
        session.rollback()
        raise Exception("Erro, ao registrar produto.")
    finally:
        session.close()