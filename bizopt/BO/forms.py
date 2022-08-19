from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account


from django.forms import ModelForm, TextInput, Textarea, Select, CharField


from .models import *
from taggit.models import Tag

COUNTRY_CHOICE = [
    ('Afghanistan', 'Afghanistan'),
    ('Åland Islands', 'Åland Islands'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('American Samoa', 'American Samoa'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Anguilla', 'Anguilla'),
    ('Antarctica', 'Antarctica'),
    ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Aruba', 'Aruba'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas', 'Bahamas'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermuda', 'Bermuda'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Bouvet Island', 'Bouvet Island'),
    ('Brazil', 'Brazil'),
    ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
    ('Brunei Darussalam', 'Brunei Darussalam'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Cape Verde', 'Cape Verde'),
    ('Cayman Islands', 'Cayman Islands'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Christmas Island', 'Christmas Island'),
    ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo', 'Congo'),
    ('The Democratic Republic of The Cook Islands', 'The Democratic Republic of The Cook Islands'),
    ('Costa Rica', 'Costa Rica'),
    ("Cote D'ivoire", "Cote D'ivoire"),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Ethiopia', 'Ethiopia'),
    ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
    ('Faroe Islands', 'Faroe Islands'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('French Guiana', 'French Guiana'),
    ('French Polynesia', 'French Polynesia'),
    ('French Southern Territories', 'French Southern Territories'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Gibraltar', 'Gibraltar'),
    ('Greece', 'Greece'),
    ('Greenland', 'Greenland'),
    ('Grenada', 'Grenada'),
    ('Guadeloupe', 'Guadeloupe'),
    ('Guam', 'Guam'),
    ('Guatemala', 'Guatemala'),
    ('Guernsey', 'Guernsey'),
    ('Guinea', 'Guinea'),
    ('Guinea-bissau', 'Guinea-bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Heard Island and Mcdonald Islands', 'Heard Island and Mcdonald Islands'),
    ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
    ('Honduras', 'Honduras'),
    ('Hong Kong', 'Hong Kong'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Islamic Republic of', 'Islamic Republic of'),
    ('Iraq', 'Iraq'),
    ('Ireland', 'Ireland'),
    ('Isle of Man', 'Isle of Man'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jersey', 'Jersey'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ("Korea", "Korea"),
    ("Democratic People's Republic of Korea", "Democratic People's Republic of Korea"),
    ('Republic of Kuwait', 'Republic of Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ("Lao People's Democratic Republic", "Lao People's Democratic Republic"),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Macao', 'Macao'),
    ('Macedonia, The Former', 'Macedonia, The Former'),
    ('Yugoslav Republic of Madagascar', 'Yugoslav Republic of Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Martinique', 'Martinique'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mayotte', 'Mayotte'),
    ('Mexico', 'Mexico'),
    ('Micronesia, Federated States of Moldova', 'Micronesia, Federated States of Moldova'),
    (' Republic of Monaco', ' Republic of Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Montserrat', 'Montserrat'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar', 'Myanmar'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('Netherlands Antilles', 'Netherlands Antilles'),
    ('New Caledonia', 'New Caledonia'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('Niue', 'Niue'),
    ('Norfolk Island', 'Norfolk Island'),
    ('Northern Mariana Islands', 'Northern Mariana Islands'),
    ('Norway', 'Norway'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palau', 'Palau'),
    ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Pitcairn', 'Pitcairn'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Puerto Rico', 'Puerto Rico'),
    ('Qatar', 'Qatar'),
    ('Reunion', 'Reunion'),
    ('Romania', 'Romania'),
    ('Russian Federation', 'Russian Federation'),
    ('Rwanda', 'Rwanda'),
    ('Saint Helena', 'Saint Helena'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
    ('Saint Vincent and The Grenadines', 'Saint Vincent and The Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Georgia and The South Sandwich Islands', 'South Georgia and The South Sandwich Islands'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
    ('Swaziland', 'Swaziland'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syrian Arab Republic', 'Syrian Arab Republic'),
    ('Taiwan', 'Taiwan'),
    ('Tajikistan', 'Tajikistan'),
    ('Tanzania, United Republic of Thailand', 'Tanzania, United Republic of Thailand'),
    ('Timor-leste', 'Timor-leste'),
    ('Togo', 'Togo'),
    ('Tokelau', 'Tokelau'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('United States', 'United States'),
    ('United States Minor Outlying', 'United States Minor Outlying'),
    ('Islands', 'Islands'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Venezuela', 'Venezuela'),
    ('Viet Nam', 'Viet Nam'),
    ('Virgin Islands, British', 'Virgin Islands, British'),
    ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
    ('Wallis and Futuna', 'Wallis and Futuna'),
    ('Western Sahara', 'Western Sahara'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
]
CATEGORY_CHOICE = [
    ('Дизайнерская одежда', 'Дизайнерская одежда'),
    ('Дизайнерская обувь', 'Дизайнерская обувь'),
    ('Сумки', 'Сумки'),
    ('Интерьер', 'Интерьер'),
    ('Украшения', 'Украшения'),
    ('Скульптуры', 'Скульптуры'),
    ('Подушки', 'Подушки'),
]

DURATION_CHOICE = [
    ('1 - 2 дня', '1 - 2 дня'),
    ('2 - 5 дней', '2 - 5 дней'),
    ('5 - 7 дней', '5 - 7 дней'),
    ('1 - 2 недели', '1 - 2 недели'),
    ('2 недели - месяц', '2 недели - месяц'),
    ('1 - 3 месяца', '1 - 3 месяца'),
    ('3 - 6 месяцев', '3 - 6 месяцев'),
    ('6 - 12 месяцев', '6 - 12 месяцев'),
    ('1 - 2 года', '1 - 2 года'),
    ('более 3-х лет', 'более 3-х лет'),
]
User = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded',
            'required': '',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': '',
            'minlength': '8'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded pswdChecker',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': '',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded pswdChecker',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': '',
            'minlength': '8'
        })

    first_name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product_creator
        fields = '__all__'
        widgets = {
            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название товара",
                'oninput': 'PassChecker(1)',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'priceInput',
                'oninput': 'recalc(this)',
                'placeholder': 'Введите стоимость товара'
            }),
            'country': Select(attrs={
                'class': 'input-group mt-2 mb-2',
            }, choices=COUNTRY_CHOICE),
            # 'subcategory': TextInput(attrs={
            #     'class': 'form-control',
            #     'oninput': 'PassChecker(1)',
            #     'placeholder': 'Пример: носки'
            # }),
            'brand': TextInput(attrs={
                'class': 'form-control',
                'id': 'brand',
                'oninput': 'PassChecker(1)',
                'placeholder': 'Введите бренд товара'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание товара',
                'oninput': 'PassChecker(3)',
            }),
            'category': Select(attrs={
                'class': 'input-group mt-2 mb-2',
            }, choices=CATEGORY_CHOICE),
            'duration': Select(attrs={
                'class': 'input-group mt-2 mb-2',
            }, choices=DURATION_CHOICE),
            'width_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'oninput': 'PassChecker(3)',
            }),
            'height_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'oninput': 'PassChecker(3)',
            }),
            'length_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'oninput': 'PassChecker(3)',
            }),
            'width_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'oninput': 'PassChecker(3)',
            }),
            'height_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'oninput': 'PassChecker(3)',
            }),
            'length_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'oninput': 'PassChecker(3)',
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

    select = forms.ModelChoiceField(queryset=Tag.objects.all(), widget=forms.Select(attrs={
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
        'class': "uk-input uk-width-1-3",
        'value': "",
    }))
    is_company = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'onchange': "isCompany()",
        'id': "isCompanyTrigger",
    }))
    company_name = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "Название компании",

    }))
    email = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
    }))
    first_name = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'value': "TROLOLO"
    }))
    cover = forms.ImageField(required=False)
    telegram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "@tag",
    }))
    vk = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "https://vk.com/yourid",
    }))
    whatsapp = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "+71234567890",
    }))
    instagram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': " https://instagram.com/tag",
    }))
    tag = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
    }))
    published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'value': "1",
    }))


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = Account
        fields = ('email', 'city', 'first_name', 'last_name', 'email',
        'ogrn', 'inn', 'kpp', 'street', 'fiz_adress', 'index', 'checking_account', 'bik', 
        'korr_check','name_small','nameFull', 'payment_account', 'reg_form')
