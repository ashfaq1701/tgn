from setuptools import setup, find_packages

setup(
    name="tgn",
    version="0.0.1",
    author="Emanuele Rossi",
    author_email="erossi@twitter.com",
    description="Temporal Graph Embedding",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ashfaq1701/tgn",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "pandas",
        "torch",
        "scikit_learn"
    ],
)