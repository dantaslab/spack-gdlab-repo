# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyEte3(PythonPackage):
    """The Environment for Tree Exploration (ETE) is a Python programming
       toolkit that assists in the recontruction, manipulation, analysis and
       visualization of phylogenetic trees"""

    homepage = "http://etetoolkit.org/"
    pypi     = "ete3/ete3-3.1.2.tar.gz"


    version('3.1.2', sha256='4fc987b8c529889d6608fab1101f1455cb5cbd42722788de6aea9c7d0a8e59e9')

    depends_on('py-numpy',        type=('build', 'run'))
    depends_on('py-pyqt5',        type=('build', 'run'))
    depends_on('py-lxml',        type=('build', 'run'))

