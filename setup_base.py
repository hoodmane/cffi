import sys, os


sources = ['c/_ffi_backend.c']
libraries = ['ffi']
include_dirs = []


if sys.platform == 'win32':
    COMPILE_LIBFFI = 'libffi_msvc'    # from the CPython distribution
else:
    COMPILE_LIBFFI = None

if COMPILE_LIBFFI:
    include_dirs.append(COMPILE_LIBFFI)
    libraries.remove('ffi')
    sources.extend(os.path.join(COMPILE_LIBFFI, filename)
                   for filename in os.listdir(COMPILE_LIBFFI)
                   if filename.lower().endswith('.c'))


if __name__ == '__main__':
    from distutils.core import setup
    from distutils.extension import Extension
    setup(ext_modules=[Extension(name = '_ffi_backend',
                                 include_dirs=include_dirs,
                                 sources=sources,
                                 libraries=libraries,
                                 )])