from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Doctor, Client, Favor, PlannedVisit, Diagnosis, Order


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ClientForm(BaseModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'date_of_birth']


class DoctorForm(BaseModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'phone_number', 'date_of_birth']


class FavorForm(BaseModelForm):
    class Meta:
        model = Favor
        fields = ['description', 'price']


class PlannedVisitForm(BaseModelForm):
    class Meta:
        model = PlannedVisit
        fields = ['client', 'doctor', 'date', 'start_time', 'end_time']


class DiagnosisForm(BaseModelForm):
    class Meta:
        model = Diagnosis
        fields = ['name', 'client', 'doctor']


class OrderForm(BaseModelForm):
    class Meta:
        model = Order
        fields = ['doctor', 'client']


class RegistrationForm(UserCreationForm):
    USER_TYPES = (
        ('client', 'Client'),
        ('doctor', 'Doctor'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect, required=True, initial='client')
    phone_number = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'date_of_birth']

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        name = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        if user_type == 'client':
            user.is_client = True
        elif user_type == 'doctor':
            user.is_doctor = True

        user.save()

        if user_type == 'client':
            Client.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                date_of_birth=date_of_birth,
                user=user
            )
        elif user_type == 'doctor':
            Doctor.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                date_of_birth=date_of_birth,
                user=user
            )

        return user
