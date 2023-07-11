from setuptools import find_packages, setup
from typing import List


def get_requirements(requirements_filepath: str) -> List[str]:
    """
    This function will return list of requirements
    """

    requirements = []
    with open(requirements_filepath) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e ." )

        return requirements


setup(
    name='end_to_end_ml_project',
    version='1.0.0',
    author='Enoch Amobire',
    author_email='eamobs@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
