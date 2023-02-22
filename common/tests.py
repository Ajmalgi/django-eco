from django.test import TestCase
from django.urls import reverse,resolve
from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.
class TestCommon(TestCase):
    def setup(self):
        self.client=APIClient

    def test_index(self):
        url = reverse('common_app:test_index') #getting url pattern
        res = self.client.get(url)
        

        # self.assertEqual(res.status_code,200)
        self.assertEquals(res.data,'congratulations, you have created')

    


    from django.test import TestCase
from django.urls import reverse,resolve
from rest_framework.test import  APIClient
from rest_framework import  status


# Create your tests here.
class TestCommon(TestCase):

        
    def test_float(self):
        url = reverse('common:test_float')
        res = self.client.get(url)
        data = res.data
        print(type(data))
        if type(data) != float:
            raise AssertionError('error')
        return True
 
    
    # def test_float(self):
    #     url = reverse('common_app:float')
    #     res = self.client.get(url)
    #     data = res.data
    #     if type(data)==float:
    #         d=True
          

    #         self.assertEquals(d,True)
            
    #     else:
    #         raise AssertionError('error')
