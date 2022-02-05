import requests
import unittest
import json

url = "http://localhost:8080/v2/pet"
petId = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
status = {
    "status":('available', 'pending', 'sold')
}


class EndPointsTests(unittest.TestCase):

    def test_post_petid(self):
        resp = requests.post(url, json=petId)
        print(resp.json())
        assert resp.json()['name'] == 'doggie', 'not a doggie pet, is it a cat? '
        assert resp.json()['id'] >> 0, "new id wasn't created for your pet"
        assert resp.json()['status'] == 'available', 'not available new pet'

    def test_put_petid(self):
        resp = requests.put(url, json=petId)
        print(resp.json())
        assert resp.json()['name'] == petId['name'], 'wrong pet update'
        assert resp.json()['status'] == 'available', 'not available pet'

    def test_get_findbystatus(self):
        url2 = url + "/findByStatus"
        data1 = {
            'status': 'available'
                }
        resp = requests.get(url2, json=data1)
        print(resp.json())
        assert resp.status_code == 200, 'no results'

    def test_post_by_petId(self):
        data = {
            'id': 50,
            'name': 'elefant',
            'status': 'available!!!'
                }
        resp = requests.post(url, json=data)
        print(resp.json())
        assert resp.json()['id'] == 50, 'not available pet'
        assert resp.json()['name'] == 'elefant', 'wrong name'

    def test_get_byId(self):
        url3 = url + '/50'
        resp = requests.get(url3)
        print(resp.json())
        assert resp.json()['status'] == 'available!!!', 'not available pet'

    def test_delete_by_petId(self):
        url3 = url + '/50'
        resp = requests.delete(url3)
        print(resp.json())
        assert resp.status_code == 200, "pet doesn't exist"


if __name__ == '__main__':
    unittest.main()
