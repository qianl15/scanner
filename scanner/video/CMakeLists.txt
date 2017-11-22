set(SOURCE_FILES
  h264_byte_stream_index_creator.cpp
  decoder_automata.cpp
  video_decoder.cpp
  video_encoder.cpp)


list(APPEND SOURCE_FILES
  software/software_video_decoder.cpp
  software/software_video_encoder.cpp)

add_library(video OBJECT
  ${SOURCE_FILES})

set_source_files_properties(${PROTO_SRCS} ${GRPC_PROTO_SRCS} PROPERTIES
  GENERATED TRUE)

# SET(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
# SET(BUILD_SHARED_LIBRARIES OFF)
# SET(CMAKE_EXE_LINKER_FLAGS "-static -fPIC -static-libgcc -static-libstdc++  -DNO_TBB=1 -DOPJ_STATIC -lx264 -lm -lpthread -ldl -lrt -lz -lswresample -lxvidcore -lopenjp2 -pie -fPIC")

# # set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ggdb")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static -static-libgcc -static-libstdc++ -fPIC")
# list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/Modules/")
# # find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui imgcodecs)
# # find_package(FFmpeg REQUIRED)
# # find_package(LibLZMA REQUIRED)
# # find_package(SaneProtobuf REQUIRED)
# # find_package(OpenJPEG REQUIRED)

# find_package(SaneProtobuf REQUIRED)
# find_package(FFmpeg REQUIRED)
# find_package(LibLZMA REQUIRED)
# find_package(OpenSSL REQUIRED)
# find_package(BZip2 REQUIRED)
# find_package(Boost COMPONENTS thread program_options regex python REQUIRED)
# find_package(GFlags REQUIRED)
# find_package(Glog REQUIRED)
# find_package(GoogleTest REQUIRED)
# find_package(CURL REQUIRED)
# find_package(Iconv REQUIRED)
# find_package(Storehouse REQUIRED CONFIG
#   PATHS "thirdparty/build/bin/storehouse")
# find_package(TinyToml REQUIRED)
# find_package(PythonLibs 2.7 EXACT REQUIRED)
# find_package(OpenCV COMPONENTS ${OPENCV_DESIRED_COMPONENTS})
# find_package(OpenMP REQUIRED)
# find_package(OpenJPEG REQUIRED)

# set(GTEST_INCLUDE_DIRS
#   "${THIRDPARTY_OUTPUT_PATH}/googletest/include")
# set(GTEST_LIBRARIES
#   "${THIRDPARTY_OUTPUT_PATH}/googletest/lib/libgtest.a")
# set(GTEST_LIB_MAIN
#   "${THIRDPARTY_OUTPUT_PATH}/googletest/lib/libgtest_main.a")

# set(SCANNER_LIBRARIES
#   "${PROTOBUF_LIBRARY}"
#   "${FFMPEG_LIBRARIES}"
#   "-L/opt/ffmpeg-3.3.1/lib"
#   "-lswscale"
#   "${OPJ_LIBRARY}"
#   "${LIBLZMA_LIBRARIES}"
#   "${OPENSSL_LIBRARIES}"
#   "${BZIP2_LIBRARIES}"
#   "${PROXYGEN_LIBRARIES}"
#   "${FOLLY_LIBRARIES}"
#   "${GFLAGS_LIBRARIES}"
#   "${GLOG_LIBRARIES}"
#   "${CURL_LIBRARIES}"
#   "${ICONV_LIBRARIES}"
#   "${SCANNER_LIBRARIES}"
#   "-lpython2.7"
#   "${Boost_LIBRARIES}"
#   "${STOREHOUSE_LIBRARIES}"
#   "-ljpeg"
#   "-lz"
#   "-ldl"
#   "-lopenjp2"
#   "-lgrpc++_unsecure -lgrpc -lgpr"
#   "-fPIE"
#   "-fPIC" )

# # include_directories(SYSTEM ${PROTOBUF_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS} ${FFMPEG_INCLUDE_DIR} ${LIBLZMA_INCLUDE_DIRS} ${OpenJPEG_INCLUDE_DIR}".")

# include_directories( SYSTEM
#   "."
#   "${CMAKE_CURRENT_BINARY_DIR}" # for protobuf generated files
#   "${PROTOBUF_INCLUDE_DIRS}"
#   "${FFMPEG_INCLUDE_DIR}"
#   "${TINYTOML_INCLUDE_DIR}"
#   "${STOREHOUSE_INCLUDE_DIRS}"
#   "${OPENSSL_INCLUDE_DIR}"
#   "${GLOG_INCLUDE_DIRS}"
#   "${LIBLZMA_INCLUDE_DIRS}"
#   "${PYTHON_INCLUDE_DIRS}"
#   "${Boost_INCLUDE_DIRS}")

# if (OpenCV_FOUND)
#   list(APPEND SCANNER_LIBRARIES ${OpenCV_LIBRARIES})
#   include_directories(${OpenCV_INCLUDE_DIRS})
#   add_definitions(-DHAVE_OPENCV)
# endif()

# add_executable(DecoderAutomataCmd decoder_automata_cmd.cpp)
# target_link_libraries(DecoderAutomataCmd ${SCANNER_LIBRARIES} /opt/scanner/build/libscanner.a ${CMAKE_EXE_LINKER_FLAGS})

#add_executable(DecoderAutomataTest decoder_automata_test.cpp)
#target_link_libraries(DecoderAutomataTest
#  ${GTEST_LIBRARIES} ${GTEST_LIB_MAIN}
#  scanner)
#add_test(DecoderAutomataTest DecoderAutomataTest)
