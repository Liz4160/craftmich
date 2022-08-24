from django.db import models

# Create your models here.
class Artesania(models.Model): #Define la estructura de nuestra tabla
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField(max_length=20,verbose_name="Nombre") #Texto largo
    descripcion=models.TextField(verbose_name="Descripcion")
    imagen=models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    municipio = models.CharField(max_length=20, verbose_name="Municipio")
    costo=models.FloatField(verbose_name="Costo")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Artesania"
        verbose_name_plural="Artesanias"
        ordering=["-created"] #Este elemento indica que se ordernara del más recienre al ,mas viejo

    def __str__(self):
        return self.nombre #Indica que se mostrare el nombre en la tabla 

class Opinion(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    usuario=models.TextField(verbose_name="Usuario")
    comentario=models.TextField(verbose_name="Comentario")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name="Opinion"
        verbose_name_plural="Opiniones"
        ordering=["-created"]

    def __str__(self):
        return self.comentario