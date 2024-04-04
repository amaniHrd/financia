
from django import forms
from .models import Tab_aux


class TabAuxForm(forms.ModelForm): 
    class Meta:
        model = Tab_aux 
        fields = ['code', 'libelle']
        # to add style 
        widgets = {
            'code': forms.TextInput(attrs= {'class': 'form-control'}), 
            'libelle': forms.TextInput(attrs= {'class': 'form-control'}),
            
        }


'''
Using form linked to my model will validate the model field types and constraints 
ensure that the data entered in form meets the requirements of the database
it automatically creates an tab_aux object and save it the databse using form.save()
it handles form submission securely  and protects against common threats like SQL injection 
 
'''

