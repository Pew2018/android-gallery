# Offline demo images

Eight photographs are bundled inside the Release APK as `demo_01.jpg` through `demo_08.jpg`, with no runtime Internet access or gallery permissions required. All photographs are listed as CC0 1.0 on their Wikimedia Commons source pages. Images are resized and stripped of source metadata for compact test APKs.

| File | Wikimedia Commons source | Author | License |
|---|---|---|---|
| demo_01.jpg | [Lake Mountain Landscape.jpg](https://commons.wikimedia.org/wiki/File:Lake_Mountain_Landscape.jpg) | Bonnie Moreland | CC0 1.0 |
| demo_02.jpg | [Price Building illuminated at night in Quebec City.jpg](https://commons.wikimedia.org/wiki/File:Price_Building_illuminated_at_night_in_Quebec_City.jpg) | Wilfredor | CC0 1.0 |
| demo_03.jpg | [Cube berlin.jpg](https://commons.wikimedia.org/wiki/File:Cube_berlin.jpg) | Shisma | CC0 1.0 |
| demo_04.jpg | [Piece of chocolate cake on a white plate decorated with chocolate sauce.jpg](https://commons.wikimedia.org/wiki/File:Piece_of_chocolate_cake_on_a_white_plate_decorated_with_chocolate_sauce.jpg) | Daria Yakovleva | CC0 1.0 |
| demo_05.jpg | [Sossusvlei Dunes Namib.jpg](https://commons.wikimedia.org/wiki/File:Sossusvlei_Dunes_Namib.jpg) | Vicartb | CC0 1.0 |
| demo_06.jpg | [Sunset sea and sky (Unsplash).jpg](https://commons.wikimedia.org/wiki/File:Sunset_sea_and_sky_(Unsplash).jpg) | James Harris | CC0 1.0 |
| demo_07.jpg | [Sang Farsh Fruit and Vegetable Market.jpg](https://commons.wikimedia.org/wiki/File:Sang_Farsh_Fruit_and_Vegetable_Market.jpg) | Behnam9395 | CC0 1.0 |
| demo_08.jpg | [Cascade de Glandieu, octobre 2019 (1).jpg](https://commons.wikimedia.org/wiki/File:Cascade_de_Glandieu%2C_octobre_2019_(1).jpg) | Benoît Prieur | CC0 1.0 |

To populate the Android drawable resources before the first build, run `python3 scripts/vendor_demo_photos.py` after installing Pillow. Once resources exist, all images load completely offline.
