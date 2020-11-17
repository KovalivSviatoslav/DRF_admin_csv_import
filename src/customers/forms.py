from django.forms import forms


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    csv_file.widget.attrs.update({'accept': ".csv"})
