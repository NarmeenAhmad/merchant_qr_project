from django.shortcuts import render
from .forms import QRForm
import qrcode
import os
from django.conf import settings



def home(request):
    if request.method=='POST':
        form=QRForm(request.POST)
        if form.is_valid():
            res_name=form.cleaned_data['Restaurant_name']
            url=form.cleaned_data['url']
            qr=qrcode.make(url)
            file_name=res_name.replace(' ','_').lower() + "_menu.png"
            file_path=os.path.join(settings.MEDIA_ROOT,file_name)
            qr.save(file_path)
            qr_url=os.path.join(settings.MEDIA_URL,file_name)
            return render(request,'result.html',{'res_name':res_name,'qr_url':qr_url,'file_name':file_name })
    else:
        form=QRForm()
        return render(request,'home.html',{'form':form})