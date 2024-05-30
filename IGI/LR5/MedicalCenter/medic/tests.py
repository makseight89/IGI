from django.test import TestCase
from django.urls import reverse
from .models import (
    Article,
    CompanyInfo,
    Term,
    Contact,
    Doctor,
    Vacancy,
    PromoCode,
    User,
    Favor,
    PlannedVisit,
    Client
)


class PagesTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            content="Test Content",
            image="test.jpg",
        )
        self.company_info = CompanyInfo.objects.create(text="Company Information")
        self.term = Term.objects.create(
            question="Test Question",
            answer="Test Answer",
        )
        self.contact = Contact.objects.create(
            doctor=Doctor.objects.create(
                name="Test Doctor",
                email="test@gmail.com",
                phone_number="+375 (29) 111-22-33",
                date_of_birth="1999-01-01",
            ),
            description="Test Description",
            photo="test.jpg",
        )
        self.vacancy = Vacancy.objects.create(
            title="Test Title",
            description="Test Description",
        )
        self.promocode = PromoCode.objects.create(
            code="TESTCODE",
            percentage=20,
            is_active=True,
        )

    def test_home_page_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.title)

    def test_about_page_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.company_info.text)

    def test_news_page_view(self):
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.title)

    def test_terms_page_view(self):
        response = self.client.get(reverse("terms"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.term.question)

    def test_contacts_page_view(self):
        response = self.client.get(reverse("contacts"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.contact.description)

    def test_privacy_policy_page_view(self):
        response = self.client.get(reverse("privacy_policy"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/privacy_policy_page.html")

    def test_vacancies_page_view(self):
        response = self.client.get(reverse("vacancies"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.vacancy.description)

    def test_promocodes_page_view(self):
        response = self.client.get(reverse("promocodes"))
        self.assertEqual(response.status_code, 302)


class AuthTests(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.profile_url = reverse("profile")
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            is_client=True,
            is_doctor=False,
        )

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            self.register_url,
            {
                "username": "newuser",
                "password1": "newpassword",
                "password2": "newpassword",
                "email": "newuser@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            self.login_url, {"username": "newuser", "password": "newpassword"}
        )
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username="newuser", password="newpassword")
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_user_model(self):
        self.assertEqual(self.user.is_client, True)
        self.assertEqual(self.user.is_doctor, False)


class StatisticTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            is_client=False,
            is_doctor=False,
        )
        self.client.force_login(self.user)

    def test_orders_stats_view(self):
        response = self.client.get(reverse("orders_stats"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "other/orders_stats.html")

    def test_planned_visits_stats_view(self):
        response = self.client.get(reverse("planned_visits_stats"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "other/planned_visits_stats.html")

    def test_sales_forecast_view(self):
        response = self.client.get(reverse("sales_forecast"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "other/sales_forecast.html")


class FavorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            is_client=False,
            is_doctor=False,
        )
        self.client.force_login(self.user)

        self.favor_data = {
            "description": "Test favor",
            "price": 1000,
        }
        self.favor_instance = Favor.objects.create(**self.favor_data)

    def test_favor_list_view(self):
        response = self.client.get(reverse("favor_list"))
        self.assertEqual(response.status_code, 200)

    def test_favor_detail_view(self):
        response = self.client.get(
            reverse("favor_detail", args=[self.favor_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_favor_create_view(self):
        response = self.client.get(reverse("favor_create"))
        self.assertEqual(response.status_code, 200)

    def test_favor_update_view(self):
        response = self.client.get(
            reverse("favor_update", args=[self.favor_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_favor_delete_view(self):
        response = self.client.get(
            reverse("favor_delete", args=[self.favor_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse("favor_delete", args=[self.favor_instance.pk])
        )
        self.assertEqual(response.status_code, 302)

        self.assertFalse(Favor.objects.filter(pk=self.favor_instance.pk).exists())


class DoctorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            is_client=False,
            is_doctor=False,
        )
        self.client.force_login(self.user)

        self.doctor_data = {
            "name": "Test Doctor",
            "email": "testdoctor@example.com",
            "phone_number": "+375 (29) 111-22-33",
            "date_of_birth": "1999-01-01",
        }
        self.doctor_instance = Doctor.objects.create(**self.doctor_data)

    def test_doctor_list_view(self):
        response = self.client.get(reverse("doctor_list"))
        self.assertEqual(response.status_code, 200)

    def test_doctor_detail_view(self):
        response = self.client.get(
            reverse("doctor_detail", args=[self.doctor_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_doctor_create_view(self):
        response = self.client.get(reverse("doctor_create"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse("doctor_create"), data=self.doctor_data)
        self.assertEqual(response.status_code, 302)

    def test_doctor_update_view(self):
        response = self.client.get(
            reverse("doctor_update", args=[self.doctor_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

        updated_data = {
            "name": "Updated Doctor",
            "email": "testdoctor@example.com",
            "phone_number": "+375 (29) 111-22-33",
            "date_of_birth": "1999-01-02",
        }
        response = self.client.post(
            reverse("doctor_update", args=[self.doctor_instance.pk]),
            data=updated_data,
        )
        self.assertEqual(response.status_code, 302)
        self.doctor_instance.refresh_from_db()

    def test_doctor_delete_view(self):
        response = self.client.get(
            reverse("doctor_delete", args=[self.doctor_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse("doctor_delete", args=[self.doctor_instance.pk])
        )
        self.assertEqual(response.status_code, 302)

        self.assertFalse(Doctor.objects.filter(pk=self.doctor_instance.pk).exists())


class ApiUtils(TestCase):
    def test_api_endpoint(self):
        response = self.client.get(reverse("jokes_and_facts"))
        self.assertEqual(response.status_code, 200)


class PlannedVisitTests(TestCase):
    def test_planed_visit_list_view(self):
        response = self.client.get(reverse("planned_visit_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "planned_visit/planned_visit_list.html")

    def test_planned_visit_create_view(self):
        response = self.client.get(reverse("planned_visit_create"))
        self.assertEqual(response.status_code, 302)


class ClientTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            is_client=False,
            is_doctor=False,
        )
        self.client.force_login(self.user)

        self.client_data = {
            "name": "Test Client",
            "email": "testclient@example.com",
            "phone_number": "+375 (29) 111-22-33",
            "date_of_birth": "1999-01-01",
        }
        self.client_instance = Client.objects.create(**self.client_data)

    def test_client_list_view(self):
        response = self.client.get(reverse("client_list"))
        self.assertEqual(response.status_code, 200)

    def test_client_detail_view(self):
        response = self.client.get(
            reverse("client_detail", args=[self.client_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_client_create_view(self):
        response = self.client.get(reverse("client_create"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse("client_create"), data=self.client_data)
        self.assertEqual(response.status_code, 302)

    def test_client_update_view(self):
        response = self.client.get(
            reverse("client_update", args=[self.client_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

        updated_data = {
            "name": "Updated Client",
            "email": "testclient@example.com",
            "phone_number": "+375 (29) 111-22-33",
            "date_of_birth": "1999-01-02",
        }
        response = self.client.post(
            reverse("client_update", args=[self.client_instance.pk]), data=updated_data
        )
        self.assertEqual(response.status_code, 302)
        self.client_instance.refresh_from_db()

    def test_client_delete_view(self):
        response = self.client.get(
            reverse("client_delete", args=[self.client_instance.pk])
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse("client_delete", args=[self.client_instance.pk])
        )
        self.assertEqual(response.status_code, 302)

        self.assertFalse(Client.objects.filter(pk=self.client_instance.pk).exists())
