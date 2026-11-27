from django.core.management.base import BaseCommand
from core.models import Subject

class Command(BaseCommand):
    help = 'Create a starter set of ten editable school subjects.'
    def handle(self,*args,**options):
        names=['English','Mathematics','Somali','Arabic','Islamic Studies','Biology','Chemistry','Physics','Geography','History']
        created=0
        for name in names:
            _,was_created=Subject.objects.get_or_create(name=name)
            created += int(was_created)
        self.stdout.write(self.style.SUCCESS(f'Subject setup complete. {created} new subjects added; existing subjects preserved.'))
