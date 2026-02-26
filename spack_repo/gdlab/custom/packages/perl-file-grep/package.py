# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.perl import PerlPackage
from spack.package import *


class PerlFileGrep(PerlPackage):
    """File::Grep mimics the functionality of the grep function in perl, but
       applying it to files instead of a list. This is similar in nature to
       the UNIX grep command, but more powerful as the pattern can be any legal
       perl function."""

    homepage = "https://metacpan.org/pod/File::Grep"
    url      = "https://cpan.metacpan.org/authors/id/M/MN/MNEYLON/File-Grep-0.02.tar.gz"

    version('0.02', sha256='462e15274eb6278521407ea302d9eea7252cd44cab2382871f7de833d5f85632')
