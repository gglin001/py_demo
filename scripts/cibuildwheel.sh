###############################################################################

# cibuildwheel --print-build-identifiers
cibuildwheel . --archs all --platform linux --print-build-identifiers
cibuildwheel . --archs all --platform macos --print-build-identifiers

# macos with colima(docker) or linux
cibuildwheel . --archs aarch64 --platform linux
cibuildwheel . --archs x86_64 --platform linux
cibuildwheel . --archs x86_64,aarch64 --platform linux

# TODO: support building cp3xx-macosx_arm64 on local env
# cibuildwheel . --archs arm64 --platform macos

###############################################################################
