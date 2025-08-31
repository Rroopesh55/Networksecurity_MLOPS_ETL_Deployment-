"""
The setup module for the NETWORKSECURITY project.
this file is an essential for packaging and distributing the project.
It provides metadata about the project and instructions on how to install it.
It specifies the package name, version, author details, description, and dependencies required for the project to run.
It also includes information about the project's license and classifiers that help users understand the project's purpose and compatibility.
"""
from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements"""
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt","r") as file:
            #Read lines from the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except fileNotFoundError:
        print("The requirements.txt file is not found.")
    return requirement_lst
        
print(get_requirements())

setup(
    name="NETWORKSECURITY",
    version="0.0.1",
    author="Rroopesh Hari",
    author_email="rroopesh.hari@okstate.edu",
    description="A Machine Learning Project For Network Security",
    packages=find_packages(),
    install_requires=get_requirements()
)
            
            

