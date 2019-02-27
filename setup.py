import setuptools

with open("README.md" , "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fsia',
    version='0.1.1',
    scripts=['fsia'],
    author="Nattapon Donratanapat",
    author_email="pleuk5667@gmail.com",
    description="A data gathering tools for USGS and Twitter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VidyaSamadi/Research-Team",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)