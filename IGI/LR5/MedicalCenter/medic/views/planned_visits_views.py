from django.shortcuts import render, get_object_or_404, redirect
from ..models import PlannedVisit
from ..forms import PlannedVisitForm
from ..decorator import role_required


def planned_visit_list(request):
    planned_visits = PlannedVisit.objects.all()
    return render(
        request,
        "planned_visit/planned_visit_list.html",
        {"planned_visits": planned_visits},
    )


def planned_visit_detail(request, pk):
    planned_visit = get_object_or_404(PlannedVisit, pk=pk)
    return render(
        request,
        "planned_visit/planned_visit_detail.html",
        {"planned_visit": planned_visit},
    )


@role_required("doctor")
def planned_visit_create(request):
    if request.method == "POST":
        form = PlannedVisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("planned_visit_list")
    else:
        form = PlannedVisitForm()
    return render(request, "planned_visit/planned_visit_form.html", {"form": form})


@role_required("doctor")
def planned_visit_update(request, pk):
    planned_visit = get_object_or_404(PlannedVisit, pk=pk)
    if request.method == "POST":
        form = PlannedVisitForm(request.POST, instance=planned_visit)
        if form.is_valid():
            form.save()
            return redirect("planned_visit_list")
    else:
        form = PlannedVisitForm(instance=planned_visit)
    return render(request, "planned_visit/planned_visit_form.html", {"form": form})


@role_required("doctor")
def planned_visit_delete(request, pk):
    planned_visit = get_object_or_404(PlannedVisit, pk=pk)
    if request.method == "POST":
        planned_visit.delete()
        return redirect("planned_visit_list")
    return render(
        request,
        "planned_visit/planned_visit_confirm_delete.html",
        {"planned_visit": planned_visit},
    )
