from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = APIClient()

        # Create test instances of the Menu model
        menu_data = [
            {'Title': 'Menu 1', 'Price': '10.99', 'Inventory': 20},
            {'Title': 'Menu 2', 'Price': '15.50', 'Inventory': 15},
            {'Title': 'Menu 3', 'Price': '8.75', 'Inventory': 30},
        ]
        for data in menu_data:
            Menu.objects.create(
                Title=data['Title'],
                Price=data['Price'],
                Inventory=data['Inventory']
            )

    def test_getall(self):
        # Get the URL for the 'menu-list' view
        url = reverse('menu-list')

        # Perform a GET request to retrieve all Menu objects
        response = self.client.get(url)

        # Retrieve all Menu objects from the database
        menus = Menu.objects.all()

        # Serialize the Menu objects
        serializer = menuSerializer(menus, many=True)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data in the response equals the expected data
        self.assertEqual(response.data, serializer.data)
