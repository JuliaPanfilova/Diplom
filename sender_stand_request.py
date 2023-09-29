import requests
import configuration
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=order_body)

response_new_order = post_new_order(data.order_body)

track_number = (response_new_order.json()["track"])

def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(track_number),
                        params={"track":track_number})
response_order_track = get_order(track_number);
