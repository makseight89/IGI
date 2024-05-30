from django.shortcuts import render
from ..models import DoctorCategory, DoctorSpecialization, Department, ReceptionSchedule
from ..decorator import role_required


def custom_404(request, exception):
    return render(request, "other/404.html", status=404)


def doctor_category_list(request):
    categories = DoctorCategory.objects.all()
    return render(
        request,
        "other/category_list.html",
        {"categories": categories},
    )


def doctor_specialization_list(request):
    specializations = DoctorSpecialization.objects.all()
    return render(
        request,
        "other/specialization_list.html",
        {"specializations": specializations},
    )


def department_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "other/department_list.html",
        {"departments": departments},
    )


@role_required("client")
def schedule_list(request):
    schedules = ReceptionSchedule.objects.all()
    return render(
        request,
        "other/schedule_list.html",
        {"schedules": schedules},
    )
