from setuptools import setup

APP = ["main.py"]
DATA_FILES = ["images/money-bag.icns"]

OPTIONS = {
    "iconfile": "images/money-bag.icns",
    "packages": ["clipboard"],
    "plist": {
        "CFBundleName": "Drawer Cash Counter",
        "CFBundleDisplayName": "Drawer Cash Counter",
        "CFBundleIdentifier": "com.ravenstudios.drawercashcounter",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
        "NSHumanReadableCopyright": "© 2026 Raven Studios",
    },
}

setup(
    app=APP,
    name="Drawer Cash Counter",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
