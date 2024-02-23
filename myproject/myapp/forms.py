from django import forms
from .models import Author,Book

class SomeForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(),label='Auteur')
    
    class Meta:
        model = Book
        fields = ['title','author','quantity']
        labels = {'title':"Titre",'author':"Auteur",'quantity':"Quantité"}
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        
        if quantity <=0 or quantity > 100:
            raise forms.ValidationError("le quantité doit être supperieur à 1 et inferieur à 100")
        
        return quantity
    
    def clean(self):
        title = self.cleaned_data.get('title')
        quantity = self.cleaned_data.get('quantity')
        
        if title and quantity:
            if title.startswith('Naruto') and quantity < 10:
                raise forms.ValidationError('la quantité du livre "naruto" doit être supperieur à 10')
        return self.cleaned_data