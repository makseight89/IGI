from django.shortcuts import render, get_object_or_404, redirect
from ..models import Doctor
from ..forms import DoctorForm
from ..decorator import role_required


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor/doctor_list.html", {"doctors": doctors})


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, "doctor/doctor_detail.html", {"doctor": doctor})


@role_required("doctor")
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm()
    return render(request, "doctor/doctor_form.html", {"form": form})


@role_required("doctor")
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm(instance=doctor)
    return render(request, "doctor/doctor_form.html", {"form": form})


@role_required("doctor")
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect("doctor_list")
    return render(request, "doctor/doctor_confirm_delete.html", {"doctor": doctor})
