from setuptools import setup

APP = ["main.py"]
DATA_FILES = ["images/money-bag.icns"]

OPTIONS = {
    "iconfile": "images/money-bag.icns",
    "packages": ["openpyxl", "requests", "pyexcel"],
    "plist": {
        "CFBundleName": "Cash Counter",
        "CFBundleDisplayName": "Cash Counter",
        "CFBundleIdentifier": "com.ravenstudios.cashcounter",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
    },
}

setup(
    app=APP,
    name="Cash Counter",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
