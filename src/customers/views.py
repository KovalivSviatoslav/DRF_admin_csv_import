import csv
from datetime import datetime

from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .forms import CsvImportForm
from .models import Customer


# Create your views here.
from .serializers import CustomerSerializer


def import_csv(request):
    if request.method == "POST":
        form = CsvImportForm(request.POST, request.FILES)

        if form.is_valid():
            upload_file = request.FILES["csv_file"]
            reader = csv.reader(upload_file.read().decode('UTF-8').splitlines())
            next(reader)

            data = [Customer(
                first_name=row[0],
                last_name=row[1],
                date_of_birth=datetime.strptime(row[2], '%Y/%m/%d').strftime('%Y-%m-%d'),
                created_at=datetime.strptime(row[3], '%Y/%m/%d').strftime('%Y-%m-%d')
            ) for row in reader]

            Customer.objects.bulk_create(data)

            return redirect("..")

    form = CsvImportForm()
    payload = {"form": form}
    return render(request, "csv_form.html", payload)


class CustomersViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['created_at']
