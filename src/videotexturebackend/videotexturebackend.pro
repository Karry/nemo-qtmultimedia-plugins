TEMPLATE = lib
TARGET = gstnemovideotexturebackend
TARGET = $$qtLibraryTarget($$TARGET)

QT += \
        gui \
        gui-private \
        quick \
        multimedia \
        multimedia-private \
        qtmultimediaquicktools-private

CONFIG += plugin hide_symbols link_pkgconfig

PKGCONFIG +=\
        egl \
        gstreamer-1.0 \
        nemo-gstreamer-interfaces-1.0

LIBS += -lqgsttools_p

# It won't compile without this,
# the issue is Xlib.h defines Bool as int but  QJsonValue.h has an enum with Bool = 0x1 --> int = 0x1 -> BOOM!
DEFINES += MESA_EGL_NO_X11_HEADERS

SOURCES += \
        texturevideobuffer.cpp \
        videotexturebackend.cpp

HEADERS += \
        texturevideobuffer.h \
        videotexturebackend.h

target.path = $$[QT_INSTALL_PLUGINS]/video/declarativevideobackend

INSTALLS += target
