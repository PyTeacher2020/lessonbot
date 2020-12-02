import requests

def vk():
    proxies = {
      'http': 'http://198.16.66.197:8080',
      'https': 'http://198.16.66.197:8080',
    }

    print(requests.get('http://vk.com/', proxies=proxies))