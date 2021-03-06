# conan-bacnetstack

[![Conan](https://api.bintray.com/packages/gocarlos/public-conan/bacnetstack:gocarlos/images/download.svg) ](https://bintray.com/gocarlos/public-conan/bacnetstack:gocarlos/_latestVersion)

## lib producer

```bash
# build conan package
conan create . gocarlos/testing --build missing

conan remote add gocarlos https://api.bintray.com/conan/gocarlos/public-conan
conan user -p $BINTRAY_API_KEY -r gocarlos gocarlos

# upload package to gocarlos artifactory
conan upload bacnet-stack -r gocarlos
```

## lib consumer

```bash
conan remote add gocarlos https://api.bintray.com/conan/gocarlos/public-conan
```

add to your conanfile.txt

```toml
[requires]
bacnetstack/4.3.0@gocarlos/testing

[generators]
cmake_find_package
cmake_paths

[options]
# if without openssl
```

add to your CMakeLists.txt

```cmake
find_package(bacnetstack REQUIRED)
#...
add_executable(main main.cpp)
target_link_libraries(main PRIVATE bacnetstack)
```
