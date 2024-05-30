from django.urls import re_path
from django.contrib.auth import views as login_views
from .views.pages_views import (
    home_page_view,
    about_page_view,
    news_page_view,
    terms_page_view,
    contacts_page_view,
    privacy_policy_page_view,
    vacancies_page_view,
    reviews_page_view,
    add_review_page_view,
    promocodes_page_view,
)
from .views.client_views import *
from .views.doctor_views import *
from .views.diagnosis_views import *
from .views.favor_views import *
from .views.planned_visits_views import *
from .views.jokes_and_facts import *
from .views.order_views import *
from .views.other_views import (
    doctor_category_list,
    doctor_specialization_list,
    department_list,
    schedule_list,
)
from .views.statistic_views import (
    orders_stats_view,
    planned_visits_stats_view,
    sales_forecast_view,
)
from .views.auth_views import logout_view, register_view, profile_view

pages_urls = [
    re_path(r"^$", home_page_view, name="home"),
    re_path(r"^about/$", about_page_view, name="about"),
    re_path(r"^news/$", news_page_view, name="news"),
    re_path(r"^terms/$", terms_page_view, name="terms"),
    re_path(r"^contacts/$", contacts_page_view, name="contacts"),
    re_path(r"^privacy_policy/$", privacy_policy_page_view, name="privacy_policy"),
    re_path(r"^vacancies/$", vacancies_page_view, name="vacancies"),
    re_path(r"^reviews/$", reviews_page_view, name="reviews"),
    re_path(
        r"^favors/(?P<pk>\d+)/add_review/$", add_review_page_view, name="add_review"
    ),
    re_path(r"^promocodes/$", promocodes_page_view, name="promocodes"),
]

client_urls = [
    re_path(r"^clients/$", client_list, name="client_list"),
    re_path(r"^clients/(?P<pk>\d+)/$", client_detail, name="client_detail"),
    re_path(r"^clients/create/$", client_create, name="client_create"),
    re_path(r"^clients/(?P<pk>\d+)/update/$", client_update, name="client_update"),
    re_path(r"^clients/(?P<pk>\d+)/delete/$", client_delete, name="client_delete"),
]

doctor_urls = [
    re_path(r"^doctors/$", doctor_list, name="doctor_list"),
    re_path(r"^doctors/(?P<pk>\d+)/$", doctor_detail, name="doctor_detail"),
    re_path(r"^doctors/create/$", doctor_create, name="doctor_create"),
    re_path(r"^doctors/(?P<pk>\d+)/update/$", doctor_update, name="doctor_update"),
    re_path(r"^doctors/(?P<pk>\d+)/delete/$", doctor_delete, name="doctor_delete"),
]

order_urls = [
    re_path(r"^orders/$", order_list, name="order_list"),
    re_path(r"^orders/(?P<pk>\d+)/$", order_detail, name="order_detail"),
    re_path(r"^orders/create/$", order_create, name="order_create"),
    re_path(r"^orders/(?P<pk>\d+)/update/$", order_update, name="order_update"),
    re_path(r"^orders/(?P<pk>\d+)/delete/$", order_delete, name="order_delete"),
]

planned_visit_urls = [
    re_path(r"^planned_visit/$", planned_visit_list, name="planned_visit_list"),
    re_path(
        r"^planned_visit/(?P<pk>\d+)/$",
        planned_visit_detail,
        name="planned_visit_detail",
    ),
    re_path(
        r"^planned_visit/create/$", planned_visit_create, name="planned_visit_create"
    ),
    re_path(
        r"^planned_visit/(?P<pk>\d+)/update/$",
        planned_visit_update,
        name="planned_visit_update",
    ),
    re_path(
        r"^planned_visit/(?P<pk>\d+)/delete/$",
        planned_visit_delete,
        name="planned_visit_delete",
    ),
]

diagnosis_urls = [
    re_path(r"^diagnosis/$", diagnosis_list, name="diagnosis_list"),
    re_path(r"^diagnosis/(?P<pk>\d+)/$", diagnosis_detail, name="diagnosis_detail"),
    re_path(r"^diagnosis/create/$", diagnosis_create, name="diagnosis_create"),
    re_path(
        r"^diagnosis/(?P<pk>\d+)/update/$", diagnosis_update, name="diagnosis_update"
    ),
    re_path(
        r"^diagnosis/(?P<pk>\d+)/delete/$", diagnosis_delete, name="diagnosis_delete"
    ),
]

favor_urls = [
    re_path(r"^favors/$", favor_list, name="favor_list"),
    re_path(r"^favors/(?P<pk>\d+)/$", favor_detail, name="favor_detail"),
    re_path(r"^favors/create/$", favor_create, name="favor_create"),
    re_path(r"^favors/(?P<pk>\d+)/update/$", favor_update, name="favor_update"),
    re_path(r"^favors/(?P<pk>\d+)/delete/$", favor_delete, name="favor_delete"),
]

jokes_and_facts_urls = [
    re_path(r"^jokes_and_facts/$", jokes_and_facts_view, name="jokes_and_facts"),
]

other_urls = [
    re_path(r"^doctor_categories/$", doctor_category_list, name="doctor_category_list"),
    re_path(
        r"^doctor_specializations/$",
        doctor_specialization_list,
        name="doctor_specialization_list",
    ),
    re_path(r"^departments/$", department_list, name="department_list"),
    re_path(r"^schedules/$", schedule_list, name="schedule_list"),
]

statistic_urls = [
    re_path(r"^orders_stats/$", orders_stats_view, name="orders_stats"),
    re_path(
        r"^planned_visits_stats/$",
        planned_visits_stats_view,
        name="planned_visits_stats",
    ),
    re_path(
        r"^sales_forecast/$", sales_forecast_view, name="sales_forecast"
    ),
]

auth_urls = [
    re_path(
        r"^login/$",
        login_views.LoginView.as_view(
            template_name="auth/login.html", next_page="profile"
        ),
        name="login",
    ),
    re_path(r"^logout/$", logout_view, name="logout"),
    re_path(r"^register/$", register_view, name="register"),
    re_path(r"^profile/$", profile_view, name="profile"),
]

urlpatterns = []
urlpatterns += pages_urls
urlpatterns += auth_urls
urlpatterns += client_urls
urlpatterns += doctor_urls
urlpatterns += planned_visit_urls
urlpatterns += diagnosis_urls
urlpatterns += favor_urls
urlpatterns += jokes_and_facts_urls
urlpatterns += other_urls
urlpatterns += order_urls
urlpatterns += statistic_urls
