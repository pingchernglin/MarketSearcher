from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache
from .models import Market

class MarketViewTests(TestCase):

    def setUp(self):
        # Create sample market objects
        market_data = [
            {'timestamp': '0x11111111', 'transactionhash': '0xdc35adbd81e4c5448317b60397c5d8cc1fda876f57d06621cfc5d1bec14aa62d', 'address': '0x972a785b390d05123497169a04c72de652493be1'},
            {'timestamp': '0x22222222', 'transactionhash': '0xdc35adbd81e4c5448317b60397c5d8cc1fda876f57d06621cfc5d1bec14aa62e', 'address': '0x666a785b390d05123497169a04c72de652493be2'}
        ]

        for market in market_data:
            Market.objects.create(
                timestamp=market['timestamp'],
                transactionhash=market['transactionhash'],
                address=market['address']
            )

    def test_markets_view(self):
        # Test the markets view
        response = self.client.get(reverse('markets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIn('mymarket', response.context)
        self.assertEqual(response.context['mymarket'].count(), 111)
 
    def test_get_update(self):
            # Test the get_update function
            cached_data = cache.get('market_data')
            self.assertIsNone(cached_data)
            response = self.client.get(reverse('markets'))
            cached_data = cache.get('market_data')
            self.assertIsNotNone(cached_data)
            self.assertEqual(len(cached_data), 111)

    def test_filter_time(self):
        # Test the filter_time view
        form_data = {'filter_time': '0x22222223'}
        response = self.client.post(reverse('filter_time'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIn('mymarket', response.context)
        self.assertEqual(response.context['mymarket'].count(), 2)
        form_data = {'filter_time': '0x11111112'}
        response = self.client.post(reverse('filter_time'), data=form_data)
        self.assertEqual(response.context['mymarket'].count(), 1)
    
    def test_filter_address(self):
        # Test the filter_address view
        form_data = {'filter_address': '0x666a785b390d05123497169a04c72de652493be2'}
        response = self.client.post(reverse('filter_address'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIn('mymarket', response.context)
        self.assertEqual(response.context['mymarket'].count(), 1)
