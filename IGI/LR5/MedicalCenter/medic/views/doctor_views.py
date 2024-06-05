from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor
from .forms import DoctorForm
from .decorators import role_required


@login_required
def doctor_list(request):
    if request.user.is_doctor:
        doctors = Doctor.objects.all()
        return render(request, "doctor/doctor_list.html", {"doctors": doctors})
    else:
        return redirect("home")


@login_required
def doctor_detail(request, pk):
    if request.user.is_doctor:
        doctor = get_object_or_404(Doctor, pk=pk)
        return render(request, "doctor/doctor_detail.html", {"doctor": doctor})
    else:
        return redirect("home")


@role_required("doctor")
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm()
    return render(request, "doctor/doctor_form.html", {"form": form})


@role_required("doctor")
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk, user=request.user)
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
    doctor = get_object_or_404(Doctor, pk=pk, user=request.user)
    if request.method == "POST":
        doctor.delete()
        return redirect("doctor_list")
    return render(request, "doctor/doctor_confirm_delete.html", {"doctor": doctor})
