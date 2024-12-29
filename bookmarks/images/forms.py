from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widget = {
            "url": forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data["url"]
        if not url:
            return url
        # wrong url
        if "." not in url:
            raise forms.ValidationError("Invalid URL format.")
        valid_extensions = ["jpg", "jpeg", "png"]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                "The given URL does not match valid image extensions."
            )
        return url
