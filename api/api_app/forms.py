from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Textarea, DateField, TextInput, PasswordInput

class HouseForm(ModelForm):
    # city = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label=None)
    # facility_sauna = forms.CheckboxInput()
    class Meta:
        model = Houses
        fields = ('name', 'desc', 'city','guests_amount', 'beds_amount', 'address', 'rules', 'bathrooms_amount')

class AuthForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {'username': 'Имя пользователя', 'password': 'Пароль'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'auth_input font_18 center'
        self.fields['password'].widget.attrs['type'] = 'password'
            # self.fields[field].label = ''

class RegForm(ModelForm):
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), to_field_name='name', empty_label=None)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'city',  'sex', 'type', 'photo',)
        widgets = {
            'password': PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'auth_input font_18 center'
        self.fields['password'].widget.attrs['type'] = 'password'
        self.fields['sex'].initial = 'm'
        self.fields['type'].initial = 'guest'
        self.fields['photo'].widget.attrs['style'] = 'display: none;'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        # user.city = Cities.objects.get(pk=self.cleaned_data['city'])
        if commit:
            user.save()
        return user

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonials
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = ''
        self.fields['text'].widget = Textarea(attrs={
            'rows': 3,
            'class': 'black font_18 testimon_textfield w-100',
            'placeholder': 'Добавить отзыв'
        })
        self.fields['text'].label = ''


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ('date_from', 'date_till', 'guests_amount')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_from'].widget = TextInput(attrs={'class': 'date_from'})
        self.fields['date_till'].widget = TextInput(attrs={'class': 'date_till'})
        self.fields['date_till'].label = ''
        self.fields['date_from'].label = ''
        self.fields['guests_amount'].widget.attrs['class'] = 'black bold font_20 center'
        self.fields['guests_amount'].widget.attrs['style'] = 'width: 180px;text-align: center; height: 45px;margin-right: 20px;'
        self.fields['guests_amount'].widget.attrs['placeholder'] = 'Кол-во гостей'
        self.fields['guests_amount'].label = ''
        self.fields['guests_amount'].widget.attrs['min'] = 1


# class MessageForm(ModelForm):
#     class Meta:
#         model = Messages
#         fields = ('message', )
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['message'].widget = Textarea(attrs={
#             'rows': 2,
#             'class': 'black font_18',
#             'placeholder': 'Сообщение'
#         })