# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCenoteTaker3(PythonPackage):
    """Discover and annotate the virome."""

    homepage = "https://github.com/mtisza1/Cenote-Taker3"
    url = "https://github.com/mtisza1/Cenote-Taker3/archive/refs/tags/v3.4.4.tar.gz"

    maintainers("caelanjmiller")

    license("MIT", checked_by="caelanjmiller")

    version("3.4.4", sha256="8bd445c5c12862e4870e12287ae8c4b35e98388e2ea51ecee964157df07e1fbc")
    version("3.4.3", sha256="5ffa1b6a158ebbdcdf1d3f5155ef76fee6ac84ec69786e63f23e8513072e3023")
    version("3.4.2", sha256="9982be1db1f0383966404b15159639a225dde848c669479c8923064f942defab")

    depends_on("py-setuptools@61.0:", type="build")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-pyhmmer", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
