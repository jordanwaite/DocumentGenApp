from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from nrotc.scripts import gens
from docx import Document

from .forms import PRBConvOrderForm, PRBReportForm
from .models import Members

def home_view(response):
    person = Members.objects.all()
    context = {
        'person': person,
    }
    return render(response, 'nrotc/index.html', context)

def contact_view(response):
    context = {
    }
    return render(response, 'nrotc/contact.html', context)

def download_docx(request):
    document = gens.createPRBConveningOrder()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    document.save(response)

    return response

def conv_order_view(request):
    if request.method == 'POST':
        form = PRBConvOrderForm(request.POST)
        if form.is_valid():
            Members.objects.create(**form.cleaned_data)
            document = gens.createPRBConveningOrder()
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=download.docx'
            document.save(response)

            return response

    else:
        form = PRBConvOrderForm(request.POST)

    context = {
        'form_PRB_conv_order': form,
    }
    return render(request, 'nrotc/conv-order.html', context)

def prb_report_view(request):
    if request.method == 'POST':
        form = PRBReportForm(request.POST)
        print('prb report method is post')
        if form.is_valid():
            print('prb report form is valid')
            Members.objects.create(**form.cleaned_data)
            
            document = gens.createPRBReport()
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=download.docx'
            document.save(response)

            return response
            # return HttpResponseRedirect('/download')

        else:
            for error in form.errors:
                print(error)
    else:
        form = PRBReportForm(request.POST)   
    
    context = {
        'form_PRB_report': form,
    }
    return render(request, 'nrotc/prb-report.html', context)





def pns_rec_view(response):
    context = {
    }
    return render(response, 'nrotc/pns-rec.html', context)

def co_sum_letter_view(response):
    context = {
    }
    return render(response, 'nrotc/co-sum-letter.html', context)

def student_prb_waiver_view(response):
    context = {
    }
    return render(response, 'nrotc/student-prb-waiver.html', context)

def pns_prb_waiver_view(response):
    context = {
    }
    return render(response, 'nrotc/pns-prb-waiver.html', context)

def prb_date_change_view(response):
    context = {
    }
    return render(response, 'nrotc/prb-date-change.html', context)