from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="immosheets",
    version="1.1.2",
    author="Arthur RICHARD",
    author_email="arthur.richard@protonmail.com",
    description="Tired of searching with your mouse ? Let's automate the process.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuRHD/immosheets",
    packages=find_packages(),
    package_data={'logo': ['SVGLogo.svg']},
    install_requires=[
        "pydantic==2.6.4",
        "pydantic-settings==2.1.0",
        "requests==2.31.0",
        "google-api-core==2.14.0",
        "google-api-python-client==2.111.0",
        "google-auth==2.23.4",
        "google-auth-httplib2==0.2.0",
        "google-auth-oauthlib==1.1.0",
        "Deprecated==1.2.14"
    ],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
