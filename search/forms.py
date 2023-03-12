from search.models import SearchTerm
from django import forms

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchTerm
        exclude = ('search_date', 'ip_address', 'user', 'tracking_id')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['size'] = '10'

        default_text = 'Search'
        self.fields['word'].widget.attrs['value'] = default_text
        self.fields['word'].widget.attrs['onfocus'] = "if(this.value =='" + default_text + "')this.value=''"
        self.fields['word'].required = ''

    include = ('word',)