from django.forms import ModelForm

from .models import Conveyane,Works

class ConveyanceaddForm(ModelForm):
    class Meta:
        model = Conveyane
        fields = ["conveyance_amount","Reason"]

class WorkAddForm(ModelForm):
    class Meta:
        model = Works
        fields = ["workname","WorkDiscription","status"]