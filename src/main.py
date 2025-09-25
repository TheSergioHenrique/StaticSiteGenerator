import os
import shutil

from copystatic import copy_files
from page_generator import generate_page


def main():
    print("Deleting public directory...")
    if os.path.exists("public"):
        shutil.rmtree("public")

    print("Copying static files to public directory...")
    copy_files("static", "public")

    print("Generating page...")
    generate_page("content/index.md", "template.html", "public/index.html")


main()
