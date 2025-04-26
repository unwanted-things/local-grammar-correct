from setuptools import setup, find_packages

setup(
    name="local-grammar-correct",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click==8.1.7",
        "pyspellchecker==0.7.2"
    ],
    entry_points={
        'console_scripts': [
            'local-grammar-correct=grammar_correct:cli',
        ],
    },
    author="unwanted-things",
    author_email="",
    description="A local CLI tool for grammar correction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/unwanted-things/local-grammar-correct",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 