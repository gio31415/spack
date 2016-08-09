from spack import *

import spack.environment

class Totalview(Package):
    """
    Totalview parallel debugger
    """

    homepage = "http://www.roguewave.com/products-services/totalview"
    url = 'fakeurl.tar.gz'
    licensed = True
    only_binary = True

    version('8.15.10-2')

    def install(self, spec, prefix):
        pass
