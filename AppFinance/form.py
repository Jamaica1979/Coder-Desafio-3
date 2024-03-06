from django import forms

class form_ingreso (forms.Form):

   fecha= forms.DateField()
   importe= forms.IntegerField()
   categoria = forms.CharField(max_length=60)
   descripcion= forms.CharField(max_length=60)

class form_egreso (forms.Form):

   fecha= forms.DateField()
   importe= forms.IntegerField()
   categoria = forms.CharField(max_length=60)
   descripcion= forms.CharField(max_length=60)
