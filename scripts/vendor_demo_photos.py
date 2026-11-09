#!/usr/bin/env python3
"""Vendor eight CC0 photographs from Wikimedia Commons for an offline demo APK."""
import hashlib
import io
import time
import urllib.parse
import urllib.request
from pathlib import Path
from PIL import Image, ImageOps

SOURCES = [
    ("01", "Lake Mountain Landscape.jpg"),
    ("02", "Price Building illuminated at night in Quebec City.jpg"),
    ("03", "Cube berlin.jpg"),
    ("04", "Piece of chocolate cake on a white plate decorated with chocolate sauce.jpg"),
    ("05", "Sossusvlei Dunes Namib.jpg"),
    ("06", "Sunset sea and sky (Unsplash).jpg"),
    ("07", "Sang Farsh Fruit and Vegetable Market.jpg"),
    ("08", "Cascade de Glandieu, octobre 2019 (1).jpg"),
]
OUTPUT = Path("app/src/main/res/drawable-nodpi")
OUTPUT.mkdir(parents=True, exist_ok=True)

def fetch_photo(name):
    filename = name.replace(" ", "_")
    digest = hashlib.md5(filename.encode("utf-8")).hexdigest()
    encoded = urllib.parse.quote(filename)
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/{}/{}/{}".format(
            digest[0], digest[:2], encoded),
        "https://commons.wikimedia.org/wiki/Special:FilePath/{}".format(encoded),
    ]
    for url in urls:
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": "AndroidGallerySample/1.0 (https://github.com/Pew2018/android-gallery)"})
                with urllib.request.urlopen(req, timeout=75) as stream:
                    contents = stream.read(28 * 1024 * 1024)
                img = Image.open(io.BytesIO(contents))
                img.load()
                return img
            except Exception as error:
                print("Download retry for {}: {}".format(name, error), flush=True)
                time.sleep(2 + attempt * 2)
    raise RuntimeError("Could not download CC0 photo: " + name)

for number, name in SOURCES:
    path = OUTPUT / ("demo_{}.jpg".format(number))
    if path.exists():
        with Image.open(str(path)) as image:
            image.verify()
        print("Using packaged photo: " + str(path))
        continue
    image = ImageOps.exif_transpose(fetch_photo(name)).convert("RGB")
    image.thumbnail((1400, 1400), Image.Resampling.LANCZOS)
    image.save(str(path), format="JPEG", quality=85, optimize=True, progressive=True)
    with Image.open(str(path)) as verify:
        verify.verify()
    print("Created {} ({} bytes)".format(path, path.stat().st_size), flush=True)

assert len(list(OUTPUT.glob("demo_*.jpg"))) == 8
print("Verified eight bundled offline photos", flush=True)
