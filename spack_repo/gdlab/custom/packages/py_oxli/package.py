# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

import os

class PyOxli(PythonPackage):
    """oxli is a powerful Rust library with a simple Python interface for counting k-mers in genomic sequencing data."""

    homepage = "https://github.com/oxli-bio/oxli"
    url = "https://files.pythonhosted.org/packages/67/5e/360ce8198e3df1c5220b0a7ce0409164e73b10a732371048bf4d11ef3234/oxli-0.3.0.tar.gz"
    pypi = "oxli/oxli-0.3.0.tar.gz"
    maintainers("caelanjmiller")

    license("BSD-3-Clause", checked_by="caelanjmiller")

    version("0.3.0", sha256="5d6903e92aadd3d2f9736b774d32ba71884a6115462fd8b1914a8dc3727ef3ad")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-maturin@1.4:2", type="build")
    depends_on("rust@1.70:", type="build")

    depends_on("py-scipy", type="test")
    depends_on("py-toml@0.10:", type="test")
    depends_on("py-pytest@7.0:", type="test")

    # Patch non-compliant metadata (ORCID)

    build_system("python", "maturin", skip_toml_check=True)

    def patch(self):
        if os.path.exists("pyproject.toml"):
            filter_file(r'orcid\s*=\s*".*"', '', "pyproject.toml")

    def check(self):
        pytest = which("pytest")
        pytest("--pyargs", "oxli")