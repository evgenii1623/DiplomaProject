# заголовки для HTTP-запроса создания нового заказа, указывающие на то, что тело запроса будет в формате JSON

headers = {
    "Content-Type": "application/json",
}


# данные заказа для создания новой записи о нем в системе, содержат имя, фамилию, адрес, станцию метро, телефон, срок аренды, дату доставки, комментарий, цвет

order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 204,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-04-24",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

status_code_200 = 200