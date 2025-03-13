from setuptools import find_packages, setup

def get_requirements(file_path):
    """
    Reads requirements.txt and returns a list of dependencies.
    """
    with open(file_path, "r") as file:
        requirements = [line.strip() for line in file if line.strip() and not line.startswith("#")]
    
    # Remove "-e ." if present
    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements

setup(
    name="mlproject_StudentPerformance",
    version="0.0.1",
    author="Somen",
    author_email="somenmishra333@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
