from conans import ConanFile, CMake, tools


class BacnetStackConan(ConanFile):
    name = "bacnet-stack"
    version = "4.3.0"
    license = "BSD"
    author = "Carlos Gomes Martinho kmartinho8@gmail.com"
    url = "https://github.com/bacnet-stack/bacnet-stack/"
    description = """
        BACnet Protocol Stack library provides a BACnet application layer,
        network layer and media access (MAC) layer communications services."""
    topics = ("bacnet")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False]
    }
    default_options = {
        "shared": False
    }
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/bacnet-stack/bacnet-stack.git")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BACNET_STACK_BUILD_APPS"] = False
        cmake.configure(source_folder="bacnet-stack")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["bacnet-stack"]
        self.cpp_info.name = "bacnet-stack"
