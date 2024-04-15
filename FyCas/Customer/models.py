from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, )#Nombre
    last_name = models.CharField(max_length=255)#Apellido
    number = models.CharField(max_length=20, blank=True)#Numero local o Movile
    address = models.CharField(max_length=255)#Direccion de donde recide
    email = models.EmailField(null=True)#Correo electronico
    amount_purpose = models.TextField(max_length=355)#Proposito por el que se solicita el prestamo
    work_information = models.TextField(max_length=300)#Informacion donde trabaja
    references_peopple = models.TextField(max_length=500)#Personas referentes
    dni = models.CharField(max_length=100) #Numero de Identidad
    amount = models.IntegerField(null=True)#Monto 
    no_account = models.IntegerField(default=0) #Numero de Cuentaloooo
    img1 = models.ImageField(upload_to="media/",  blank=True, null=True, default="media/img-default/img.png")#Foto de Cedula delantera
    img2 = models.ImageField(upload_to="media/", blank=True, null=True, default="media/img-default/img.png")#Foto de Cedula tracera
    name_r1 = models.CharField(max_length=255,  )#Nombre
    name_r2 = models.CharField(max_length=255,  )#Nombre
    number_r1 = models.CharField(default="", max_length=30)#Numero local o Movile
    number_r2 = models.CharField(default="", max_length=30  )#Numero local o Movile
    
    # CaptureLocation
    lat = models.CharField(max_length=100000000050005, default='')
    lon = models.CharField(max_length=100000000000000055, default='')
    
    # Tipo de Entrada
    type_input = models.CharField(max_length=2, default='P')
    #Sexo
    sexo = models.CharField(max_length=2, default='')
    # Estado Civil 
    estado_civil = models.CharField(max_length=2, default='')
    # Ocupacion 
    ocupacion = models.CharField(max_length=25, default='Estudiante')
    # Codigo de cliente
    code_customer = models.CharField(max_length=122000, default='')
    # Date 
    nacimiento = models.CharField(max_length=40, default='10/11/2001')
    # Nacionalidad 
    nacionalidad = models.CharField(max_length=25, default='DOMINICANA')
    # Direccion
    direccion = models.CharField(max_length=255, default='')
    # Sector
    sector = models.CharField(max_length=455, default='')
    # Calle/Numero
    calle_numero = models.CharField(max_length=255, default='')
    # municipio
    municipio = models.CharField(max_length=255, default='')
    # Cuidad 
    ciudad = models.CharField(max_length=250, default='Santo Domingo Este')
    # provincia
    provincia = models.CharField(max_length=255, default='SANTO DOMINGO DE GUZMAN')
    # Pais
    pais = models.CharField(max_length=255, default='REPUBLICA DOMINICANA')
    # dir_referencia
    dir_referencia = models.CharField(max_length=255, default='')
    # Numero de telefono de la empresa
    phone = models.CharField(max_length=18, default='')
    
    # Datos donde labura
    # Empresa donde trabaja  
    empresa_trabaja = models.CharField(max_length=255, default='')
    # Cargo
    cargo = models.CharField(max_length=255, default='')
    # Direccion 
    direccion_trabajo = models.CharField(max_length=255, default='')
    # Sector 
    sector = models.CharField(max_length=244, default='')
    # Calle
    calle_numero_trabajo = models.CharField(max_length=255, default='')
    # Municipio 
    municipio_trabaja = models.CharField(max_length=255, default='')
    # Ciudad 
    ciudad_trabaja = models.CharField(max_length=255, default='')
    # provins
    provincia_trabajo = models.CharField(max_length=255, default='SANTO DOMINGO DE GUZMAN')
    # pais
    pais_trabajo = models.CharField(max_length=244, default='REPUBLICA DOMINICANA')
    # dir_referencia
    dir_referencia_trabajo = models.CharField(max_length=244, default='')
    #Salario de M
    salario_m = models.CharField(max_length=233, default='')
    # Moneda 
    moneda = models.CharField(max_length=3, default='RD$')  
    # Datos de la cuantas 
    # Realcion tipo uno
    relacion_tipo = models.CharField(max_length=233, default='1')
    # Fecha de Apertura
    fecha_apertura = models.CharField(max_length=233, default='')
    # Fecha de Vencimiento
    fecha_vencimiento = models.CharField(max_length=233, default='')
    # Fecha del ultimo pago
    fecha_ultimo_pago = models.CharField(max_length=233, default='')
    # Numero de cuenta 
    numeoro_cuenta = models.CharField(max_length=233, default='')
    # Estatus 
    estatus = models.CharField(max_length=233, default='')
    # Tipo de prestamo
    tipo_prestamo = models.CharField(max_length=233, default='N')
    # Moneda 
    moneda_prestamo = models.CharField(max_length=233, default='RD$')
    # Credito Aprovado 
    credito_aprovado = models.CharField(max_length=233, default='')
    #Balance al Corte
    balance_corte = models.CharField(max_length=233, default='')
    #Monto Adeudado
    monto_adeudado = models.CharField(max_length=233, default='')
    # Pago mandatotio o cuota
    pago_mandatorio_cuota = models.CharField(max_length=233, default='')
    # Monto Ultimo Pago
    monto_ultimo_pago = models.CharField(max_length=233, default='') 
    # Total de Atraso
    total_atraso = models.CharField(max_length=233, default='')
    # Tasa de interes
    tasa_interes = models.CharField(max_length=233, default='0.15')
    # Forma de pago 
    forma_pago = models.CharField(max_length=233, default='Mensual')
    # Cantidad de Cuota
    cantidad_cuota = models.CharField(max_length=233, default='6')
    atraso1_30 = models.CharField(max_length=233, default='')
    atraso31_60 = models.CharField(max_length=233, default='')
    atraso61_90 = models.CharField(max_length=233, default='')
    atraso91_120 = models.CharField(max_length=233, default='')
    atraso121_150 = models.CharField(max_length=233, default='')
    atraso151_180 = models.CharField(max_length=233, default='')
    atraso181_o_mas = models.CharField(max_length=233, default='')


    def __str__(self):
        return self.name


class Credit(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE, related_name="credit")
    amount = models.IntegerField(default=10000)
    name = models.CharField(max_length=100)
    price_feed = models.IntegerField(default=1)
    dni = models.TextField(default="")
    no_account = models.TextField() #Numero de Cuenta
    
    #thow pay for monts
    mode_pay = models.BooleanField(default=False)
    #if mode_pay is True Appli 2 Pay 
    day_pay = models.IntegerField(default=30)
    is_active = models.BooleanField(default=True)#is active rederict at diferens view

    amount_feed = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.name
