from django.shortcuts import render, get_object_or_404, redirect
from ..models import Diagnosis
from ..forms import DiagnosisForm
from ..decorator import role_required


@role_required("doctor")
def diagnosis_list(request):
    diagnoses = Diagnosis.objects.all()
    return render(request, "diagnosis/diagnosis_list.html", {"diagnoses": diagnoses})


@role_required("doctor")
def diagnosis_detail(request, pk):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    return render(request, "diagnosis/diagnosis_detail.html", {"diagnosis": diagnosis})


@role_required("doctor")
def diagnosis_create(request):
    if request.method == "POST":
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diagnosis_list")
    else:
        form = DiagnosisForm()
    return render(request, "diagnosis/diagnosis_form.html", {"form": form})


@role_required("doctor")
def diagnosis_update(request, pk):
    diagnosis = get_object_or_404(DiagnosisForm, pk=pk)
    if request.method == "POST":
        form = DiagnosisForm(request.POST, instance=diagnosis)
        if form.is_valid():
            form.save()
            return redirect("diagnosis_list")
    else:
        form = DiagnosisForm(instance=diagnosis)
    return render(request, "diagnosis/diagnosis_form.html", {"form": form})


@role_required("doctor")
def diagnosis_delete(request, pk):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    if request.method == "POST":
        diagnosis.delete()
        return redirect("diagnosis_list")
    return render(
        request, "diagnosis/diagnosis_confirm_delete.html", {"diagnosis": diagnosis}
    )
