from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date, timedelta


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CompanyInfo(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Term(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question


class Contact(models.Model):
    doctor = models.OneToOneField("Doctor", on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.doctor.name


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(
        choices=(
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        )
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    favor = models.ForeignKey("Favor", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(99)],
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r"^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$",
        message="Phone number must be in the format '+375 (29) XXX-XX-XX'",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=20, null=True)
    date_of_birth = models.DateField(
        validators=[MaxValueValidator(date.today() - timedelta(days=365 * 18))]
    )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r"^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$",
        message="Phone number must be in the format '+375 (29) XXX-XX-XX'",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=20, null=True)
    date_of_birth = models.DateField(
        validators=[MaxValueValidator(date.today() - timedelta(days=365 * 18))]
    )
    doctor_category = models.ForeignKey(
        "DoctorCategory", on_delete=models.CASCADE, null=True, related_name="doctors"
    )
    doctor_specialization = models.ForeignKey(
        "DoctorSpecialization", on_delete=models.CASCADE, null=True
    )
    doctor_department = models.ForeignKey(
        "DoctorCategory",
        on_delete=models.CASCADE,
        null=True,
        related_name="department_doctors",
    )

    def __str__(self):
        return self.name


class Favor(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DoctorCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    favors = models.ManyToManyField(Favor)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    favor_quantities = models.JSONField(encoder=DjangoJSONEncoder, default=dict)

    def __str__(self):
        return f"Order #{self.pk} - {self.client.name} - {self.date_ordered}"


class ReceptionSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day}"


class PlannedVisit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.client.name} - {self.doctor.name} - {self.date}"
