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

#     spack install dorado
#
# You can edit this file again by typing:
#
#     spack edit dorado
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Dorado(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://cdn.oxfordnanoportal.com/software/analysis/dorado-1.1.1-linux-x64.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.1.1', sha256='08f6ef13b23867bddaa2abee292627e617ca2d2d68d9379dcae703add9940360')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    depends_on('cuda@11.0.0:', when='@6.5.7-cuda', type='run')
    def install(self, spec, prefix):
        # FIXME: Unknown build system
        install_tree("bin", prefix.bin)
        install_tree("lib", prefix.lib)
