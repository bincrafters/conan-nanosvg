#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class LibnameConan(ConanFile):
    name = "nanosvg"
    version = "0.0.0"
    url = "https://github.com/bincrafters/conan-nanosvg"
    description = "Simple stupid SVG parser"
    
    # Indicates License type of the packaged library
    license = "ZLIB"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/memononen/nanosvg"
        tools.get("{0}/archive/master.zip".format(source_url))
        extracted_dir = self.name + "-master"

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = os.path.join(self.source_subfolder, "src")
        self.copy(pattern="LICENSE")
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
