from django.shortcuts import render, get_object_or_404, redirect
from ..models import Order, Favor
from ..forms import OrderForm
from ..decorator import role_required


@role_required("doctor")
def order_list(request):
    orders = Order.objects.all()
    return render(
        request,
        "order/order_list.html",
        {"orders": orders},
    )


@role_required("doctor")
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(
        request,
        "order/order_detail.html",
        {"order": order},
    )


@role_required("doctor")
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            selected_favors = request.POST.getlist("favors")
            favor_quantities = {}

            total_price = 0
            for favor_id in selected_favors:
                favor = Favor.objects.get(pk=favor_id)
                quantity = int(request.POST.get(f"quantity_{favor_id}", 0))

                favor_quantities[favor_id] = quantity
                total_price += favor.price * quantity

            order = form.save(commit=False)
            order.total_price = total_price
            order.save()
            order.favors.add(*selected_favors)
            order.favor_quantities = favor_quantities
            order.save()

            return redirect("order_list")
    else:
        form = OrderForm()
    all_favors = Favor.objects.all()

    context = {"form": form, "all_favors": all_favors}
    return render(request, "order/order_form.html", context)


@role_required("doctor")
def order_update(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            selected_favors = request.POST.getlist("favors")
            favor_quantities = {}

            total_price = 0
            for favor_id in selected_favors:
                favor = Favor.objects.get(pk=favor_id)
                quantity = int(request.POST.get(f"quantity_{favor_id}", 0))

                favor_quantities[favor_id] = quantity
                total_price += favor.price * quantity

            order.total_price = total_price
            order.favors.clear()
            order.favors.add(*selected_favors)
            order.favor_quantities = favor_quantities
            order.save()

            return redirect("order_list")
    else:
        initial_data = {
            "doctor": order.doctor,
            "client": order.client,
        }
        form = OrderForm(initial=initial_data, instance=order)

    all_favors = Favor.objects.all()
    context = {"form": form, "all_favors": all_favors}
    return render(request, "order/order_form.html", context)


@role_required("doctor")
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")
    return render(
        request,
        "order/order_confirm_delete.html",
        {"order": order},
    )
