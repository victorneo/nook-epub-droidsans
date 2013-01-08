## Nook EPUB Droidsans

This is a simple Python script for injecting a CSS stylesheet into an OPS EPUB file that
will force the reader to render using the `DroidSans` font.

### Motivation

On certain E-Reader devices, such as the [first generation Nook](http://www.barnesandnoble.com/u/Support-NOOK-1st-Edition/379003191),
non-English characters such as Chinese are not displayed correctly without the
correct font.

The [existing method](http://www.cnepub.com/discuz/forum.php?mod=viewthread&tid=21195&page=1&authorid=144624)
is to add additional CSS declaractions into the EPUB by using Calibre.

As I do not use Calibre for managing my Ebooks, I wrote this simple script to
create a CSS file and add the `<link>` tag to all HTML files within the EPUB file.

### Usage

    python convert.py [epub file name]

    eg. python convert.py my_book.epub
    An EPUB file named my_book_nook.epub will be generated.
    The original EPUB file is left untouched.

### Caveats

The script assumes that your EPUB file uses OPS, or Open Publication Structure and does not contain DRM.
