from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
