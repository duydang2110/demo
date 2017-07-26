from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Asset
from .forms import AssetForm
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


