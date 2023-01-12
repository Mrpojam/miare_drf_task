from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.
class CourierListTest(APITestCase):
    def test_get_all_courier(self):
        response = self.client.get('/api/courier/')
        self.assertEqual(200, response.status_code)
    
    def test_post_new_courier(self):
        testcase = {'id':100, 'first_name':'test_name','last_name':'test_name'}
        response = self.client.post('/api/courier/', testcase)
        self.assertEqual(201, response.status_code)

    def test_post_badrequest_courier(self):
        testcase = {'id':1, 'first_name':'test_name','sir_name':'test_name'}
        response = self.client.post('/api/courier/', testcase)
        self.assertEqual(400, response.status_code)

class IncomeApiTest(APITestCase):
    def test_get_income(self):
        response = self.client.get('/api/income/')
        self.assertEqual(200, response.status_code)
    
    def test_post_badrequest_income(self):
        testcase = {"Date": "2020-02-13", "type": "In","value": 120,"courier": 12}
        response = self.client.post('/api/income/', testcase)
        print(response.data)
        self.assertEqual(400, response.status_code)
