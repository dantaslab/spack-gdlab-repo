# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack_repo.builtin.build_systems.generic import Package
import os

class Metagenemark(Package):
    """Ab initio gene identification in metagenomic sequences
       Nucleic Acids Research (2010) 38, e132 """

    homepage = "http://exon.gatech.edu/GeneMark/"
    url      = "file://{0}/MetaGeneMark_linux_64.tar.gz".format(os.getcwd())
    manual_download = True

    version("3.38", sha256="99c43f22c7fa1ff13ae461e8d7a4624c298da1f9c3a517d291db127055abe206")

    def install(self, spec, prefix):
        mkdirp(prefix.bin) 
        install("mgm/gmhmmp", prefix.bin)
