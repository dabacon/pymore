# Copyright 2021 The pymore Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os
from setuptools import setup

name = "pymore"

description = "Mo python, less problems. Helpful python utilities."

long_description = io.open("README.md", encoding="utf-8").read()

# Read in requirements
requirements = open("requirements.txt").readlines()
requirements = [r.strip() for r in requirements]
dev_requirements = open("requirements-dev.txt").readlines()
dev_requirements = [r.strip() for r in dev_requirements]

pymore_packages = ["pymore"]

setup(
    name=name,
    version="0.1.3",
    url="http://github.com/dabacon/pymore",
    author="The pymore Developers",
    author_email="dabacon@gmail.com",
    python_requires=(">=3.6.0"),
    install_requires=requirements,
    extras_require={
        "dev_env": dev_requirements,
    },
    license="Apache 2",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=pymore_packages,
    include_package_data=True,
)

# Instruction for release
# 1. Create distribution:
#   python setup.py sdist bdist_wheel
# 2. Check the distribution:
#   twine check dist/*
# 3. Upload to test pypi:
#   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# 4. Visit https://test.pypi.org/project/pymore/ and check.
# 5. Upload to prod pypi:
#   twine upload dist/*
# 6. Confirm on https://pypi.org/project/pymore/
