import webbrowser
import requests

def open_website():
    website_name=input('please enter the website name (e.g., "redbus"):')
    url=f"https://www.{website_name}.com"
    try:
        response=requests.get(url)
        response.raise_for_status()
        webbrowser.open(url)
        print(f"opening {url}...")
    except requests.exceptions.RequestException as e:
        print(f"failed to open {url}. Error: {e}")
open_website()


