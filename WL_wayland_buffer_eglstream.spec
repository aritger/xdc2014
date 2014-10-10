Name

    WL_wayland_buffer_eglstream

Name Strings

    EGL_WL_wayland_buffer_eglstream

Contributors

    James Jones

Contact

    James Jones, NVIDIA (jajones 'at' nvidia.com)

Status

    Draft

Version

    1 - August 22, 2014

Number

    TBD

Extension Type

    Display extension

Dependencies

    EGL_WL_bind_wayland_display is required.

    EGL_KHR_stream is required.

    EGL_KHR_stream_cross_process_fd is required.

Overview

    It is possible to implement a wayland buffer as an EGLStream that
    further encapsulates the delivery of buffer content, the buffer
    format, and the methods by which it can be composited by the
    wayland compositor.  To enable such implementations, this
    extension adds a mechanism to query an EGLNativeFileDescriptorKHR
    object from a wl_buffer.

IP Status

    No known IP issues.

New Procedures and Functions

    None

New Tokens

    Returned by eglQueryWaylandBufferWL in <value> when <attribute> is
    EGL_WAYLAND_BUFFER_TYPE_WL:

        EGL_WAYLAND_BUFFER_EGLSTREAM_WL         0xXXXX

    Accepted in the <attribute> parameter of eglQueryWaylandBufferWL:

        EGL_WAYLAND_BUFFER_EGLSTREAM_FD_WL      0xXXXX

Additions to the EGL 1.4 Specification:

    (After the section describing how to bind buffers of type
    EGL_WAYLAND_BUFFER_EGLIMAGE_WL to a GL texture, add the following)

    A wl_buffer of type EGL_WAYLAND_BUFFER_EGLSTREAM_WL will contain
    a file descriptor from the wayland client which refers to an
    EGLStreamKHR object that defines the buffer content.  To query
    this file descriptor, eglQueryWaylandBufferWL() can be called with
    <attribute> set to EGL_WAYLAND_BUFFER_EGLSTREAM_FD_WL.  An
    EGLNativeFileDescriptorKHR object will be returned in <value>.
    A local stream object can be created from this object and bound to
    a stream consumer.  Attempting to bind a stream producer to the
    stream, or leaving it unbound will result in undefined behavior.

Issues

    None

Revision History:

    Version 1 (August 22, 2014) James Jones
        Initial draft.
