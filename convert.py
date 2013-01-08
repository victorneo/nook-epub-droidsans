import fnmatch
import os
import shutil
import sys
import zipfile
from zipfile import ZipFile


extra_css = '''@font-face {
font-family: "DroidFont", serif, sans-serif;
font-weight: normal;
font-style: normal;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
@font-face {
font-family: "DroidFont", serif, sans-serif;
font-weight: bold;
font-style: normal;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
@font-face {
font-family: "DroidFont", serif, sans-serif;
font-weight: normal;
font-style: italic;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
@font-face {
font-family: "DroidFont", serif, sans-serif;
font-weight: bold;
font-style: italic;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
body { font-family: "DroidFont", serif;}
p{ font-family: "DroidFont", serif;}
div{ font-family: "DroidFont", serif;}
h1{ font-family: "DroidFont", serif;}
h2{ font-family: "DroidFont", serif;}
h3{ font-family: "DroidFont", serif;}
'''
css_link = '<link rel="stylesheet" type="text/css" href="extra_nook.css"/>'


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Specify a filename')
        print('eg. convert.py mybook.epub')
        sys.exit(1)

    epub = sys.argv[1]

    if not zipfile.is_zipfile(epub):
        print('EPUB file given is not a valid zip file.')
        sys.exit(1)

    with ZipFile(open(epub, 'r')) as zf:
        zf.extractall(path='extracted')

    shutil.copytree('extracted', 'output')

    with open('output/OPS/extra_nook.css', 'w') as f:
        f.write(extra_css)

    for fname in os.listdir('extracted/OPS'):
        if not fnmatch.fnmatch(fname, '*.html'):
            continue

        out = open('output/OPS/%s' % fname, 'w')
        with open('extracted/OPS/%s' % fname, 'r') as f:
            for line in f:
                if '</head>' in line:
                    out.write(css_link)
                out.write(line)

        out.close()

    output_fname = '%s_converted.epub' % os.path.splitext(epub)[0]
    shutil.make_archive(output_fname, format='zip', root_dir='output')
    shutil.move('%s.zip' % output_fname, output_fname)

    shutil.rmtree('extracted')
    shutil.rmtree('output')
