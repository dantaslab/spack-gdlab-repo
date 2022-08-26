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
#     spack install any2fasta
#
# You can edit this file again by typing:
#
#     spack edit any2fasta
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Any2fasta(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/tseemann/any2fasta/archive/refs/tags/v0.4.2.tar.gz"

    version("0.4.2", sha256="e4cb2ddccda6298f5b0aee0c10184a75307a08b584d2abbfbf0d59d37b197e73")

    depends_on("perl@5.10:", type=("build", "run"))
