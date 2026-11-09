package pl.kitek.gallery.data

data class GalleryItem(val id: Int, val imageResId: Int) {
    companion object {
        fun transitionName(id: Int) = "item_$id"
    }
}
