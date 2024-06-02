###############################################################################

# cibuildwheel --print-build-identifiers
cibuildwheel . --archs all --platform linux --print-build-identifiers
cibuildwheel . --archs all --platform macos --print-build-identifiers

# enable targets:
# cp311-manylinux_x86_64
# cp312-manylinux_x86_64
# cp311-manylinux_aarch64
# cp312-manylinux_aarch64
# cp311-macosx_arm64
# cp312-macosx_arm64

# macos with colima(docker) or linux
cibuildwheel . --archs aarch64 --platform linux
cibuildwheel . --archs x86_64 --platform linux
cibuildwheel . --archs x86_64,aarch64 --platform linux

# TODO: support building cp3xx-macosx_arm64 on local env
# cibuildwheel . --archs arm64 --platform macos

###############################################################################
