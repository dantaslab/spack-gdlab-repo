# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fastp(MakefilePackage):
    """A tool designed to provide fast
    all-in-one preprocessing for FastQ files."""

    homepage = "https://github.com/OpenGene/fastp"
    url = "https://github.com/OpenGene/fastp/archive/v0.20.0.tar.gz"

    version("1.0.1", sha256="80464cca840f7ecaeec63528cc5c4b138af83da909f91291115e1811e5f8cec6")
    version("1.0.0", sha256="cd8ba4bbadacadf22a8dd83445455717689a01c774a0a0c23cf36f7a05496c91")
    version("0.26.0", sha256="ab5396f448bece92e599e4d3acc48751fc46f0f43333ca271d229aa95dc47c4e")
    version("0.25.0", sha256="55fa7d9b8166200e901ff59a1825ba6455ec1a322d9465ce40aae6d145c3146f")
    version("0.23.4", sha256="4fad6db156e769d46071add8a778a13a5cb5186bc1e1a5f9b1ffd499d84d72b5")
    version("0.23.3", sha256="a37ee4b5dcf836a5a19baec645657b71d9dcd69ee843998f41f921e9b67350e3")
    version("0.20.0", sha256="8d751d2746db11ff233032fc49e3bcc8b53758dd4596fdcf4b4099a4d702ac22")

    depends_on("libisal", type=("build", "link"), when="@0.23:")
    depends_on("libdeflate", type=("build", "link"), when="@0.23:")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make("install", "PREFIX={0}".format(prefix))
