import setuptools

with open("README.md" , "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fais",
    version="0.0.1",
    author="Nattapon Donratanapat",
    author_email="pleuk5667@gmail.com",
    description="USGS and Twitter data gathering and analysis tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VidyaSamadi/Research-Team-private",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)