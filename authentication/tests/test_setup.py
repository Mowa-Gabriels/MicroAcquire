from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


# Create your tests here.


class TestSetUp(APITestCase):

    def setUp(self):

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()

        self.user_data = {
            "email": self.fake.email(),
            "first_name": self.fake.email().split('@')[0],
            "password":"temilade"

        }
        import pdb ; pdb.set_trace()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()