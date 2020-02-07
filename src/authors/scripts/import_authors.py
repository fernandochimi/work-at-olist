import csv

from authors.models import Author


def run(file):
    try:
        file = open(file)
        reader = csv.DictReader(file)

        Author.objects.all().delete()

        for row in reader:
            author, created = Author.objects.get_or_create(name=row['name'])
        return "Import data with success"
    except Exception as e:
        raise e
