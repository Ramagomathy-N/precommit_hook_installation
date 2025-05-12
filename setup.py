from setuptools import setup, find_packages

setup(
    name="precommit_hook_installation",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "snyk",  # Add snyk as a dependency
        "talisman"  # Add talisman as a dependency
    ],
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
