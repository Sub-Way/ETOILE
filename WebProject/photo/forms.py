from photo.models import Album, Photo, Categories
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           fields=['image', 'title', 'description'],
                                           extra=5
                                           )
