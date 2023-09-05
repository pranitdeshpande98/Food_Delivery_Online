import os
from django.core.exceptions import ValidationError


def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]

    valid_extensions = ['.png','.jpeg','.jpg']
    if  not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported File Extension. Allowed extensions: '+str(valid_extensions))
    
