from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = ['name', 'category', 'price', 'quantity', 'color', 'image']
        widgets = {
            'name':     forms.TextInput(attrs={
                            'placeholder': 'Product Name',
                            'class':       'form-input'
                        }),
            'category': forms.TextInput(attrs={
                            'placeholder': 'Category',
                            'class':       'form-input'
                        }),
            'price':    forms.NumberInput(attrs={
                            'placeholder': 'Price',
                            'class':       'form-input',
                            'min':         '0'
                        }),
            'quantity': forms.NumberInput(attrs={
                            'placeholder': 'Quantity',
                            'class':       'form-input',
                            'min':         '0'
                        }),
            'color':    forms.TextInput(attrs={
                            'placeholder': 'Color',
                            'class':       'form-input'
                        }),
            'image':    forms.FileInput(attrs={
                            'class': 'form-input file-input'
                        }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError('Invalid field')
        return name

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category or not category.strip():
            raise forms.ValidationError('Invalid field')
        return category

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price < 0:
            raise forms.ValidationError('Invalid field')
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity < 0:
            raise forms.ValidationError('Invalid field')
        return quantity

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color or not color.strip():
            raise forms.ValidationError('Invalid field')
        return color

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('Invalid field')
        return image