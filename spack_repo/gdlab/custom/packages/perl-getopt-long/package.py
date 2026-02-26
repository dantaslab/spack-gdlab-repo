# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PerlGetoptLong(PerlPackage):
    """The Getopt::Long module implements an extended getopt function called
       GetOptions(). It parses the command line from @ARGV, recognizing
       and removing specified options and their possible values."""

    homepage = "https://metacpan.org/pod/Getopt::Long"
    url      = "https://cpan.metacpan.org/authors/id/J/JV/JV/Getopt-Long-2.52.tar.gz"

    version('2.52', sha256='9dc7a7c373353d5c05efae548e7b123aa8a31d1f506eb8dbbec8f0dca77705fa')
