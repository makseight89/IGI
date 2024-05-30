from django.shortcuts import render, get_object_or_404, redirect
from ..models import Client
from ..forms import ClientForm
from ..decorator import role_required


@role_required("doctor")
def client_list(request):
    clients = Client.objects.all()
    return render(
        request,
        "client/client_list.html",
        {"clients": clients},
    )


@role_required("doctor")
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(
        request,
        "client/client_detail.html",
        {"client": client},
    )


@role_required("doctor")
def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm()
    return render(request, "client/client_form.html", {"form": form})


@role_required("doctor")
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm(instance=client)
    return render(request, "client/client_form.html", {"form": form})


@role_required("doctor")
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("client_list")
    return render(
        request,
        "client/client_confirm_delete.html",
        {"client": client},
    )
