from __future__ import unicode_literals, print_function, division, absolute_import
import django
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_files_import():
    count_files = 0
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, "staticbuilder")):
        for filename in files:
            if filename.endswith(".py"):
                import_filename(os.path.join(root, filename))
                count_files += 1
    if not count_files:
        raise Exception("No .py files found")


def import_filename(filename):
    module = ".".join(filter(None, filename.replace(BASE_DIR, "", 1).split(os.sep)))[:-3]
    if module.endswith(".__init__"):
        module = module[:-9]
    try:
        __import__(module)
    except:
        print("Cannot import module %s" % module, file=sys.stderr)
        raise


if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    django.setup()
    test_files_import()
