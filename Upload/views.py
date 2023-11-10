from django.shortcuts import render, redirect
from .forms import FolderForm
from .forms import FolderOneForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import subprocess
from .models import Folder
from .models import OneFolder
from django.conf import settings
import os
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import default_storage
import subprocess
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import subprocess


def Uploadfiles(request):
    form = None
    if request.method == 'POST':
        form = FolderForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded files from the request
            file1 = request.FILES['file1']
            file2 = request.FILES['file2']
            
            # Check if the uploads folder already contains 2 files
            uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            num_files = len(os.listdir(uploads_dir))
            if num_files == 2:
                # Move the existing files to history folder
                history_dir = os.path.join(settings.MEDIA_ROOT, 'history')
                if not os.path.exists(history_dir):
                    os.makedirs(history_dir)
                for filename in os.listdir(uploads_dir):
                    src = os.path.join(uploads_dir, filename)
                    dst = os.path.join(history_dir, filename)
                    os.rename(src, dst)

            # Save the new files to uploads folder
            folder = form.save(commit=False)
            folder.file1 = file1
            folder.file2 = file2
            folder.save()

           

    else:
        form = FolderForm()
    
    return render(request, 'upload.html', {'form':form}) 
      



def Uploadonefiles(request):
    form = None
    if request.method == 'POST':
        form = FolderOneForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file from the request
            file1 = request.FILES['file1']

            # # Check if the uploads OneFolder already contains a file
            # uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            # num_files = len(os.listdir(uploads_dir))
            # if num_files == 1:
            #     # Move the existing file to history OneFolder
            #     history_dir = os.path.join(settings.MEDIA_ROOT, 'history')
            #     if not os.path.exists(history_dir):
            #         os.makedirs(history_dir)
            #     for filename in os.listdir(uploads_dir):
            #         src = os.path.join(uploads_dir, filename)
            #         dst = os.path.join(history_dir, filename)
            #         os.rename(src, dst)

            # Save the new file to the uploads OneFolder
            OneFolder = form.save(commit=False)
            OneFolder.file1 = file1
            OneFolder.save()

            return render(request, 'd.html')

    else:
        form = FolderOneForm()

    return render(request, 'upload.html', {'form': form})


    
import subprocess
from django.shortcuts import render
from django.http import HttpResponseNotFound
import time
def run_docker(request):
    time.sleep(5.5)
    f = open('D:\\trusted\\Graduation_Project\\temp.txt', 'r')
    if f.mode == 'r':
     contents =f.read()
    input_path = contents  # Replace with the actual input file path
    output_path = contents  # Replace with the actual output file path
    file_name = "Final_result.txt"  # Replace with the actual output file name

    input = contents+":/Project/in"
    output1 = contents+":/Project/out"
    # Run the Docker container and capture the output
    cmd = ['docker', 'run', '-v',input,'-v',output1,'project']
    output = subprocess.check_output(cmd).decode('utf-8')


    # file_path = f"{output_path}/{file_name}"

    # try:
    #     with open(file_path, 'r') as file:
    #         file_content = file.read()
    # except FileNotFoundError:
    #     return HttpResponseNotFound("Output file not found")
    
    # context = {
    #     'output_url': '/download/',  # URL to trigger the download
    #     'view_url': '/view/',
    #     'file_name': file_name,
    #     'file_content': file_content,
    # }

    # return render(request, 'd.html', context)


def file_view(request):
    f = open('D:\\trusted\\Graduation_Project\\temp.txt', 'r')
    if f.mode == 'r':
     contents =f.read()
    file_name = "Final_result.txt"  # Replace with the actual file name
    file_path = contents+"\\" + file_name  # Replace with the actual file path

    try:
        file_content = open(file_path, 'r').read()
    except FileNotFoundError:
        return HttpResponseNotFound("File not found")

    context = {
        'output_url': '/download/',  # URL to trigger the download
        'view_url': '/view/',
        'file_name': file_name,
        'file_content': file_content,
    }

    return render(request, 'd.html', context)

from django.http import FileResponse
def download(request):
    f = open('D:\\trusted\\Graduation_Project\\temp.txt', 'r')
    if f.mode == 'r':
     contents =f.read()
    file_name = "Final_result.txt"  # Replace with the actual file name
    file_path = contents+"\\" + file_name  # Replace with the actual file path

    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    except FileNotFoundError:
        return HttpResponseNotFound("File not found")


def view(request):
    f = open('D:\\trusted\\Graduation_Project\\temp.txt', 'r')
    if f.mode == 'r':
     contents =f.read()
    file_name = "Final_result.txt"  # Replace with the actual file name
    file_path = contents+"\\" + file_name  # Replace with the actual file path

    try:
        file_content = open(file_path, 'r').read()
    except FileNotFoundError:
        return HttpResponseNotFound("File not found")

    context = {
        'file_name': file_name,
        'file_content': file_content,
    }

    return render(request, 'view.html', context)