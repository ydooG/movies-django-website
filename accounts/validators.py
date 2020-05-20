from django.core.exceptions import ValidationError


# Doesn't work
class PasswordsAreEqualValidator(object):
    def __init__(self, password1):
        self.password1 = password1

    def validate(self, password2, user=None):
        if password2 != self.password1:
            raise ValidationError('Passwords don\'t match', code='not equal passwords')

    def get_help_text(self):
        return 'Passwords should be equal.'
