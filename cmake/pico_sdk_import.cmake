# This is a copy of <PICO_SDK_PATH>/external/pico_sdk_import.cmake

# This can be dropped into an external project to help locate this SDK
# It should be include()ed prior to project()

set(pico_sdk_tag 1.5.1)

set(pico_sdk_submod lib/tinyusb)
if(PICO_BOARD STREQUAL "pico_w")
  list(APPEND pico_sdk_submod lib/cyw43-driver lib/lwip)
endif()

set(FETCHCONTENT_UPDATE_DISCONNECTED ON)
set(FETCHCONTENT_QUIET OFF)
if (DEFINED ENV{PICO_SDK_PATH} AND NOT PICO_SDK_PATH)
    set(PICO_SDK_PATH $ENV{PICO_SDK_PATH})
    message("Using PICO_SDK_PATH from environment ('${PICO_SDK_PATH}')")
endif ()


if(NOT PICO_SDK_PATH)
  include(FetchContent)

  FetchContent_Declare(pico_sdk
  GIT_REPOSITORY https://github.com/raspberrypi/pico-sdk
  GIT_TAG ${pico_sdk_tag}
  GIT_SUBMODULES ${pico_sdk_submod}
  GIT_SHALLOW true
  TLS_VERIFY true
  GIT_SUBMODULES_RECURSE false
  )

  FetchContent_Populate(pico_sdk)

  set(PICO_SDK_PATH ${pico_sdk_SOURCE_DIR})
endif()

get_filename_component(PICO_SDK_PATH "${PICO_SDK_PATH}" REALPATH BASE_DIR "${PROJECT_BINARY_DIR}")
if (NOT IS_DIRECTORY ${PICO_SDK_PATH})
  message(FATAL_ERROR "Directory '${PICO_SDK_PATH}' not found")
endif()

set(PICO_SDK_INIT_CMAKE_FILE ${PICO_SDK_PATH}/pico_sdk_init.cmake)
if (NOT EXISTS ${PICO_SDK_INIT_CMAKE_FILE})
  message(FATAL_ERROR "Directory '${PICO_SDK_PATH}' does not appear to contain the Raspberry Pi Pico SDK")
endif()

set(PICO_SDK_PATH ${PICO_SDK_PATH} CACHE PATH "Path to the Raspberry Pi Pico SDK" FORCE)

include(${PICO_SDK_INIT_CMAKE_FILE})
