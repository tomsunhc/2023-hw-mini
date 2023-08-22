cmake_minimum_required(VERSION 3.17...3.27)

if(CMAKE_SOURCE_DIR STREQUAL CMAKE_BINARY_DIR)
  message(FATAL_ERROR "In-source builds are not allowed. Specify build directory like:
  cmake -Bbuild")
endif()

set(PICO_PLATFORM rp2040)

if(NOT DEFINED PICO_BOARD)
  set(PICO_BOARD pico)
endif()

# initialize the SDK based on PICO_SDK_PATH, before project()
include(cmake/pico_sdk_import.cmake)

project(PicoExamples
LANGUAGES C CXX ASM
)

# compilers may default to too-old language standards
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# inspect environment and inform
message(STATUS "CMAKE_EXE_LINKER_FLAGS_INIT: ${CMAKE_EXE_LINKER_FLAGS_INIT}
CMAKE_C_FLAGS: ${CMAKE_C_FLAGS}
CMAKE_CXX_FLAGS: ${CMAKE_CXX_FLAGS}"
)

# --- auto-ignore build directory
file(CONFIGURE OUTPUT .gitignore CONTENT "*")

# Initialize the SDK
pico_sdk_init()

# Each example in a subdirectory for clarity
add_subdirectory(src)
