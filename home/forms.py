from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows" : "1", "cols" : "50", "id" : "contact-name", "placeholder" : "NAME:"}))
    contact_email = forms.EmailField(required=True, widget=forms.Textarea(attrs={"rows" : "1", "cols" : "50", "id" : "contact-email", "placeholder" : "EMAIL:"}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"rows" : "5", "cols" : "50", "id" : "contact-message", "placeholder" : "MESSAGE:"})
    )