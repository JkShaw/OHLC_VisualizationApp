import json

from django import forms
from django.core.serializers.json import DjangoJSONEncoder

from django.http import HttpResponse, HttpResponseBadRequest

from django.shortcuts import render, render_to_response

from django.template import RequestContext

import django_excel as excel

from .models import StockData


class UploadFileForm(forms.Form):
    """Upload file form."""

    file = forms.FileField()


def index(request):
    """Index page."""
    return render(request, 'index.html')


def get_data(request):
    """Get Stock date from db in JSON format."""
    if request.method == 'GET':
        stockid = request.GET.get('stock')
        records = (StockData.objects.filter(stock=stockid).order_by(
            'date').values(
                'date', 'open', 'high', 'low',
                'close', 'volume', 'adjusted'))
        records = records
        json_customers = json.dumps(list(records), cls=DjangoJSONEncoder)
    return HttpResponse(json_customers)


def upload(request):
    """Upload file to convert it into csv format."""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render_to_response(
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file')
        },
        context_instance=RequestContext(request))


def import_data(request):
    """Import file to store in db table stockData."""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                request.FILES['file'].save_to_database(
                    name_columns_by_row=2,
                    model=StockData,
                    mapdict=[
                        'trade_date', 'open_price',
                        'high_price', 'low_price',
                        'close_price', 'volume',
                        'adj_close', 'stock'])
            except Exception as e:
                return HttpResponse(str(e))
            else:
                return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render_to_response(
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database',
            'header': 'Please upload Stock excel file:'
        },
        context_instance=RequestContext(request))
