import configuration
import requests
import data


def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_NEW,
                         json=body,
                         headers=data.headers)


response = post_new_orders(data.orders_body)
print(response.status_code)
print(response.json())


def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK,
                        params={"t": track},
                        headers=data.headers)
