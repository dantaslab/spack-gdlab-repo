# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack import *

class DeconseqMulti(Package):
    """The DeconSeq tool can be used to automatically detect and efficiently
    remove sequence contaminations from genomic and metagenomic datasets; optimized for multithreaded usage."""

    homepage = "https://github.com/dantaslab/deconseq-multi"
    url = "/ref/gdlab/software/custom-packages/deconseq-multi-v1.0.1.tar.gz"
    version('1.0.1', sha256='334d5b8d99fb888d2efa5ee378911c2cbfc875e42589ff66d45a0d77a15b356d')
    
    depends_on("perl@5:")
    def install(self, spec, prefix):
        filter_file(r"#!/usr/bin/perl", "#!/usr/bin/env perl", "deconseq.pl")
        filter_file(r"#!/usr/bin/perl", "#!/usr/bin/env perl", "splitFasta.pl")

        mkdirp(prefix.bin)
        install("bwa64", prefix.bin)
        install("bwaMAC", prefix.bin)
        install("deconseq.pl", prefix.bin)
        install("splitFasta.pl", prefix.bin)
        install("DeconSeqConfig.pm", prefix)

        chmod = which("chmod")
        chmod("+x", join_path(prefix.bin, "bwa64"))
        chmod("+x", join_path(prefix.bin, "bwaMAC"))
        chmod("+x", join_path(prefix.bin, "deconseq.pl"))
        chmod("+x", join_path(prefix.bin, "splitFasta.pl"))

    def setup_run_environment(self, env):
        env.prepend_path("PERL5LIB", self.prefix)