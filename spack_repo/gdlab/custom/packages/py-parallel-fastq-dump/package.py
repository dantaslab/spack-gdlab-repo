# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyParallelFastqDump(PythonPackage):
    """NCBI fastq-dump can be very slow sometimes, even if you have the
       resources (network, IO, CPU) to go faster, even if you already
       downloaded the sra file (see the protip below). This tool speeds
       up the process by dividing the work into multiple threads"""

    homepage = "https://github.com/rvalieris/parallel-fastq-dump"
    url      = "https://github.com/rvalieris/parallel-fastq-dump/archive/refs/tags/0.6.7.tar.gz"

    version('0.6.7', sha256='cb33ea0ed0b1123c100aee7b9ea60a3fc3fc81a3a46be5237c85ba56380617de')
    version('0.6.6', sha256='38a3db72e4f87b8ca2412147a5938372098df15e839c78cddc8a7bfa3dd35b64')

    depends_on('py-setuptools', type='build')
    depends_on('sratoolkit',    type=('build', 'run'))
