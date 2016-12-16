from django import forms

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid url")
    return value

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self, ).clean()
    #     url = cleaned_data['url']
    #     # print url
    #     # return url
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Not valid url")
