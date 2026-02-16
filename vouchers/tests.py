from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class VoucherViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_url = reverse('dashboard')

    @patch('vouchers.model_voucher.Voucher.count_vouches_by_status')
    def test_dashboard_page_context_counts(self, mock_count):
        mock_count.side_effect = [10, 5, 20, 2]

        response = self.client.get(self.dashboard_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['active_count'], 10)
        self.assertEqual(response.context['sold_count'], 20)

        self.assertEqual(mock_count.call_count, 4)