# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCheckv(PythonPackage):
    """CheckV is a fully automated command-line pipeline for assessing the quality of single-contig viral genomes, including identification of host contamination for integrated proviruses, estimating completeness for genome fragments, and identification of closed genomes."""

    homepage = "https://bitbucket.org/berkeleylab/checkv/src/master/"
    pypi = "checkv/checkv-1.0.3.tar.gz"

    maintainers("caelanjmiller")

    license("BSD-3-Clause", checked_by="caelanjmiller")

    version("1.0.3", sha256="2438516f270191267a9860dfe31bf596d64a4fbc16be922b46fb6a4fd98d762a")

    depends_on("py-flit-core@3.2:3", type="build")
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("hmmer@3.3", type="run")
    depends_on("prodigal@2.6.3", type="run")
    depends_on("diamond@2.1.8", type="run")
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-numpy@1.5:", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-oxli", type=("build", "run"))
