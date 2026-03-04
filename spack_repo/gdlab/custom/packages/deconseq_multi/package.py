# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DeconseqMulti(Package):
    """The DeconSeq tool can be used to automatically detect and efficiently
    remove sequence contaminations from genomic and metagenomic datasets; optimized for multithreaded usage."""

    homepage = "https://github.com/dantaslab/deconseq-multi"
    url = "https://github.com/dantaslab/deconseq-multi/releases/download/v1.0.0/deconseq-multi-v1.0.0.tar.gz"
    
    maintainers("caelanjmiller")

    license("MIT", checked_by="caelanjmiller")

    version("1.0.0", sha256="d40ea902d9f0ea86e7e0890d948f1e9516d767f98011d588cd6828c3b125309d")

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