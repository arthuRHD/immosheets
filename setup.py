from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="immosheets",  # Replace with your own username
    version="1.0.14",
    author="Arthur RICHARD",
    author_email="arthur.richard@protonmail.com",
    description="Tired of searching with your mouse ? Let's automate the process.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuRHD/immosheets",
    packages=find_packages(),
    install_requires=[
        "pydantic==1.9.1",
        "requests==2.28.1",
        "google-api-core==2.8.2",
        "google-api-python-client==2.52.0",
        "google-auth==2.9.0",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==0.5.2"
    ],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
