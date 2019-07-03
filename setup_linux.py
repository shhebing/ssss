#!/usr/bin/env python3

import os
from setuptools import setup
from setuptools.extension import Extension
#from distutils.extension import Extension
#from distutils.core import setup
from Cython.Distutils import build_ext
from Cython.Build import cythonize

includedirs=["libs/Voro++/src", "libs/Zeo++"]
libdirs = ["libs/Voro++/src", "libs/Zeo++"]
runtimedir = os.path.realpath("libs/Zeo++")
netstorage_srcfiles = ['cavd/netstorage.pyx' ]
netinfo_srcfiles = ['cavd/netinfo.pyx']
netio_srcfiles = ['cavd/netio.pyx', 'cavd/netinfo.pyx']
graphstorage_srcfiles = ['cavd/graphstorage.pyx']
psd_srcfiles = ['cavd/psd.pyx']
Voronoicell_srcfiles = ['cavd/voronoicell.pyx']
channel_srcfiles = ['cavd/channel.pyx']
highaccuracy_srcfiles = ['cavd/high_accuracy.pyx']
areavol_srcfiles = ['cavd/area_volume.pyx']
cluster_srcfiles = ['cavd/cluster.pyx' ]
geometry_srcfiles = ['cavd/geometry.pyx']
cycle_srcfiles = ['cavd/cycle.pyx']

setup(
    name = 'cavd',
    version = '0.1.16',
    language_level = 3,
    description = "Crystal structure Analysis by Voronoi Decomposition",
    url = "ehpc.shu.edu.cn",
    author = "yeanjiang",
    author_email = "yeanjiang11@qq.com",
    packages=["cavd"],
    package_dir={"cavd": "cavd"},
    license = "",
    cmdclass = {'build_ext':build_ext},
    package_data = {"cavd": ["ionic_radii.json", "bvmparam.dat", "bvse.dat", "BVSEParam.dat"]},
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Cython",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
        ],
    ext_modules = [Extension("cavd.voronoicell", 
                             sources=Voronoicell_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'], 
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.netstorage",
                             sources=netstorage_srcfiles, 
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'], 
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.netinfo", 
                             sources=netinfo_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'], 
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.netio",
                             sources=netio_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.graphstorage",
                             sources=graphstorage_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'], 
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.psd", 
                             sources=psd_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.channel", 
                             sources=channel_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'], 
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.high_accuracy", 
                             sources=highaccuracy_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.area_volume", 
                             sources=areavol_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.cluster", 
                             sources=cluster_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.geometry", 
                             sources=geometry_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                   Extension("cavd.cycle", 
                             sources=cycle_srcfiles,
                             include_dirs=includedirs,
                             libraries = ['voro++', 'zeo++'],
                             library_dirs = libdirs,
                             extra_compiler_args = ['-fPIC -Wl,-rpath='+runtimedir],
                             runtime_library_dirs=[runtimedir],
                             language = 'c++'),
                             ]
)
