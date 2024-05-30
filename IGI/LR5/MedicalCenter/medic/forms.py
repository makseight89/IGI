from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Doctor, Client, Favor, PlannedVisit, Diagnosis, Order


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "email", "phone_number", "date_of_birth"]


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "email", "phone_number", "date_of_birth"]


class FavorForm(forms.ModelForm):
    class Meta:
        model = Favor
        fields = ["description", "price"]


class PlannedVisitForm(forms.ModelForm):
    class Meta:
        model = PlannedVisit
        fields = ["client", "doctor", "date", "start_time", "end_time"]


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ["name", "client", "doctor"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["doctor", "client"]


class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=[("client", "Client"), ("doctor", "Doctor")],
        widget=forms.RadioSelect,
        required=True,
        initial="client",
    )
    phone_number = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "date_of_birth",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get("user_type")
        name = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        phone_number = self.cleaned_data.get("phone_number")
        date_of_birth = self.cleaned_data.get("date_of_birth")

        if user_type == "client":
            user.is_client = True
            user.save()
            Client.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                date_of_birth=date_of_birth,
            )
        elif user_type == "doctor":
            user.is_doctor = True
            user.save()
            Doctor.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                date_of_birth=date_of_birth,
            )

        return user
