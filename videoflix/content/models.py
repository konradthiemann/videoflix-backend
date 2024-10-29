import os
from datetime import date
from datetime import datetime
import json
from videoflix import settings
from django.db import models
from import_export import resources
from import_export.widgets import JSONWidget

class Video(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos')
    thumbnail = models.ImageField(upload_to='thumbnails')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class VideoResource(resources.ModelResource):
    class Meta:
        model = Video
        fields = ('title', 'description', 'created_at','file')  
        export_order = fields

    def __str__(self):
        return self.title


def export_videos():
    """
    function exports Videodata to backup-directory
    """
    dataset = VideoResource().export()
    dataset_json = dataset.json
    print(dataset_json)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(settings.BACKUP_ROOT, f"videos_{timestamp}.json")
    print(backup_path)

    os.makedirs(settings.BACKUP_ROOT, exist_ok=True)

    with open(backup_path, 'w') as file:
        file.write(dataset_json)

if __name__ == "__main__":
    export_videos()


def import_videos(backup):
    """
    function to reimport Videos from Backup
    """
    video_resource = resources.modelresource_factory(model=Video)()

    with open(backup, 'r') as file:
        json_data = json.load(file)

    for video_json in json_data:
        dataset = dataset.Dataset()
        dataset.json = video_json
        result = video_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
           
            result = video_resource.import_data(dataset, dry_run=False)
            if result.has_errors():
                # Behandeln von Fehlern beim Import
                print(result.errors)
            else:
               
                print(f"Das Video  wurde erfolgreich importiert.")
        else:
            # Fehler beim Probeimport des aktuellen Videos
            print(result.errors)
