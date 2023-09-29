# Юлия Панфилова, 8а когорта - финальный проект. Инженер по тестированию плюс.
import data
import sender_stand_request

def test_order_create():
    response_new_order = sender_stand_request.post_new_order(data.order_body)

    track_number = response_new_order.json().get("track")

    response_number = sender_stand_request.get_order(track_number)

    assert response_number.status_code == 200
    
