"""
Multiprocess - Tratamento de imagens
    Autor: Júlia Onora da Silva
    Data: 19 de janeiro de 2022
"""


import time
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg'
]

if __name__ == '__main__':

    t1 = time.perf_counter()

    size = (1200, 1200)

    for img_name in img_names:
        img = Image.open(img_name)

        img = img.filter(ImageFilter.GaussianBlur(15))

        img.thumbnail(size)
        img.save(f"processed/{img_name}")
        print(f'{img_name} was processed...')

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')