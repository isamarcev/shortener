from django.urls import register_converter


class StringConverter:
    """Converter of the url path for redirect"""
    regex = "[-a-zA-Z0-9]+"

    @staticmethod
    def to_python(value):
        return str(value)

    @staticmethod
    def to_url(value):
        return value