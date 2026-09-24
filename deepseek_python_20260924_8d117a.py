from setuptools import setup, find_packages

setup(
    name="teoria_N",
    version="1.0.0",
    author="Stelian Costin",
    author_email="",
    description="Implementare computationala a teoriei N = {A, F, N}",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/[username]/teoria_N",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20",
        "scipy>=1.7",
    ],
)