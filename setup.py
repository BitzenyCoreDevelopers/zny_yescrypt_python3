from distutils.core import setup, Extension

zny_yescrypt_module = Extension('zny_yescrypt',
                            sources = ['yescrypt.c'],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'zny_yescrypt',
       version = '1.0',
       description = 'Bindings for yescrypt proof of work used by bitzeny',
       ext_modules = [zny_yescrypt_module])
