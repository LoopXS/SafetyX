import setuptools


setuptools.setup(
    name="SafetyX",
    version="0.1.8",
    author="None",
    author_email="None@gmail.com",
    description="Hmm",
    long_description="Hmm...",
    long_description_content_type="text/markdown",
    url="https://fuckoff.com",
    packages=setuptools.find_namespace_packages(include=["safety.*"]),
    namespace_packages=["safety"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
