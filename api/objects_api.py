from api import routes
import allure


@allure.step('Получение объектов')
def get_objects(client, *ids):
    return client.get(routes.Routes.OBJECTS, params={'id': ids} if ids else None)

@allure.step('Получение объекта')
def get_object(client, obj_id):
    return client.get(routes.Routes.OBJECTS_ITEM.format(obj_id))

@allure.step('Отправка объектов с параметрами')
def post_object(client, **kwargs):
    return client.post(routes.Routes.OBJECTS, **kwargs)

@allure.step('Изменение объектов')
def put_object(client, obj_id, **kwargs):
    return client.put(routes.Routes.OBJECTS_ITEM.format(obj_id), **kwargs)

@allure.step('Удаление объекта')
def delete_object(client, obj_id):
    return client.delete(routes.Routes.OBJECTS_ITEM.format(obj_id))