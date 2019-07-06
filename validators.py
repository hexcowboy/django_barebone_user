import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z0-9]+$'
    message = _('Username may be 20 characters or fewer. Letters and numbers only.')
    flags = 0
