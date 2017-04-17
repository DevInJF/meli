from django import forms
from .models import MeliAccount
from django.contrib.auth.models import User
from django.forms import ModelChoiceField




class CopyForm(forms.Form):
    
    def __init__(self,*args,**kwargs):
        logged_user = kwargs.pop('logged_user')
        #self.copy_from = forms.ModelChoiceField(queryset = User.objects.filter(meli_accounts__id = logged_user.id))
        super(CopyForm,self).__init__(*args,**kwargs)
        meli_accs = MeliAccount.objects.filter(owner = logged_user.id)
        self.fields['copy_from'].queryset = meli_accs
        self.fields['copy_to'].queryset = meli_accs
        
    copy_from =  forms.ModelChoiceField(queryset = None, empty_label="--", label="Copiar de",required=True)
    copy_to =  forms.ModelChoiceField(queryset = None, empty_label="--", label="Copiar para",required=True)
    
    def is_valid(self):
 
        # run the parent validation first
        valid = super(CopyForm, self).is_valid()
 
        # we're done now if not valid
        if not valid:
            return valid
 
        # so far so good, get this user based on the username or email
        if self.cleaned_data['copy_from'].id == self.cleaned_data['copy_to'].id:
            self.add_error('','Não é possível copiar para a mesma conta')
            return False
        else:
            return True