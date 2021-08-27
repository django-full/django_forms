from django import forms

class Post(forms.Form):

    #python data type
    inter_ger   = forms.IntegerField(required=False)
    decimal     = forms.DecimalField()
    float       =forms.FloatField()
    bolean      = forms.BooleanField()
    char_field  = forms.CharField(max_length=10)

    #stringIput
    email_field =forms.EmailField()
    slug_field  = forms.SlugField()
    url_field   = forms.URLField
    ip_field    = forms.GenericIPAddressField()


    #selec input
    PILIHAN = (
        ('P','PRIA'),
        ('W','WANITA')
    )
    choice_field            = forms.ChoiceField(choices=PILIHAN)
    multi_choice_field      = forms.MultipleChoiceField(choices=PILIHAN)
    multi_type_choice_field = forms.TypedMultipleChoiceField(choices=PILIHAN)
    null_bolean_field       = forms.NullBooleanField()

    #date_time
    date_field          = forms.DateField()
    datetime_field      = forms.DateTimeField()
    duration_field      = forms.DurationField()
    time_field          = forms.TimeField()
    splitdatetime_field =forms.SplitDateTimeField()
    #fileinput
    file_field = forms.FileField()
    image_field = forms.ImageField()



class Contact(forms.Form):
    Nama_Lengkap = forms.CharField(max_length=20)
    PILIHAN = (
        ('P', 'PRIA'),
        ('W', 'WANITA')
    )
    Gender = forms.ChoiceField(
        choices=PILIHAN,widget=forms.RadioSelect
    )

    Tahun = range(1990,2022,1)
    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(years=Tahun)
    )

    email = forms.EmailField(label='alamat Email')

    Alamat = forms.CharField(max_length=600,
                             widget=forms.Textarea)

    aggre = forms.BooleanField()
