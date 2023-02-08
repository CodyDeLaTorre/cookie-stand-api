from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Stand


class StandsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.stand = Stand.objects.create(
            location="Los Angeles",
            owner=self.user,
            description="This is our L.A., CA location",
            hourly_sales=[23],
            minimum_customers_per_hour=3,
            maximum_customers_per_hour=7,
            average_cookies_per_sale=9,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.stand), "Los Angeles")

    def test_stand_content(self):
        self.assertEqual(f"{self.stand.location}", "Los Angeles")
        self.assertEqual(f"{self.stand.owner}", "tester")
        self.assertEqual(self.stand.description, "This is our L.A., CA location")

    def test_stand_list_view(self):
        response = self.client.get(reverse("stand_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Los Angeles")
        self.assertTemplateUsed(response, "stand_list.html")

    def test_stand_detail_view(self):
        response = self.client.get(reverse("stand_detail", args="1"))
        no_response = self.client.get("/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Owner: tester")
        self.assertTemplateUsed(response, "stand_detail.html")

    def test_stand_create_view(self):
        response = self.client.post(
            reverse("stand_create"),
            {
                "location": "Dallas",
                "owner": self.user.id,
                "description": "Dallas Location",
                "hourly_sales": [24],
                "minimum_customers_per_hour": 4,
                "maximum_customers_per_hour": 8,
                "average_cookies_per_sale": 10,
            }, follow=True
        )

        self.assertRedirects(response, reverse("stand_detail", args="2"))
        self.assertContains(response, "Dallas")

    def test_stand_update_view_redirect(self):
        response = self.client.post(
            reverse("stand_update", args="1"),
            {
                "location": "Chicago",
                "owner": self.user.id,
                "description": "Chicago Location",
                "hourly_sales": [25],
                "minimum_customers_per_hour": 5,
                "maximum_customers_per_hour": 9,
                "average_cookies_per_sale": 11,
            }
        )

        self.assertRedirects(response, reverse("stand_detail", args="1"), target_status_code=200)

    def test_stand_update_bad_url(self):
        response = self.client.post(
            reverse("stand_update", args="1"),
            {
                "location": "Chicago",
                "owner": self.user.id,
                "description": "Chicago Location",
                "hourly_sales": [25],
                "minimum_customers_per_hour": 5,
                "maximum_customers_per_hour": 9,
                "average_cookies_per_sale": 11,
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_stand_delete_view(self):
        response = self.client.get(reverse("stand_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    # you can also tests models directly
    def test_model(self):
        stand = Stand.objects.create(location="Los Angeles", owner=self.user)
        self.assertEqual(stand.location, "Los Angeles")
