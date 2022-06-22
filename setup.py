import os
import shutil
import urllib.error
import urllib.request


def create_dir():
    """
    Create a directories 'resources', 'resources/data/' and 'resources/download/data' in the current working directory if not exist
    :return:
    """
    
    try:
        os.makedirs(os.path.join('resources'))
        print('Success: Directory created resources')
    except FileExistsError:
        print('Directory already exist: resources')
    
    try:
        os.makedirs(os.path.join('resources', 'data'))
        print('Success: Directory created resources/data')
    except FileExistsError:
        print('Directory already exist: resources/data')
        
    try:
        os.makedirs(os.path.join('resources', 'styles'))
        print('Success: Directory created resources/styles')
    except FileExistsError:
        print('Directory already exist: resources/styles')
        
    try:
        os.makedirs(os.path.join('resources', 'images'))
        print('Success: Directory created resources/images')
    except FileExistsError:
        print('Directory already exist: resources/images')
        
    try:
        os.makedirs(os.path.join('resources', 'download'))
        print('Success: Directory created resources/download')
    except FileExistsError:
        print('Directory already exist: resources/download')


def download_unpack(data_url):
    """
    Download file to 'resources/data'
    :param data_url:
    :return:
    """
    file_name = data_url.split("/")[-1]
    data_path = os.path.join('resources', 'data')
    data_file = os.path.join(data_path, file_name)
    if not os.path.exists(data_file):
        try:
            urllib.request.urlretrieve(data_url, data_file)
            print("Success: File downloaded " + data_file)
        except urllib.error.URLError:
            print("Something went wrong: Could download file")
    else:
        print('File already exist: ' + data_file)

    try:
        shutil.unpack_archive(data_file, data_path)
        print("Success: File unpacked")
    except shutil.Error:
        print("Something went wrong: Could unpack file")


if __name__ == 'main':
    # Setup relevant project directories
    create_dir()

    # Download and extract archived dataset
    data_url = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz'
    download_unpack(data_url)
