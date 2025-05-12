from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess

class CustomInstallCommand(install):
    """Custom install command to run post-install script."""
    def run(self):
        # Run the standard install process
        install.run(self)
        # Run the pre-commit hook installation script
        try:
            subprocess.check_call(["install-precommit-hook"])
        except Exception as e:
            print(f"Error running post-install script: {e}")

setup(
    name="precommit_hook_installation",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # No snyk or talisman dependencies
    ],
    cmdclass={
        "install": CustomInstallCommand,
    },
    entry_points={
        "console_scripts": [
            "install-precommit-hook=precommit_hook_installation.install_hook:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
