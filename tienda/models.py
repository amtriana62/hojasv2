from django.db import models

# Create your models here.
#capturar toda la estructura de la tabla hoja
class Hoja(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo:') #verbose mostrar el titulo del campo
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='Imagen:', null=True)
    descripcion=models.TextField(verbose_name='Descripción:', null=True) #true obligatorio
    precio=models.PositiveIntegerField(verbose_name='Precio:', default=0, null=True)


    def __str__(self):
        fila = "Titulo:" + self.titulo + " - " + "Descripción:" + self.descripcion + " - " + "Precio:" + format(str(self.precio))
        return fila

#el problema era la identación, deben estar dentro de la clase hoja
#toco instalar pip install django-cleanup y en setting-app django-cleanup
#https://es.stackoverflow.com/questions/242326/como-eliminar-im%C3%A1genes-almacenadas-en-media-usando-deleteview-en-django
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super(Hoja, self).delete()

 
class Compra(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre cliente:')
    tipo=models.PositiveBigIntegerField(verbose_name='Tipo cliente:',default=1,null=True)
    cantidad=models.PositiveIntegerField(verbose_name='Cantidad hojas:',default=1,null=True)
    precio=models.PositiveIntegerField(verbose_name='Precio hoja:',null=True)
    subtotal=models.PositiveIntegerField(verbose_name='Subtotal:',null=True)
    neto:models.PositiveIntegerField(verbose_name='Neto a pagar:',null=True)

""" 
    def calcular_total(nombre, tipo, cantidad, precio):
        descuentos = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}
        if tipo in descuentos:
            descuento = descuentos[tipo]
        else:
            descuento = 0.0
    
    subtotal = cantidad * precio
    neto_por_pagar = subtotal * (1 - descuento)
    
    imprimir_recibo(nombre, subtotal, neto_por_pagar)

    def imprimir_recibo(nombre, subtotal, neto_por_pagar):
        print("Nombre del cliente:", nombre)
        print("Subtotal por pagar:", subtotal)
        print("Neto por pagar:", neto_por_pagar)
"""