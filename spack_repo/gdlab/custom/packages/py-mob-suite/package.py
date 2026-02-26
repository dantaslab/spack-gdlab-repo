# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#

from spack_repo.builtin.build_systems.python import PythonPackage
from spack import *


class PyMobSuite(PythonPackage):
    """MOB-suite: Software tools for clustering, reconstruction and typing of
       plasmids from draft assemblies"""

    homepage = "https://github.com/phac-nml/mob-suite"
    pypi     = "mob_suite/mob_suite-3.1.0.tar.gz"


    version('3.1.0', sha256='03b502673dd115ccceaf912330cb7f4e38b77c9ab895119891ecf8ef0e115f91')

    depends_on('python@3.7.0:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-pytest-runner', type='build')
    depends_on('py-pytest', type='build')
    depends_on('py-numpy@1.11.1:',        type=('build', 'run'))
    depends_on('py-tables@3.3.0:',        type=('build', 'run'))
    depends_on('py-pandas@0.22.0:1.0.5',        type=('build', 'run'))
    depends_on('py-biopython@1.70:',        type=('build', 'run'))
    depends_on('py-pycurl@7.43.0:',        type=('build', 'run'))
    depends_on('py-scipy@1.1.0:',        type=('build', 'run'))
    depends_on('py-ete3@3.0:',        type=('build', 'run'))
    depends_on('py-six@1.10:',        type=('build', 'run'))
    depends_on('blast-plus', type='run')
    depends_on('mash', type='run')
