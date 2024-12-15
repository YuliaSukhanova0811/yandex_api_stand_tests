import configuration
import requests
import data 

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()

print(response.status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})

response = get_logs()

# Выводим в консоль HTTP-статус код ответа сервера. Коды состояния HTTP сообщают
# о результате выполнения запроса. Например, код 200 означает "OK", а 404 - "Не найдено".
print(response.status_code)
print(response.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,params={"count":20})

response = get_users_table()

print(response.status_code)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)
print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,  # Тело запроса содержит ID продуктов в формате JSON
                         headers=data.headers)  # Использование заголовков из файла data.py

# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.products_ids)

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
# Это позволяет проверить успешность выполнения запроса и посмотреть результаты поиска наборов
print(response.status_code)
print(response.json()) 
