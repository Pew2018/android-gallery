package pl.kitek.gallery.data

import pl.kitek.gallery.R

/** Eight self-contained photos loaded from app resources, not remote hosts. */
object DataSource {
    val ITEMS = listOf(
        GalleryItem(1, R.drawable.demo_01),
        GalleryItem(2, R.drawable.demo_02),
        GalleryItem(3, R.drawable.demo_03),
        GalleryItem(4, R.drawable.demo_04),
        GalleryItem(5, R.drawable.demo_05),
        GalleryItem(6, R.drawable.demo_06),
        GalleryItem(7, R.drawable.demo_07),
        GalleryItem(8, R.drawable.demo_08)
    )
}
