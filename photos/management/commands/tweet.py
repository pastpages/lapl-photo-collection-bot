import time
from photos.models import Photo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Make tweets at @OldLAPhotos"

    def handle(self, *args, **options):
        obj_list = Photo.objects.untweeted().order_by("-pub_date")[:10]
        for obj in obj_list:
            print(f"Tweeting {obj}")
            obj.tweet()
            time.sleep(3)
