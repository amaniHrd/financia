
from audioop import reverse
import os
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import openpyxl
import pandas as pd
from io import BytesIO
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




       




