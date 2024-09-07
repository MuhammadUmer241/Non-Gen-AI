import os.path

from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    """
    for getting requirements from requirements.txt
    :param file_path:
    :return: list of packages
    """
    requirement= []
    with open(file_path) as file_obj:
        obj= file_obj.readlines()
    for package in obj:
        if package=="-e.":
            continue
        pack = package.replace("\n", "")
        requirement.append(pack)

    return requirement




setup(
    author="Muhammad Umer",
    version="0.0.1",
    author_email="umernadeem241@gmai.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)