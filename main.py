import requests
import subprocess
from bs4 import BeautifulSoup


def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('title')
    return title_tag.text if title_tag else "No title tag found"


def download_m3u8_video(m3u8_url, output_file):
    command = ['ffmpeg', '-i', m3u8_url, '-c', 'copy', output_file]
    subprocess.call(command)


name_file = get_title(input('ссылка на страницу '))

m3u8_url = input('ссылка на m3u8 ')
output_file = f'{name_file}.mp4'

download_m3u8_video(m3u8_url, output_file)
