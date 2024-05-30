from django.http import HttpResponse
from django.db.models import Sum
from django.shortcuts import render
import io
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from statistics import mean, mode, median
from datetime import datetime, timedelta
from ..models import Order, PlannedVisit, Doctor
from ..decorator import role_required


@role_required("superuser")
def orders_stats_view(request):
    orders = Order.objects.all()
    order_data = orders.values("doctor__name").annotate(total_cost=Sum("total_price"))

    doctor_names = [item["doctor__name"] for item in order_data]
    total_costs = [item["total_cost"] for item in order_data]

    plt.figure(figsize=(10, 6))
    plt.bar(doctor_names, total_costs)
    plt.xlabel("Doctor")
    plt.ylabel("Total Cost")
    plt.title("Total Cost of Orders by Doctor")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)

    plot_data = buffer.getvalue()
    buffer.close()

    return render(request, "other/orders_stats.html", {"plot_data": plot_data})


@role_required("superuser")
def planned_visits_stats_view(request):
    if request.method == "GET":
        doctor_id = request.GET.get("doctor")
        visit_date = request.GET.get("visit_date")

        if doctor_id and visit_date:
            doctor = Doctor.objects.get(id=doctor_id)
            doctors = Doctor.objects.all()
            visits = PlannedVisit.objects.filter(doctor=doctor, date=visit_date)
            clients = [visit.client for visit in visits]
            context = {
                "doctor": doctor,
                "doctors": doctors,
                "visit_date": visit_date,
                "clients": clients,
            }
            return render(request, "other/planned_visits_stats.html", context)

    doctors = Doctor.objects.all()
    context = {
        "doctors": doctors,
    }
    return render(request, "other/planned_visits_stats.html", context)


@role_required("superuser")
def sales_forecast_view(
    request,
):  # Линейный тренд продаж, Прогноз продаж, статистические показатели (среднее, мода и медиана) по сумме продаж
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)

    sales_amounts = Order.objects.filter(
        date_ordered__range=[start_date, end_date]
    ).values_list("total_price", flat=True)

    total_sales = sum(sales_amounts)
    total_sales = total_sales or 0

    days = (end_date - start_date).days + 1
    average_daily_sales = total_sales / days

    projected_sales = average_daily_sales * 30

    if len(sales_amounts) > 0:
        sales_mean = mean(sales_amounts)
        sales_mode = mode(sales_amounts)
        sales_median = median(sales_amounts)
    else:
        sales_mean = 0
        sales_mode = 0
        sales_median = 0

    context = {
        "start_date": start_date,
        "end_date": end_date,
        "total_sales": total_sales,
        "average_daily_sales": average_daily_sales,
        "projected_sales": projected_sales,
        "sales_mean": sales_mean,
        "sales_mode": sales_mode,
        "sales_median": sales_median,
    }

    return render(request, "other/sales_forecast.html", context)
