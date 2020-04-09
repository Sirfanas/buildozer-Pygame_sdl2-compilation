# coding: utf-8

from pythonforandroid.recipe import PythonRecipe, warning


class Pygame_sdl2Recipe(PythonRecipe):

    name = 'pygame_sdl2'
    version = '2.1.0'
    url = 'https://testpypi.python.org/packages/2f/f1/8dd343ae2d97c432cf1c81ca03d2d0472396f9d8e76c677aeae9ce2ec61d/pygame_sdl2-{version}.tar.gz'

    site_packages_name= 'pygame_sdl2'

    depends = []

    def prebuild_arch(self, arch):
        super(Pygame_sdl2Recipe, self).prebuild_arch(arch)
        # AND: Fix this warning!
        warning('Pygame_sdl2 is built assuming the archiver name is '
            'arm-linux-androideabi-ar, which may not always be true!')

recipe = Pygame_sdl2Recipe()
