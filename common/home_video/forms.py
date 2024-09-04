from django import forms

from common.models import HomeVideo


class HomeVideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = HomeVideo
        fields = (
                "name",
                "description", 
                "video",
                )

        widgets = {
                "name": forms.TextInput(
                    attrs={"class": "form-control"}
                    ),
                'description': forms.Textarea(attrs={"class": "form-control", 'cols': 35, 'rows': 8}),
                'video': forms.ClearableFileInput(),
                }

