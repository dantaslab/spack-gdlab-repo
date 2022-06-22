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
#     spack install py-metaphlan
#
# You can edit this file again by typing:
#
#     spack edit py-metaphlan
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyMetaphlan(Package):
    """Description: MetaPhlAn is a computational tool for profiling the composition of microbial communities (Bacteria, Archaea and Eukaryotes) from metagenomic shotgun sequencing data (i.e. not 16S) with species-level. With the newly added StrainPhlAn module, it is now possible to perform accurate strain-level microbial profiling."""

    # URL for your package's homepage.
    homepage = "https://github.com/biobakery/MetaPhlAn#:~:text=Description-,MetaPhlAn%20is%20a%20computational%20tool%20for%20profiling%20the%20composition%20of,accurate%20strain%2Dlevel%20microbial%20profiling."
    url      = "https://github.com/biobakery/MetaPhlAn/archive/refs/tags/3.0.14.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated. - no updates
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('3.0.14', sha256='6553a0e7e027e4b26feab0fa50418da45331d318bb1406020b8e6a376b1772c0')

    # FIXME: Add dependencies if required.

    depends_on('python@3:')
    depends_on('py-numpy')
    depends_on('py-h5py')
    depends_on('py-biom-format')
    depends_on('py-biopython')
    depends_on('py-pandas')
    depends_on('py-scipy')
    depends_on('py-requests')
    depends_on('py-dendropy')
    depends_on('py-pysam')
    depends_on('py-cmseq')
    depends_on('py-phylophlan')


    def build_args(self, spec, prefix):
        # FIXME: Unknown build system
        args = []
        return args
