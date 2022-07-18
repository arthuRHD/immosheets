from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="seloger-google-sheets",  # Replace with your own username
    version="1.0.0",
    author="Arthur RICHARD",
    author_email="arthur.richard@protonmail.com",
    description="Tired of searching with your mouse ? Let's automate the process.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuRHD/seloger-google-sheets",
    packages=['seloger_google_sheets'],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
