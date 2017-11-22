set(SOURCE_FILES
  h264_byte_stream_index_creator.cpp
  decoder_automata.cpp
  video_decoder.cpp
  video_encoder.cpp)

SET(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
SET(BUILD_SHARED_LIBRARIES OFF)
SET(CMAKE_EXE_LINKER_FLAGS "-static -DNO_TBB=1 -lx264 -DOPJ_STATIC -lm -pthread -ldl -lrt")

if (BUILD_CUDA)
  add_definitions(-DHAVE_NVIDIA_VIDEO_HARDWARE)
  list(APPEND SOURCE_FILES
    nvidia/nvidia_video_decoder.cpp)
endif()

if (MFX_FOUND)
  add_definitions(-DHAVE_INTEL_VIDEO_HARDWARE)
  list(APPEND SOURCE_FILES
    intel/intel_video_decoder.cpp)
endif()

list(APPEND SOURCE_FILES
  software/software_video_decoder.cpp
  software/software_video_encoder.cpp)

add_library(video OBJECT
  ${SOURCE_FILES})

set_source_files_properties(${PROTO_SRCS} ${GRPC_PROTO_SRCS} PROPERTIES
  GENERATED TRUE)

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ggdb")

find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui imgcodecs)
find_package(FFmpeg REQUIRED)
find_package(SaneProtobuf REQUIRED)

include_directories(SYSTEM ${PROTOBUF_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS} ${FFMPEG_INCLUDE_DIR} ".")
add_executable(DecoderAutomataCmd decoder_automata_cmd.cpp)
target_link_libraries(DecoderAutomataCmd ${PROTOBUF_LIBRARY} ${FFMPEG_LIBRARIES} ${OpenCV_LIBRARIES} "-L/opt/ffmpeg-3.3.1/lib" /opt/scanner/build/libscanner.a  ${CMAKE_EXE_LINKER_FLAGS})
# add_executable(DecoderAutomataTest decoder_automata_test.cpp)
#target_link_libraries(DecoderAutomataTest
#  ${GTEST_LIBRARIES} ${GTEST_LIB_MAIN}
#  scanner)
#add_test(DecoderAutomataTest DecoderAutomataTest)
