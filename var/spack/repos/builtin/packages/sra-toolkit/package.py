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


class SraToolkit(Package):
    """The NCBI SRA Toolkit enables reading ("dumping") of sequencing files
       from the SRA database and writing ("loading") files into the .sra
       format."""

    homepage = "https://trace.ncbi.nlm.nih.gov/Traces/sra"
    url      = "https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2-1/sratoolkit.2.8.2-1-centos_linux64.tar.gz"

    version('2.9.2', '285cb6c328bc3f214fe8954997cf7f4c')
    version('2.8.2-1', '3a2910754aea71aba5662804efff2a68')

    def url_for_version(self, version):
        url = 'https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/{0}/sratoolkit.{0}-centos_linux64.tar.gz'
        return url.format(version)

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin, symlinks=True)
        install_tree('example', prefix.example)
        install_tree('schema', prefix.schema)
