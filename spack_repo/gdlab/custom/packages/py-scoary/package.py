# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage
from spack import *


class PyScoary(PythonPackage):
    """Scoary is designed to take the gene_presence_absence.csv file from Roary as
    well as a traits file created by the user and calculate the assocations 
    between all genes in the accessory genome and the traits. It reports a 
    list of genes sorted by strength of association per trait."""

    homepage = "https://github.com/AdmiralenOla/Scoary"
    url      = "https://github.com/AdmiralenOla/Scoary/releases/download/v1.6.16/scoary-1.6.10.tar.gz"


    version('1.6.16', sha256='f433343422c5805a70a20f7fe83851490ae3cdf07745c65680de5feea40a6dca')

    depends_on('python@3.6', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-scipy@0.16:',        type=('build', 'run'))
    depends_on('py-argparse',        type=('build', 'run'))
    depends_on('py-ete3',        type=('build', 'run'))
    depends_on('py-six',        type=('build', 'run'))

