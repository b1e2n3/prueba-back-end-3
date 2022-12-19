from django import forms
from serialApp.models import Inscrito

class FormInscrito(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['id','nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','email','estado','observacion']
    
    def __init__(self, *args, **kwargs):
        super(FormInscrito, self).__init__(*args, **kwargs)
        self.fields['observacion'].required = False