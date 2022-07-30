# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PerlFilePath(PerlPackage):
    """This module provides a convenient way to create directories of arbitrary
       depth and to delete an entire directory subtree from the filesystem."""

    homepage = "https://metacpan.org/pod/File::Path"
    url      = "https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/File-Path-2.18.tar.gz"

    version('2.18_001', sha256='0420e419aaa69b58b0066fe4131656eb2674fef8b38a9adbf55909125c098102')
