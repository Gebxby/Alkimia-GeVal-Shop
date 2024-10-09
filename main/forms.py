from django.forms import ModelForm
from main.models import Menutoko
from django.utils.html import strip_tags

class MenutokoForm(ModelForm):
    class Meta:
        model = Menutoko
        fields = ["name", "price", "description"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)
        def celan_description(self):
            description = self.celan_description(description)["description"]
            return strip_tags(description)