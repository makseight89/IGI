from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from ..models import Favor
from ..forms import FavorForm
from ..utils.date_utils import get_favor_time
from ..decorator import role_required


@role_required("client")
def favor_list(request):
    search_term = request.GET.get("search")
    sort_order = request.GET.get("sort")

    favors = Favor.objects.all()

    if search_term:
        favors = favors.filter(Q(description__icontains=search_term))

    if sort_order == "ascending":
        favors = favors.order_by("price")
    elif sort_order == "descending":
        favors = favors.order_by("-price")

    return render(request, "favor/favor_list.html", {"favors": favors})


@role_required("client")
def favor_detail(request, pk):
    favor = get_object_or_404(Favor, pk=pk)
    created_tz, updated_tz, created_utc, updated_utc = get_favor_time(favor)
    context = {
        "favor": favor,
        "created_tz": created_tz,
        "updated_tz": updated_tz,
        "created_utc": created_utc,
        "updated_utc": updated_utc,
    }
    return render(request, "favor/favor_detail.html", context)


@role_required("doctor")
def favor_create(request):
    if request.method == "POST":
        form = FavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("favor_list")
    else:
        form = FavorForm()
    return render(request, "favor/favor_form.html", {"form": form})


@role_required("doctor")
def favor_update(request, pk):
    favor = get_object_or_404(Favor, pk=pk)
    if request.method == "POST":
        form = FavorForm(request.POST, instance=favor)
        if form.is_valid():
            form.save()
            return redirect("favor_list")
    else:
        form = FavorForm(instance=favor)
    return render(request, "favor/favor_form.html", {"form": form})


@role_required("doctor")
def favor_delete(request, pk):
    favor = get_object_or_404(Favor, pk=pk)
    if request.method == "POST":
        favor.delete()
        return redirect("favor_list")
    return render(request, "favor/favor_confirm_delete.html", {"favor": favor})
