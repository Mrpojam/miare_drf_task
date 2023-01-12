from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.
class CourierListTest(APITestCase):
    def test_get_all_courier(self):
        response = self.client.get('/api/courier/')
        self.assertEqual(200, response.status_code)
    
    def test_post_new_courier(self):
        response = self.client.post('/api/courier/', {'id':100, 'first_name':'test_name','last_name':'test_name'})
        self.assertEqual(201, response.status_code)

    def test_post_badrequest_courier(self):
        response = self.client.post('/api/courier/', {'id':1, 'first_name':'test_name','sir_name':'test_name'})
        self.assertEqual(400, response.status_code)
        