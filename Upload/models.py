from django.db import models
import os
from django.core.files import File
def get_upload_path(instance, filename):
    f = open('D:\\trusted\\Graduation_Project\\temp.txt', 'w')
    testfile = File(f)
    testfile.write('D:\\trusted\\Graduation_Project\\media\\uploads\\'+instance.name)
    testfile.close
    f.close
    # Construct the upload path based on the instance name and filename
    return os.path.join('uploads', instance.name, filename)

class Folder(models.Model):
    name = models.CharField(max_length=150, default='')
    file1 = models.FileField(max_length=150, upload_to=get_upload_path)
    file2 = models.FileField(max_length=150, upload_to=get_upload_path)

    def save(self, *args, **kwargs):
        # Check if there are existing files
        
        # Set the filename of file1 to "x"
        if self.file1.name:
            self.file1.name = 'alignments.bam'
        # Set the filename of file2 to "y"
        if self.file2.name:
            self.file2.name = 'y.txt'
        super().save(*args, **kwargs)       

class OneFolder(models.Model):
    name = models.CharField(max_length=150, default='')
    file1 = models.FileField(max_length=1500, upload_to=get_upload_path)

    def save(self, *args, **kwargs):
        # Check if there is an existing file
        
        # Set the filename of file1 to "x"
        if self.file1.name:
            self.file1.name = 'alignments.bam'
        super().save(*args, **kwargs)
