import requests
import os
import ctypes
import urllib.request
import datetime

API_KEY = 'GPTRKAULZXFwuaDDIkhTOf3Q6wLgWvXvozRER31x' 
URL = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

def get_picture_of_the_day():
    response = requests.get(URL).json()
    image_url = response['hdurl']
    return image_url

def download_image(image_url, image_path):
    urllib.request.urlretrieve(image_url, image_path)

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def main():
    image_url = get_picture_of_the_day()
    folder_path = os.path.join(os.path.expanduser('~'), 'Pictures', 'NASA Wallpapers')
    os.makedirs(folder_path, exist_ok=True)  # creates the directory if it doesn't exist

    # Get the current date and format it as 'YYYY-MM-DD'
    current_date = datetime.date.today().isoformat()

    # Include the date in the filename
    image_path = os.path.join(folder_path, f'wallpaper_{current_date}.jpg')

    download_image(image_url, image_path)
    set_wallpaper(image_path)
if __name__ == '__main__':
    main()