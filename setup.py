from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """ This function returns list of requirements"""
    req = []
    with open(file_path) as files:
        req = files.readlines()
        req = [r.replace("\n"," ") for r in req]
        
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
            
    return req

setup(
    name="Ashu , Enes, Pana",
    version="0.0.1",
    description="Power Eloectronics Lab Report",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)