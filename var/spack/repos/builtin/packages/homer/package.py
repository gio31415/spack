##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class Homer(MakefilePackage):
    """	HOMER (Hypergeometric Optimization of Motif EnRichment) is a suite of
        tools for Motif Discovery and next-gen sequencing analysis."""

    homepage = "http://homer.ucsd.edu/homer"
    url      = "http://homer.ucsd.edu/homer/data/software/homer.v4.10.3.zip"

    version('4.9.1', 'ed5742bf69b72fc92810a2e2fb0fd129')

    depends_on('zip')

    def edit(self, spec, prefix):
        with working_dir("cpp", create=False):
            makefile = FileFilter('Makefile')
            makefile.filter('COMPILER = .*', 'COMPILER = c++')

    def build(self, spec, prefix):
        with working_dir("cpp"):
            make('clean')
            make()

    def install(self, spec, prefix):
        install_tree(join_path(self.stage.source_path, 'bin'),
                    self.prefix.bin)
