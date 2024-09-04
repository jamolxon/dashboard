from django.forms import widgets


class CheckboxWidget(widgets.CheckboxInput):
    template_name = "widgets/input.html"


class DateWidget(widgets.DateInput):
    template_name = "widgets/date.html"


class DateTimeWidget(widgets.DateTimeInput):
    template_name = "widgets/datetime.html"


class CkeditorWidget(widgets.Textarea):
    template_name = "widgets/ckeditor.html"
 
