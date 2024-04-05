import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyQt6extn", 
    version="1.0.0",
    author="Charles K Barcza",
    author_email="kbarcza@blackpanther.hu",
    description="PySide2extn fork for PyQt6. An Open Source Python Programming language extension for PyQt6, which greatly enhances the capability of the PyQt6 library with extra widgets and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blackPantherOS/PyQt6extn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    install_requires=["PyQt6"],
)