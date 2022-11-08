from django.core.exceptions import ValidationError


def validate_username(value):
    value = value.replace('_', '')
    if not value.isalnum():
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
