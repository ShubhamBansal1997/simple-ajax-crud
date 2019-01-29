from django import forms

from .models import Book


class BookForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Book
		fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type',)
