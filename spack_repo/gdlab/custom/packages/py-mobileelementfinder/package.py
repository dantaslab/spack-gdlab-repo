# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMobileelementfinder(PythonPackage):
    """MobileElementFinder is a tool for identifying Mobile Genetic Elements
    (MGEs) in Whole Genome Shotgun sequence data."""

    homepage = "https://pypi.org/project/MobileElementFinder/"
    pypi     = "MobileElementFinder/MobileElementFinder-1.0.5.tar.gz"

    version('1.0.5', sha256='672ff088adb06711a06d31e06f559a64a96e1bfc60776803e77cb2ee3a49d84e')

    depends_on('blast-plus@2.10.0:', type=('build', 'run'))
    depends_on('kma@1.2.3:', type=('build', 'run'))
    depends_on('py-setuptools',  type=('build', 'run'))
    depends_on('py-wheel', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
