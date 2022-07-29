# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Roary(Package):
    """Rapid large-scale prokaryote pan genome analysis"""
    
    homepage = "https://sanger-pathogens.github.io/Roary/"
    url      = "https://github.com/sanger-pathogens/Roary/archive/refs/tags/v3.13.0.tar.gz"

    version('3.13.0', sha256='375f83c8750b0f4dea5b676471e73e94f3710bc3a327ec88b59f25eae1c3a1e8')

    depends_on('perl@5.8:5.9,5.11.5.13:',   type=('build', 'run'))
    depends_on('perl-array-utils',   type=('build', 'run'))
    depends_on('perl-bioperl',   type=('build', 'run'))
    depends_on('perl-exception-class',   type=('build', 'run'))
    depends_on('perl-graph',   type=('build', 'run'))
    depends_on('perl-file-slurper',   type=('build', 'run'))
    depends_on('perl-file-which',   type=('build', 'run'))
    depends_on('perl-log-log4perl',   type=('build', 'run'))
    depends_on('perl-moose',   type=('build', 'run'))
    depends_on('perl-text-csv',   type=('build', 'run'))
    depends_on('perl-perlio-utf8-strict',   type=('build', 'run'))
    depends_on('perl-devel-overloadinfo',   type=('build', 'run'))
    
    #TODO add the following perl dependencies:
    # File::Basename
    # File::Copy
    # File::Find::Rule
    # File::Grep
    # File::Path
    # File::Spec
    # File::Temp
    # FindBin
    # Getopt::Long
    # Graph::Writer::Dot
    # List::Util
    # Moose::Role
    # Digest::MD5::File

    depends_on('bedtools2',   type=('build', 'run'))
    depends_on('cdhit',   type=('build', 'run'))
    depends_on('blast-plus',   type=('build', 'run'))
    depends_on('mcl',   type=('build', 'run'))
    depends_on('parallel',   type=('build', 'run'))
    depends_on('prank',   type=('build', 'run'))
    depends_on('mafft',   type=('build', 'run'))
    depends_on('fasttree',   type=('build', 'run'))
    
    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
