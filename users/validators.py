from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


def AgeCheckValidator(value: date):
    difference = relativedelta(date.today(), value).years
    if difference < 9:
        raise ValidationError(
            ('is too small: %(value)s'),
            params={"value": value},
        )


def EmailCheckValidator(value: str):
    if '@rambler' in value:
        raise ValidationError(
            ('Is not correct: %(value)s'),
            params={'value': value},

        )
