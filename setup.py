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
        "pydantic==2.0.3",
        "pydantic-settings==2.0.2",
        "requests==2.31.0",
        "google-api-core==2.11.1",
        "google-api-python-client==2.93.0",
        "google-auth==2.22.0",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==1.0.0"
    ],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
