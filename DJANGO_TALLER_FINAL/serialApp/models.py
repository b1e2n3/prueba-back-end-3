from django.db import models

#Para cada Inscrito mínimo se debe considerar, su ID, nombre de la persona, teléfono, 
#fecha inscripción, institución, la hora de inscripción, el estado (RESERVADO, COMPLETADA, 
#ANULADA, NO ASISTEN) y una observación.

class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=50)
    hora_inscripcion = models.TimeField()
    email = models.EmailField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=300)
