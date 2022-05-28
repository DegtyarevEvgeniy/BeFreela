from django import forms
from django.forms import ModelChoiceField

from django.forms import ModelForm, TextInput, Textarea, Select, CharField
from .models import *
from taggit.models import Tag

COUNTRY_CHOICE = [
    ('Afghanistan','Afghanistan'),
    ('Åland Islands','Åland Islands'),
    ('Albania','Albania'),
    ('Algeria','Algeria'),
    ('American Samoa','American Samoa'),
    ('Andorra','Andorra'),
    ('Angola','Angola'),
    ('Anguilla','Anguilla'),
    ('Antarctica','Antarctica'),
    ('Antigua and Barbuda','Antigua and Barbuda'),
    ('Argentina','Argentina'),
    ('Armenia','Armenia'),
    ('Aruba','Aruba'),
    ('Australia','Australia'),
    ('Austria','Austria'),
    ('Azerbaijan','Azerbaijan'),
    ('Bahamas','Bahamas'),
    ('Bahrain','Bahrain'),
    ('Bangladesh','Bangladesh'),
    ('Barbados','Barbados'),
    ('Belarus','Belarus'),
    ('Belgium','Belgium'),
    ('Belize','Belize'),
    ('Benin','Benin'),
    ('Bermuda','Bermuda'),
    ('Bhutan','Bhutan'),
    ('Bolivia','Bolivia'),
    ('Bosnia and Herzegovina','Bosnia and Herzegovina'),
    ('Botswana','Botswana'),
    ('Bouvet Island','Bouvet Island'),
    ('Brazil','Brazil'),
    ('British Indian Ocean Territory','British Indian Ocean Territory'),
    ('Brunei Darussalam','Brunei Darussalam'),
    ('Bulgaria','Bulgaria'),
    ('Burkina Faso','Burkina Faso'),
    ('Burundi','Burundi'),
    ('Cambodia','Cambodia'),
    ('Cameroon','Cameroon'),
    ('Canada','Canada'),
    ('Cape Verde','Cape Verde'),
    ('Cayman Islands','Cayman Islands'),
    ('Central African Republic','Central African Republic'),
    ('Chad','Chad'),
    ('Chile','Chile'),
    ('China" selected>China','China" selected>China'),
    ('Christmas Island','Christmas Island'),
    ('Cocos (Keeling) Islands','Cocos (Keeling) Islands'),
    ('Colombia','Colombia'),
    ('Comoros','Comoros'),
    ('Congo','Congo'),
    ('Congo, The Democratic Republic','Congo, The Democratic Republic'),
    ('of The','of The'),
    ('Cook Islands','Cook Islands'),
    ('Costa Rica','Costa Rica'),
    ("Cote D'ivoire","Cote D'ivoire"),
    ('Croatia','Croatia'),
    ('Cuba','Cuba'),
    ('Cyprus','Cyprus'),
    ('Czech Republic','Czech Republic'),
    ('Denmark','Denmark'),
    ('Djibouti','Djibouti'),
    ('Dominica','Dominica'),
    ('Dominican Republic','Dominican Republic'),
    ('Ecuador','Ecuador'),
    ('Egypt','Egypt'),
    ('El Salvador','El Salvador'),
    ('Equatorial Guinea','Equatorial Guinea'),
    ('Eritrea','Eritrea'),
    ('Estonia','Estonia'),
    ('Ethiopia','Ethiopia'),
    ('Falkland Islands (Malvinas)','Falkland Islands (Malvinas)'),
    ('Faroe Islands','Faroe Islands'),
    ('Fiji','Fiji'),
    ('Finland','Finland'),
    ('France','France'),
    ('French Guiana','French Guiana'),
    ('French Polynesia','French Polynesia'),
    ('French Southern Territories','French Southern Territories'),
    ('Gabon','Gabon'),
    ('Gambia','Gambia'),
    ('Georgia','Georgia'),
    ('Germany','Germany'),
    ('Ghana','Ghana'),
    ('Gibraltar','Gibraltar'),
    ('Greece','Greece'),
    ('Greenland','Greenland'),
    ('Grenada','Grenada'),
    ('Guadeloupe','Guadeloupe'),
    ('Guam','Guam'),
    ('Guatemala','Guatemala'),
    ('Guernsey','Guernsey'),
    ('Guinea','Guinea'),
    ('Guinea-bissau','Guinea-bissau'),
    ('Guyana','Guyana'),
    ('Haiti','Haiti'),
    ('Heard Island and Mcdonald Islands','Heard Island and Mcdonald Islands'),
    ('Holy See (Vatican City State)','Holy See (Vatican City State)'),
    ('Honduras','Honduras'),
    ('Hong Kong','Hong Kong'),
    ('Hungary','Hungary'),
    ('Iceland','Iceland'),
    ('India','India'),
    ('Indonesia','Indonesia'),
    ('Iran, Islamic Republic of','Iran, Islamic Republic of'),
    ('Iraq','Iraq'),
    ('Ireland','Ireland'),
    ('Isle of Man','Isle of Man'),
    ('Israel','Israel'),
    ('Italy','Italy'),
    ('Jamaica','Jamaica'),
    ('Japan','Japan'),
    ('Jersey','Jersey'),
    ('Jordan','Jordan'),
    ('Kazakhstan','Kazakhstan'),
    ('Kenya','Kenya'),
    ('Kiribati','Kiribati'),
    ("Korea, Democratic People's","Korea, Democratic People's"),
    ('Republic of','Republic of'),
    ('Korea, Republic of','Korea, Republic of'),
    ('Kuwait','Kuwait'),
    ('Kyrgyzstan','Kyrgyzstan'),
    ("Lao People's Democratic Republic","Lao People's Democratic Republic"),
    ('Latvia','Latvia'),
    ('Lebanon','Lebanon'),
    ('Lesotho','Lesotho'),
    ('Liberia','Liberia'),
    ('Libyan Arab Jamahiriya','Libyan Arab Jamahiriya'),
    ('Liechtenstein','Liechtenstein'),
    ('Lithuania','Lithuania'),
    ('Luxembourg','Luxembourg'),
    ('Macao','Macao'),
    ('Macedonia, The Former','Macedonia, The Former'),
    ('Yugoslav Republic of','Yugoslav Republic of'),
    ('Madagascar','Madagascar'),
    ('Malawi','Malawi'),
    ('Malaysia','Malaysia'),
    ('Maldives','Maldives'),
    ('Mali','Mali'),
    ('Malta','Malta'),
    ('Marshall Islands','Marshall Islands'),
    ('Martinique','Martinique'),
    ('Mauritania','Mauritania'),
    ('Mauritius','Mauritius'),
    ('Mayotte','Mayotte'),
    ('Mexico','Mexico'),
    ('Micronesia, Federated States of','Micronesia, Federated States of'),
    ('Moldova, Republic of','Moldova, Republic of'),
    ('Monaco','Monaco'),
    ('Mongolia','Mongolia'),
    ('Montenegro','Montenegro'),
    ('Montserrat','Montserrat'),
    ('Morocco','Morocco'),
    ('Mozambique','Mozambique'),
    ('Myanmar','Myanmar'),
    ('Namibia','Namibia'),
    ('Nauru','Nauru'),
    ('Nepal','Nepal'),
    ('Netherlands','Netherlands'),
    ('Netherlands Antilles','Netherlands Antilles'),
    ('New Caledonia','New Caledonia'),
    ('New Zealand','New Zealand'),
    ('Nicaragua','Nicaragua'),
    ('Niger','Niger'),
    ('Nigeria','Nigeria'),
    ('Niue','Niue'),
    ('Norfolk Island','Norfolk Island'),
    ('Northern Mariana Islands','Northern Mariana Islands'),
    ('Norway','Norway'),
    ('Oman','Oman'),
    ('Pakistan','Pakistan'),
    ('Palau','Palau'),
    ('Palestinian Territory, Occupied','Palestinian Territory, Occupied'),
    ('Panama','Panama'),
    ('Papua New Guinea','Papua New Guinea'),
    ('Paraguay','Paraguay'),
    ('Peru','Peru'),
    ('Philippines','Philippines'),
    ('Pitcairn','Pitcairn'),
    ('Poland','Poland'),
    ('Portugal','Portugal'),
    ('Puerto Rico','Puerto Rico'),
    ('Qatar','Qatar'),
    ('Reunion','Reunion'),
    ('Romania','Romania'),
    ('Russian Federation','Russian Federation'),
    ('Rwanda','Rwanda'),
    ('Saint Helena','Saint Helena'),
    ('Saint Kitts and Nevis','Saint Kitts and Nevis'),
    ('Saint Lucia','Saint Lucia'),
    ('Saint Pierre and Miquelon','Saint Pierre and Miquelon'),
    ('Saint Vincent and The Grenadines','Saint Vincent and The Grenadines'),
    ('Samoa','Samoa'),
    ('San Marino','San Marino'),
    ('Sao Tome and Principe','Sao Tome and Principe'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Senegal','Senegal'),
    ('Serbia','Serbia'),
    ('Seychelles','Seychelles'),
    ('Sierra Leone','Sierra Leone'),
    ('Singapore','Singapore'),
    ('Slovakia','Slovakia'),
    ('Slovenia','Slovenia'),
    ('Solomon Islands','Solomon Islands'),
    ('Somalia','Somalia'),
    ('South Africa','South Africa'),
    ('South Georgia and The','South Georgia and The'),
    ('South Sandwich Islands','South Sandwich Islands'),
    ('Spain','Spain'),
    ('Sri Lanka','Sri Lanka'),
    ('Sudan','Sudan'),
    ('Suriname','Suriname'),
    ('Svalbard and Jan Mayen','Svalbard and Jan Mayen'),
    ('Swaziland','Swaziland'),
    ('Sweden','Sweden'),
    ('Switzerland','Switzerland'),
    ('Syrian Arab Republic','Syrian Arab Republic'),
    ('Taiwan','Taiwan'),
    ('Tajikistan','Tajikistan'),
    ('Tanzania, United Republic of','Tanzania, United Republic of'),
    ('Thailand','Thailand'),
    ('Timor-leste','Timor-leste'),
    ('Togo','Togo'),
    ('Tokelau','Tokelau'),
    ('Tonga','Tonga'),
    ('Trinidad and Tobago','Trinidad and Tobago'),
    ('Tunisia','Tunisia'),
    ('Turkey','Turkey'),
    ('Turkmenistan','Turkmenistan'),
    ('Turks and Caicos Islands','Turks and Caicos Islands'),
    ('Tuvalu','Tuvalu'),
    ('Uganda','Uganda'),
    ('Ukraine','Ukraine'),
    ('United Arab Emirates','United Arab Emirates'),
    ('United Kingdom','United Kingdom'),
    ('United States','United States'),
    ('United States Minor Outlying','United States Minor Outlying'),
    ('Islands','Islands'),
    ('Uruguay','Uruguay'),
    ('Uzbekistan','Uzbekistan'),
    ('Vanuatu','Vanuatu'),
    ('Venezuela','Venezuela'),
    ('Viet Nam','Viet Nam'),
    ('Virgin Islands, British','Virgin Islands, British'),
    ('Virgin Islands, U.S.','Virgin Islands, U.S.'),
    ('Wallis and Futuna','Wallis and Futuna'),
    ('Western Sahara','Western Sahara'),
    ('Yemen','Yemen'),
    ('Zambia','Zambia'),
    ('Zimbabwe','Zimbabwe'),
]

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product_creator
        fields = '__all__'
        widgets = {
            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "name",
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'priceInput',
                'onchange': 'recalc(this)',
            }),
            'country': Select(attrs={
                'class': 'input-group mt-2 mb-2',
            }, choices=COUNTRY_CHOICE),

            'brand': TextInput(attrs={
                'class': 'form-control',
                'id': 'brand',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
            }),
            'width_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'height_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'length_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'width_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'height_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'length_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),

        }

    # product_name = forms.CharField(required=True)
    # cost = forms.CharField(required=True)
    # availability = forms.ChoiceField()
    # description = forms.CharField()
    # picture = forms.ImageField()



class MyProfile(forms.Form):
    select = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label=None
    )


class addTasks(forms.Form):
    task_name = forms.CharField(label='Название', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название',
        'id': "floatingInputGrid",
    }))

    select = forms.ModelChoiceField(queryset=Tag.objects.all(), widget =forms.Select(attrs = {
        'class': "form-select",
    }))


    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Описание',
        'style': "height: 100px",
        'id': "floatingTextarea2",

    }))
    price = forms.IntegerField(label='Цена', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))


class Resume(forms.Form):
    description = forms.CharField(label='Расскажите о себе', required=True, widget=forms.Textarea(attrs={
        'class': "form-control",
    }))
    is_company = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'onchange': "isCompany()",
        'id': "isCompanyTrigger",
    }))
    company_name = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Название компании",

    }))
    email = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
    }))
    first_name = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
        'value': "TROLOLO"
    }))
    cover = forms.ImageField(required=False)
    telegram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "@tag",
    }))
    vk = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "https://vk.com/yourid",
    }))
    whatsapp = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "+71234567890",
    }))
    instagram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': " https://instagram.com/tag",
    }))
    tag = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
    }))
    published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'value': "1",
    }))