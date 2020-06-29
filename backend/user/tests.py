import json
from django.contrib.auth.models import User
from django.forms import model_to_dict

from django.test import TransactionTestCase

from user.models import DeliveryAddress


class AddressCreationTest(TransactionTestCase):
    def test_create_address(self):
        """
        tests that the address information is saved to the database.
        """
        self.maxDiff = None

        user_email = 'cristina@gmail.com'
        user = User.objects.create(username=user_email, email=user_email, password='password')

        response = self.client.post(
            path=f'/api/v1/user/{user.email}/address/',
            data=json.dumps({
                "first_name": "first_name",
                "last_name": "last_name",
                "street_address": "street_address",
                "apt_nr": 3,
                "postal_code": 1245,
                "city": "city",
                "country": "country",
            }),
            content_type="application/json")

        new_address = DeliveryAddress.objects.get(user=user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_address.user, user)

    def test_create_unique_address(self):
        """
        tests that if the address already exists 200 status code is returned and the address is not added to
        the database.
        """
        self.maxDiff = None

        user_email = 'cristina@gmail.com'
        user = User.objects.create(username=user_email, email=user_email, password='password')

        self.client.post(
            path=f'/api/v1/user/{user.email}/address/',
            data=json.dumps({
                "first_name": "first_name",
                "last_name": "last_name",
                "street_address": "street_address",
                "apt_nr": 3,
                "postal_code": 1245,
                "city": "city",
                "country": "country",
            }),
            content_type="application/json")

        response = self.client.post(
            path=f'/api/v1/user/{user.email}/address/',
            data=json.dumps({
                "first_name": "first_name",
                "last_name": "last_name",
                "street_address": "street_address",
                "apt_nr": 3,
                "postal_code": 1245,
                "city": "city",
                "country": "country",
            }),
            content_type="application/json")

        address_count = DeliveryAddress.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(address_count, 1)


class AddressRetrieveTest(TransactionTestCase):
    def test_retrieve_address(self):
        """
        tests that the address information is retrieved from the database.
        """
        self.maxDiff = None

        user_email = 'cristina@gmail.com'
        user = User.objects.create(username=user_email, email=user_email, password='password')
        DeliveryAddress.objects.create(first_name='cristina', last_name='garbuz',
                                       street='street', apt_nr=21, user=user,
                                       zip_code=14, city='Stockholm', country='Sweden')

        response = self.client.get(
            path=f'/api/v1/user/{user.email}/address/')

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            'address': {'apt_nr': 21,
                        'city': 'Stockholm',
                        'country': 'Sweden',
                        'first_name': 'cristina',
                        'id': 1,
                        'last_name': 'garbuz',
                        'street': 'street',
                        'user': 1,
                        'zip_code': 14}
        })

    def test_retrieve_latest_address(self):
        """
        tests that the address information is retrieved from the database.
        """
        self.maxDiff = None

        user_email = 'cristina@gmail.com'
        user = User.objects.create(username=user_email, email=user_email, password='password')
        DeliveryAddress.objects.create(first_name='cristina', last_name='garbuz',
                                       street='street', apt_nr=21, user=user,
                                       zip_code=14, city='Stockholm', country='Sweden')
        DeliveryAddress.objects.create(first_name='cristina23', last_name='garbuz23',
                                       street='street', apt_nr=21, user=user,
                                       zip_code=14, city='Stockholm', country='Sweden')

        response = self.client.get(
            path=f'/api/v1/user/{user.email}/address/')

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            'address': {'apt_nr': 21,
                        'city': 'Stockholm',
                        'country': 'Sweden',
                        'first_name': 'cristina23',
                        'id': 2,
                        'last_name': 'garbuz23',
                        'street': 'street',
                        'user': 1,
                        'zip_code': 14}
        })
