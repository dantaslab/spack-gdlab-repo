# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install py-cmseq
#
# You can edit this file again by typing:
#
#     spack edit py-cmseq
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyCmseq(PythonPackage):
    """CMSeq is a set of commands to provide an interface to .bam files for coverage and sequence consensus. Used as a dependency for py-metaphlan."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/SegataLab/cmseq"
    url      = "https://github.com/SegataLab/cmseq/archive/refs/tags/1.0.4.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.0.4', sha256='9d9412b0c58dfaef0d9e3621a0c4b7cd5330dbc1399370d3e69ba03959a26d68')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    depends_on('py-numpy')
    depends_on('samtools@1.0:')
    depends_on('py-pysam')
    depends_on('py-pandas')
    depends_on('py-biopython@:1.76')
    depends_on('py-setuptools@:57', type=('build'))

    def build_args(self, spec, prefix):
        # FIXME: Unknown build system
        args = []
        return args
