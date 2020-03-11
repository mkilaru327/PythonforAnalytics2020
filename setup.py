import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kilarupkg", # Replace with your own username
    version="0.0.1",
    author="Megha Kilaru",
    author_email="mkilaru@uchicago.edu",
    description="Python for Analytics Class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkilaru327/PythonforAnalytics2020",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)