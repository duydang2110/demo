from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms.models import modelformset_factory
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings


from .models import Asset,History,Driver
from .forms import AssetForm,HistoryForm
# Create your views here.

@login_required(login_url="login")
def save_asset_form(request,form,template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            assets = Asset.objects.all()
            data['html_asset_list'] = render_to_string('asset_tracking/partial_asset_list.html',{'assets':assets})
        else:
            data['form_is_valid'] = False
    else:
        data['form_is_valid'] = False
    context = {'form':form}
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)


@login_required(login_url="login")
def asset_list(request):
    assets = Asset.objects.all()
    return render(request,'asset_tracking/asset_list.html',{'assets':assets})


@login_required(login_url="login")
def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
    else:
        form = AssetForm()
    return save_asset_form(request, form, 'asset_tracking/partial_asset_create.html')


@login_required(login_url="login")
def asset_update(request,pk):
    asset = get_object_or_404(Asset,pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST,instance=asset)
    else:
        form = AssetForm(instance=asset)
    return save_asset_form(request,form, 'asset_tracking/partial_asset_update.html')


@login_required(login_url="login")
def asset_delete(request,pk):
    asset = get_object_or_404(Asset,pk=pk)
    data = dict()
    if request.method == 'POST':
        asset.delete()
        data['form_is_valid'] = True
        assets = Asset.objects.all()
        data['html_asset_list'] = render_to_string('asset_tracking/partial_asset_list.html',{'assets':assets})
    else:
        context = {'asset':asset}
        data['html_form'] = render_to_string('asset_tracking/partial_asset_delete.html',context,request=request)

    return JsonResponse(data)


@login_required(login_url="login")
def history_create(request,pk):
    asset_id = pk
    if request.method == 'POST':
        form = HistoryForm(request.POST,initial={'maasset' : asset_id})
    else:
        form = HistoryForm(initial={'maasset' : asset_id})
    return save_history_form(request,form,'asset_tracking/partial_history_create.html',asset_id)

@login_required(login_url="login")
def save_history_form(request,form,template_name,asset_id):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            asset = Asset.objects.get(pk=asset_id)
            asset.total += form.cleaned_data['gia']
            asset.save()
            data['form_is_valid'] = True
            assets = Asset.objects.all()
            data['html_asset_list'] = render_to_string('asset_tracking/partial_asset_list.html',{'assets':assets})
        else:
            data['form_is_valid'] = False
    else:
        data['form_is_valid'] = False


    context = {'form':form,
               'asset_id':asset_id
               }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url="login")
def report(request):
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            sp = form.save(commit=False)
            sp.save()
            return redirect('report')
    else:
        form = HistoryForm()
    return render(request, 'asset_tracking/report.html', {'form': form})

@login_required(login_url="login")
def get_data(request):
    data = {
        "sale":100,
        "customers":10,
    }
    return JsonResponse(data)

class ChartData(LoginRequiredMixin,APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        assets = Asset.objects.all()
        default = []
        labels = []
        for asset in assets:
            labels.append(asset.name)
            default.append(asset.total)

        data = {
            "labels": labels,
            "default": default,
            "customers": 10,
        }
        return Response(data)


class GeneratePdf(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        assets = Asset.objects.all()
        data = {
            'today': datetime.date.today(),
            'amount': 39.99,
            'customer_name': 'DEV2',
            'order_id': 1233434,
            'assets': assets,
        }
        pdf = render_to_pdf('asset_tracking/pdfreport.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
