from rest_framework.test import RequestsClient, APIClient


def test_get_list_by_ip():
    client = RequestsClient()
    response = client.get("http://testserver/api/shorter/")
    assert response.status_code == 200


def test_post_data():
    client = APIClient()
    data = {'url': 'https://test-link.com/', 'expireAt': '2'}
    response = client.post("http://testserver/api/shorter/", data=data)
    assert response.status_code == 201


def test_fail_post_data():
    client = APIClient()
    data = {'url': 's://test-link.com/', 'expireAt': 'incorrect data'}
    response = client.post("http://testserver/api/shorter/", data=data)
    assert response.status_code == 400

