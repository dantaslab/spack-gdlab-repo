# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RosettaddgpredictionGit(PythonPackage):
    """RosettaDDGPrediction is a Python package to run Rosetta-based protocols
    for the prediction of the ΔΔG of stability upon mutation of a monomeric
    protein or the ΔΔG of binding upon mutation of a protein complex and analyze
    the results."""

    homepage = "https://github.com/ELELAB/RosettaDDGPrediction"
    git = "https://github.com/ELELAB/RosettaDDGPrediction.git"

    version("master", branch="master")

    # non-python deps
    #depends_on("rosetta", type="run")

    # python-deps
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-mdanalysis", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
