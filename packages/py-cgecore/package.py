# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyCgecore(PythonPackage):
    """Core module for the Center for Genomic Epidemiology:
       This module contains classes and functions needed to run the service
       wrappers and pipeline scripts"""

    homepage = "https://pypi.org/project/cgecore/"
    pypi     = "cgecore/cgecore-1.5.6.tar.gz"


    version('1.5.6', sha256='310dbaf02c6791dcc17cff7b01930a6260d92328c07cfaaf431742f073fcc758')

    depends_on('py-setuptools', type='build')
    depends_on('py-biopython', type=('build', 'run'))

