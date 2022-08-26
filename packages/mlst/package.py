# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mlst
#
# You can edit this file again by typing:
#
#     spack edit mlst
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Mlst(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/tseemann/mlst/archive/refs/tags/v2.22.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("2.22.1", sha256="a8f64d7cb961a8e422e96a19309ad8707f8792d9f755a9e5a1f5742986d19bca")

    depends_on("any2fasta", type=("build", "run"))
    depends_on("blast-plus", type=("build", "run"))
    depends_on("perl@5.26:", type=("build", "run"))
    depends_on("perl-bioperl@1.7.2:", type=("build", "run"))
    depends_on("perl-moo", type=("build", "run"))
    depends_on("perl-list-moreutils", type=("build", "run"))
    depends_on("perl-json", type=("build", "run"))
    depends_on("zlib", type=("build", "run"))
