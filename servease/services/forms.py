from django import forms 

from .models import Service

INPUT_CLASSES = 'form-control mb-2'

class NewServiceForm(forms.ModelForm):
	class Meta:
		model = Service 
		fields = ('category', 'name', 'description', 'price', 'image',)


		widgets = {
			'category': forms.Select(attrs={
				'class': INPUT_CLASSES
				}),
			'name': forms.TextInput(attrs={
				'class': INPUT_CLASSES
				}),
			'description': forms.Textarea(attrs={
				'class': INPUT_CLASSES
				}),
			# 'price': forms.TextInput(attrs={
			# 	'class': INPUT_CLASSES
			# 	}),
			'image': forms.FileInput(attrs={
				'class': INPUT_CLASSES
				}),
			}


		price = forms.FloatField(
	        widget=forms.NumberInput(attrs={'class': INPUT_CLASSES}),
	    )

class EditServiceForm(forms.ModelForm):
	class Meta:
		model = Service 
		fields = ('name', 'description', 'price', 'image', 'is_sold')
		
		widgets = {
			'name': forms.TextInput(attrs={
				'class': INPUT_CLASSES
				}),
			'description': forms.Textarea(attrs={
				'class': INPUT_CLASSES
				}),
			# 'price': forms.TextInput(attrs={
			# 	'class': INPUT_CLASSES
			# 	}),
			'image': forms.FileInput(attrs={
				'class': INPUT_CLASSES
				}),
			}


		price = forms.FloatField(
	        widget=forms.NumberInput(attrs={'class': INPUT_CLASSES}),
	    )
