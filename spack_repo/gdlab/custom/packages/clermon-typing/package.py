# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack.package import *

class ClermonTyping(Package):
    """An easy-to-use and accurate in silico method for Escherichia genus strain phylotyping."""
    
    homepage = "https://github.com/dantaslab/ClermonTyping"
    url = "https://github.com/dantaslab/ClermonTyping/releases/download/v1.0.0/clermont-typing-1.0.0.tar.gz"
    version("1.0.0", sha256="849f753637e8abe9cd67042a3538a9fd1052c913113fa4e0362ce3d54a71b67f")
    depends_on("r@3.4.2", type="run")
    depends_on("r-readr@2.1.3", type="run")
    depends_on("r-dplyr@1.0.9", type="run")
    depends_on("r-tidyr@1.3.0", type="run")
    depends_on("r-stringr@1.5.0", type="run")
    depends_on("r-knitr@1.39", type="run")
    depends_on("pandoc", type="run")
    depends_on("blast-plus", type="run")
    depends_on("py-biopython", type="run")
    
    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
        install_tree("data", prefix.data)
        install("clermonTyping.sh", prefix.bin)
        chmod = which("chmod")
        chmod("+x", join_path(prefix.bin, "clermonTyping.sh"))
