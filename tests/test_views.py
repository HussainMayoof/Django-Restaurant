from django.test import TestCase
from Restaurant.models import MenuItem
from Restaurant import serializers

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Burger", price=125, inventory=70)
        MenuItem.objects.create(title="Salad", price=55, inventory=30)

    def test_getall(self):
        items = MenuItem.objects.all()
        serializer = serializers.MenuItemSerializer(items, many=True)

        self.assertEqual(serializer.data[0]["title"], "IceCream")
        self.assertEqual(serializer.data[0]["price"], "80.00")
        self.assertEqual(serializer.data[0]["inventory"], 100)

        self.assertEqual(serializer.data[1]["title"], "Burger")
        self.assertEqual(serializer.data[1]["price"], "125.00")
        self.assertEqual(serializer.data[1]["inventory"], 70)

        self.assertEqual(serializer.data[2]["title"], "Salad")
        self.assertEqual(serializer.data[2]["price"], "55.00")
        self.assertEqual(serializer.data[2]["inventory"], 30)