from django.forms import ModelForm
from main.models import Menutoko

class MenutokoForm(ModelForm):
    class Meta:
        model = Menutoko
        fields = ["name", "price", "description"]