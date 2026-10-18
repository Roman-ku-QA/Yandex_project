import sender_stand_request
import data


def test_create_order_and_get_track():  # создание заказа
    create_response = sender_stand_request.post_new_orders(data.orders_body)
    assert create_response.status_code == 201
    track = create_response.json()["track"]
    # Получение заказа по треку и проверка, что код равен 200
    get_response = sender_stand_request.get_orders_track(track)
    assert get_response.status_code == 200
