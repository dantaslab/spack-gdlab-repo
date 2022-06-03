# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPlasclass(PythonPackage):
    """PlasClass: This module allows for easy classification of sequences as
       either plasmid or chromosomal. For example, it can be used to classify
       the contigs in a (metagenomic) assembly."""

    homepage = "https://github.com/Shamir-Lab/PlasClass"
    url      = "https://github.com/Shamir-Lab/PlasClass/archive/refs/tags/v0.1.1.tar.gz"


    version('0.1.1', sha256='af292efedac64d54de9fc27b5765bcef3a69320b1928b1c01cc93144a621717a')

    depends_on('python@3.7', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-scipy@1.3.2',        type=('build', 'run'))
    depends_on('py-scikit-learn@0.21.3',        type=('build', 'run'))
    depends_on('py-joblib@0.14',        type=('build', 'run'))
    depends_on('py-numpy@1.17.4',        type=('build', 'run'))

