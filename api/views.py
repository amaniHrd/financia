
from audioop import reverse
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from .models import Tab_aux

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import openpyxl
import pandas as pd
from io import BytesIO
from .forms import TabAuxForm
from api.utils.functions import *


def api(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello world!")

def download_excel(request):
    # Assuming you have some content to put in the Excel file
    file_path = os.path.join(settings.MEDIA_ROOT, 'journal17.xlsx')
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Create a Django response with the Excel file
    response = HttpResponse(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=journal17.xlsx'

    return response


def download_rap(request):
    # Assuming you have some content to put in the Excel file
    rap_path = os.path.join(settings.MEDIA_ROOT, 'rapprochement.xlsx')
    with open(rap_path, 'rb') as file:
        file_content = file.read()

    # Create a Django response with the Excel file
    response = HttpResponse(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=rapprochement.xlsx'

    return response



def handle_files(request):

    if request.method == 'POST':
        billet = request.FILES.get('fileInput1')
        fact = request.FILES.get('fileInput2')
        aux = request.FILES.get('fileInput3')
        com = request.FILES.get('fileInput4')

        # Check if any file is selected
        if not any([billet, fact, aux, com]):
            # Redirect to the same page or return an appropriate response
            return render(request, 'index.html')

        billet_file = pd.read_excel(billet)
        fact_file = pd.read_excel(fact)
        aux_file = pd.read_excel(aux)
        com_file = pd.read_excel(com)
        
        # this function returns the created excel files 
        journal17_workbook,rapprochement_workbook = create_journal_17(billet_file, fact_file,aux_file, com_file)

        # Save the journal17 workbook content to a BytesIO object
        excel_data = BytesIO()
        journal17_workbook.save(excel_data)
        # was excel_content 
        excel_data.seek(0)

        # Save the rapprochement workbook content to a BytesIO object
        rap_data = BytesIO()
        rapprochement_workbook.save(rap_data)
        # was excel_content 
        rap_data.seek(0)

        # Save the journal 17 Excel file on the server
        file_path = os.path.join(settings.MEDIA_ROOT, 'journal17.xlsx')
        with open(file_path, 'wb') as file:
            file.write(excel_data.getvalue())

        # Save the rapprochement Excel file on the server
        rap_path = os.path.join(settings.MEDIA_ROOT, 'rapprochement.xlsx')
        with open(rap_path, 'wb') as file:
            file.write(rap_data.getvalue())


        file1_link ='/download-excel/'  
        file2_link = '/download-rap/'
        context = {'file1_link': file1_link, 'file2_link':file2_link}

        return render(request, 'index.html', context)
    return render(request, 'index.html') 

# change 
def add_tab_aux(request): 
    
     if request.method == 'POST':
        # intialize a form with the data submitted in the request 
        form = TabAuxForm(request.POST)
        # if the form data is valid we save the data in the databse 
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
        else:
            pass
     # when the user first loads the form page   
     else:
        # this creates an emty form instance 
        form = TabAuxForm()
     # we pass the emty form instance to the html template, now the template is available for redering 
     return render(request, 'form.html', {'form': form})

def tab_aux_success(request): 
    return render(request, 'success.html')
       
# Display a list of the tab_aux 
def tab_aux_list(request):
    tab_aux_instances = Tab_aux.objects.all()
    return render(request, 'list.html', {'tab_aux_instances': tab_aux_instances})

def tab_aux_delete(request, pk):
   instance = get_object_or_404 (Tab_aux, pk=pk)
   if request.method == 'POST':
       instance.delete()
       return redirect('tab_aux_list')
   
def tab_aux_edit(request, pk):
    instance = get_object_or_404(Tab_aux, pk=pk)
    if request.method == 'POST':
        form = TabAuxForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('tab_aux_list')
        else: 
            pass
    else:
        form = TabAuxForm(instance=instance)
    return render(request,'edit.html',{'form':form})        

def index(request): 
    return render(request, 'index.html')

def listAffilie(request): 
    return render(request, 'listAffilie.html')

def listNts(request): 
    tab_aux_instances = Tab_aux.objects.all()
    return render(request, 'listNts.html', {'tab_aux_instances': tab_aux_instances})
  

def listBanque(request): 
    return render(request, 'listBanque.html')

def listCoffre(request): 
    return render(request, 'listCoffre.html')

def addAffilie(request): 
    return render(request, 'addAffilie.html')

def addNts(request): 
    if request.method == 'POST':
        form = TabAuxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listNts') 
        else:
            pass 
    else:
        form = TabAuxForm()
    return render(request, 'addNts.html', {'form': form})

def deleteNts (request, pk):
       instance = get_object_or_404 (Tab_aux, pk=pk)
       if request.method == 'POST':
        instance.delete()
       return redirect('listNts')

def editNts(request, pk):
    instance = get_object_or_404(Tab_aux, pk=pk)
    if request.method == 'POST':
        form = TabAuxForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listNts')
        else: 
            pass
    else:
        form = TabAuxForm(instance=instance)
    return render(request,'editNts.html',{'form':form}) 

    
def submitCbl(request):

    if request.method == 'POST':
        billet = request.FILES.get('fileInput1')
        fact = request.FILES.get('fileInput2')

        # Check if any file is selected
        if not any([billet, fact]):
            # Redirect to the same page or return an appropriate response
            return render(request, 'cbl.html')

        billet_file = pd.read_excel(billet)
        fact_file = pd.read_excel(fact)
 
        # this function returns the created excel files 
        #journal17_workbook,rapprochement_workbook = create_journal_17(billet_file, fact_file)
        # create an empty excel file 
        journal17_workbook = openpyxl.Workbook()
        rapprochement_workbook = openpyxl.Workbook()
        # Save the journal17 workbook content to a BytesIO object
        excel_data = BytesIO()
        journal17_workbook.save(excel_data)
        # was excel_content 
        excel_data.seek(0)

        # Save the rapprochement workbook content to a BytesIO object
        rap_data = BytesIO()
        rapprochement_workbook.save(rap_data)
        # was excel_content 
        rap_data.seek(0)

        # Save the journal 17 Excel file on the server
        file_path = os.path.join(settings.MEDIA_ROOT, 'journal17.xlsx')
        with open(file_path, 'wb') as file:
            file.write(excel_data.getvalue())

        # Save the rapprochement Excel file on the server
        rap_path = os.path.join(settings.MEDIA_ROOT, 'rapprochement.xlsx')
        with open(rap_path, 'wb') as file:
            file.write(rap_data.getvalue())


        file1_link ='/download-excel/'  
        file2_link = '/download-rap/'
        context = {'file1_link': file1_link, 'file2_link':file2_link}

        return render(request, 'cbl.html', context)
    return render(request, 'cbl.html')    
    


def addCoffre(request): 
    return render(request, 'addCoffre.html')

def addBanque(request): 
    return render(request, 'addBanque.html')

def cbl(request): 
    return render(request, 'cbl.html')

def banque(request): 
    return render(request, 'banque.html')

def coffre(request): 
    return render(request, 'coffre.html')


