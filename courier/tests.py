from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Courier, Income

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
        self.assertEqual(400, response.status_code)

    def test_post_create_income(self):
        testcase0 = {'id':100, 'first_name':'test_name','last_name':'test_name'}
        response0 = self.client.post('/api/courier/', testcase0)
        if (response0.status_code != 201):
            print (f"Response : {response0.data}")
            self.assertEqual(201, response0.status_code)
        
        testcase = {"Date": "2023-02-13", "type":"In", "value":100, "courier":100}
        response1 = self.client.post('/api/income/', testcase)
        if (response1.status_code != 201):
            print (f"Response : {response1.data}")
            self.assertEqual(201, response1.status_code)
        
        income = Income.objects.get(courier=100, Date="2023-02-13")
        self.assertEqual(100, income.value)

    def test_post_update_income(self):
        testcase0 = {'id':100, 'first_name':'test_name','last_name':'test_name'}
        response0 = self.client.post('/api/courier/', testcase0)
        if (response0.status_code != 201):
            print (f"Response : {response0.data}")
            self.assertEqual(201, response0.status_code)
        
        testcase = {"Date": "2023-02-13", "type":"In", "value":100, "courier":100}
        response1 = self.client.post('/api/income/', testcase)
        if (response1.status_code != 201):
            print (f"Response : {response1.data}")
            self.assertEqual(201, response1.status_code)
        
        testcase = {"Date": "2023-02-13", "type":"I", "value":100, "courier":100}
        response2 = self.client.post('/api/income/', testcase)
        if (response2.status_code != 201):
            print (f"Response : {response2.data}")
            self.assertEqual(201, response2.status_code)

        testcase = {"Date": "2023-02-13", "type":"D", "value":50, "courier":100}
        response3 = self.client.post('/api/income/', testcase)
        if (response3.status_code != 201):
            print (f"Response : {response3.data}")
            self.assertEqual(201, response3.status_code)

        income = Income.objects.get(courier=100, Date="2023-02-13")
        self.assertEqual((100 + 100 - 50), income.value)