from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, label='Количество')

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Количество должно быть больше 0.")
        return quantity
