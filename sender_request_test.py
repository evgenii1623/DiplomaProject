# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Создание заказа
def post_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)

# Получение заказа по номеру трекера
def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK_PATH + str(track),
	                    headers = data.headers)

# Выполнить запрос на получения заказа по треку заказа.
def get_track():
	response = post_new_order(data.order_body)
	track = response.json()["track"]
	return get_order_from_track(track).status_code

# Проверить, что код ответа равен 200.
def test_get_order_from_track_code_200():
	assert get_track() == data.status_code_200

# Евгений Аваргин 21 когорта, инженер тестировщик плюс




