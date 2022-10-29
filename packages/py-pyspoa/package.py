# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPyspoa(PythonPackage):
    """Python bindings to spoa"""

    homepage = "https://github.com/nanoporetech/pyspoa"
    pypi = "pyspoa/pyspoa-0.0.8.tar.gz"

    version("0.0.8", sha256="8299d18066b498a6ef294c5a33a99266ded06eeb022f67488d2caecba974b0a4")

    depends_on("py-setuptools", type="build")
    depends_on("cmake@3.18.4", type="build")
    depends_on("py-pybind11@2.4:", type=("build", "run"))
