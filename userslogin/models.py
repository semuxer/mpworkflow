from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    fistname = models.CharField(blank=True, max_length=64, default='', help_text='Имя')
    midlname = models.CharField(blank=True, max_length=64, default='', help_text='Отчество')
    lastname = models.CharField(max_length=64, default='', help_text='Фамилия')
    nickname = models.CharField(max_length=64, unique=True, help_text='Логин')
    password = models.CharField(max_length=64, null=True, help_text='Пароль')
    email = models.EmailField(unique=True, help_text='e-mail')
    phone1 = models.CharField(blank=True, max_length=20, default='', help_text='Номер телефона 1: +38 067 123 44 55')
    phone2 = models.CharField(blank=True, max_length=20, default='', help_text='Номер телефона 2: +38 067 123 44 55')
    func = models.CharField(blank=True, max_length=120, default='', help_text='Должность')
    dep = models.ForeignKey('Department', null=True, blank=True, help_text='Департамент')
    active = models.BooleanField(default=False, help_text='Разрешить доступ к системе')

    def __str__(self):
        fn = ""
        mn = ""
        if len(self.fistname)>=1:
            fn = ' '+self.fistname[0]+'.'
        if len(self.midlname)>=1:
            mn = self.midlname[0]+'.'
        return self.lastname+fn+mn

class Department(models.Model):
    name = models.CharField(max_length=256, help_text='Название департамента')
    
    def __str__(self):
        return self.name        

class NewsPaper(models.Model):

    size_choice = (
        ('840',(
            ('A1', 'A1 578x840'),
            ('A2', 'A2 420x578'),
            ('A3', 'A3 289x420'),
            ('A4', 'A4 210x289'),
            ('A5', 'A5 140x420'),
            )
        ),
        ('800',(
            ('A1', 'A1 578x800'),
            ('A2', 'A2 400x578'),
            ('A3', 'A3 289x400'),
            ('A4', 'A4 200x289'),
            ('A5', 'A5 140x400'),
            )
        ),
        ('760',(
            ('B2', 'B2 578x760'),
            ('B3', 'B3 380x578'),
            ('B4', 'B4 289x380'),
            ('B5', 'B5 190x289'),
            ('B6', 'B6 140x380'),
            )
        ),
        ('700',(
            ('B2', 'B2 578x700'),
            ('B3', 'B3 350x578'),
            ('B4', 'B4 289x350'),
            ('B5', 'B5 175x289'),
            ('B6', 'B6 140x350'),
            )
        ),     
    )

    name = models.CharField(default="", max_length=128, help_text='Название газеты')
    number = models.CharField(blank=True, default="", max_length=20, help_text='Номер газеты')
    manager = models.ForeignKey('User', blank=True, help_text='Менеджер')
    pages = models.SmallIntegerField(blank=True, default=0, help_text='Количество страниц')
    size = models.CharField(blank=True, max_length=2,choices=size_choice, default="A3", help_text='Формат газеты')
    copies = models.IntegerField(blank=True, default=0, help_text='Тираж')
    copiesadd = models.IntegerField(blank=True, default=0, help_text='Тираж')
    filedate = models.DateField(blank=True, default=timezone.now, null=True, help_text='Дата прихода файлов')
    filetime = models.TimeField(blank=True, default=timezone.now, null=True, help_text='Время прихода файлов')
    shipmentdate = models.DateField(blank=True, default=timezone.now, null=True, help_text='Дата отгрузки готовой продукции')
    shipmenttime = models.TimeField(blank=True, default=timezone.now, null=True, help_text='Время отгрузки готовой продукции')
    createdatetime = models.DateTimeField(default=timezone.now, help_text='Дата/Время внесения записи о газете')
    pages4color = models.CharField(blank=True, max_length=260, help_text='Список полноцветных страниц (например: 1, 8)')
    pages2color = models.CharField(blank=True, max_length=260, help_text='Список двухцветных страниц (например: 2, 7)')
    pages1color = models.CharField(blank=True, max_length=260, help_text='Список ч/б страниц (например: 3, 4, 5, 6)')
    papermarks = models.ForeignKey('Paper', blank=True,  null=True, help_text='Тип бумаги')
    
    def __str__(self):
        return self.name+" #"+self.number

class Paper(models.Model):
    brand = models.CharField(default="", max_length=64, help_text = 'Марка бумаги')
    width = models.SmallIntegerField(default=84, help_text = 'Ширина роля (см)')
    density = models.SmallIntegerField(default=42, help_text = 'Плотность бумаги (г/м.кв)')

    def __str__(self):
        return self.brand+" "+str(self.width)+'/'+str(self.density)
        

class Acces(models.Model):
    """ 
        appendable — создавать
        visible — видеть
        changeable — изменять
        deleteable — удалять
    """
    target_choice = (
        ('NewsPaper','NewsPaper'),
        )
    user = models.ForeignKey('User', help_text='Пользователь')
    target = models.CharField(max_length=120, choices=target_choice, default='NewsPaper', help_text='Выбор таблицы')
    appendable = models.BooleanField(default=False, help_text='Разрешение на создание записей')
    visible = models.BooleanField(default=True, help_text='Разрешение на просмотр записей')
    changeable = models.BooleanField(default=False, help_text='Разрешение на редактирование записей')
    deleteable = models.BooleanField(default=False, help_text='Разрешение на удаление записей')
    
    def __str__(self):
        out =""
        if self.appendable:
            out = out + "1"
        else:
            out = out + "0"
        if self.visible:
            out = out + "1"
        else:
            out = out + "0"
        if self.changeable:
            out = out + "1"
        else:
            out = out + "0"
        if self.deleteable:
            out = out + "1"
        else:
            out = out + "0"
        return str(self.user) + ' ' + self.target + ' ' + out