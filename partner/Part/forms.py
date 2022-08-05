from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField, ModelForm, TextInput, Textarea, Select, CharField
from .models import *

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

User = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'placeholder': 'Введите название',
            'maxlength': '16',
            'minlength': '6',

        })
        self.fields['ogrn'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'ogrn',
            'id': 'ogrn',
            'type': 'number',
            'placeholder': 'Введите свой ОГРН',
            'maxlength': '13',
            'minlength': '13'
        })
        self.fields['inn'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'inn',
            'id': 'inn',
            'type': 'number',
            'placeholder': 'Введите свой ИНН',
            'maxlength': '13',
            'minlength': '10'
        })
        self.fields['kpp'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'kpp',
            'id': 'kpp',
            'type': 'number',
            'placeholder': 'Введите свой КПП',
            'maxlength': '9',
            'minlength': '9'
        })
        self.fields['street'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'street',
            'id': 'street',
            'type': 'text',
            'placeholder': '162390, Россия, Вологодская область, город Великий Устюг, дом Деда Мороза',
            'maxlength': '100',
            'minlength': '8'
        })
        self.fields['fiz_adress'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'fiz_adress',
            'id': 'fiz_adress',
            'type': 'text',
            'placeholder': 'Мурманская обл., Мончегорск, Лапландский заповедник, пер.Зеленый, д.8',
            'maxlength': '100',
            'minlength': '10'
        })
        self.fields['index'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'index',
            'id': 'index',
            'type': 'number',
            'placeholder': '184506',
            'maxlength': '6',
            'minlength': '6'
        })
        self.fields['checking_account'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'checking_account',
            'id': 'checking_account',
            'type': 'number',
            'placeholder': '',
            'maxlength': '20',
            'minlength': '20'
        })
        self.fields['bik'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'checking_account',
            'id': 'checking_account',
            'type': 'number',
            'placeholder': '',
            'maxlength': '22',
            'minlength': '8'
        })
        self.fields['korr_check'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'korr_check',
            'id': 'korr_check',
            'type': 'number',
            'placeholder': '',
            'maxlength': '20',
            'minlength': '20'
        })

    name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email', 'ogrn', 'inn', 'kpp', 'street', 'fiz_adress', 'index', 'checking_account', 'bik',
                       'korr_check']

    class Meta:
        model = User
        fields = (
            'name', 'email', 'ogrn', 'inn', 'kpp', 'street', 'fiz_adress', 'index', 'checking_account', 'bik', 'korr_check')


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

            'brand': TextInput(attrs={
                'class': 'form-control',
                'id': 'brand',
                'oninput': 'PassChecker(1)',
                'placeholder': 'Введите бренд товара'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание товара'
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
