# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PerlMoo(PerlPackage):
    """Moo - Minimalist Object Orientation (with Moose compatibility)"""

    homepage = "https://metacpan.org/pod/Moo"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005004.tar.gz"

    version("2.005004", sha256="e3030b80bd554a66f6b3c27fd53b1b5909d12af05c4c11ece9a58f8d1e478928")
