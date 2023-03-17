import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kmidataset",
    version="0.1.0",
    author="parkminwoo",
    author_email="parkminwoo1991@gmail.com",
    description="This dataset includes some macroeconomic indicators for South Korea in 2021-2022.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSDanielPark/kmi2122-dataset",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
    "json", "pandas"
    ])