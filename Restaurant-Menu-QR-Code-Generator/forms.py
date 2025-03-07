from django import forms


class QRForm(forms.Form):
    Restaurant_name=forms.CharField(max_length=200, 
                                    label='Restaurant Name',
                                    widget=forms.TextInput({
                                        'class':"form-control",
                                        'placeholder':'Enter Restaurant Name'
                                    })
                                    )
    url=forms.URLField(max_length=200,
                       label='Menu URL',
                       widget=forms.URLInput({
                                        'class':"form-control",
                                        'placeholder':'Enter URL of your online menu'
                                    }))