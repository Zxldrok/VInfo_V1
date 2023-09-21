from setuptools import setup, find_packages

setup(
    name="MonLogiciel",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "psutil",
        "gpuinfo",
        "cpuinfo",
    ],
)
