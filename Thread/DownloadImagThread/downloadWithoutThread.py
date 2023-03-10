"""
Python Multitasks - Download sem thread
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""

import requests
import time

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719'
]

t1 = time.perf_counter()

for img_url in img_urls:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = (f"{img_name}.jpg")

    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded...")

t2 = time.perf_counter()

print(f"Finished in {t2-t1} seconds")