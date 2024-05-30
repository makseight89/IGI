from django.contrib import admin
from .models import (
    User,
    Article,
    CompanyInfo,
    Term,
    Contact,
    Vacancy,
    Review,
    PromoCode,
    Client,
    Doctor,
    Favor,
    Diagnosis,
    DoctorCategory,
    DoctorSpecialization,
    Department,
    Order,
    ReceptionSchedule,
    PlannedVisit,
)


admin.site.register(User)
admin.site.register(Article)
admin.site.register(CompanyInfo)
admin.site.register(Term)
admin.site.register(Contact)
admin.site.register(Vacancy)
admin.site.register(Review)
admin.site.register(PromoCode)
admin.site.register(Doctor)
admin.site.register(Favor)
admin.site.register(Diagnosis)
admin.site.register(DoctorCategory)
admin.site.register(DoctorSpecialization)
admin.site.register(Department)
admin.site.register(ReceptionSchedule)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone_number", "date_of_birth"]


class PlannedVisitAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "doctor", "date", "start_time", "end_time"]
    list_filter = ("client",)
    ordering = ("date", "client__name")


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "doctor", "client", "date_ordered", "total_price"]
    list_filter = ("client",)


admin.site.register(PlannedVisit, PlannedVisitAdmin)
admin.site.register(Order, OrderAdmin)
