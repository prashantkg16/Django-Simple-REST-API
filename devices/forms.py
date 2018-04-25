from django import forms
from .models import router

class routerForm(forms.ModelForm):
    class Meta:
        model = router
        fields = ('sapid','hostname', 'loopback','macaddress')