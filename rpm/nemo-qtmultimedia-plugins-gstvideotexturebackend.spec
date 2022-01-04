Name:       nemo-qtmultimedia-plugins-gstvideotexturebackend
Summary:    QtMultimedia QML VideoOutput backend for GStreamer NemoVideoTexture interface
Version:    0.1.3
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/nemo-qtmultimedia-plugins
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(nemo-gstreamer-interfaces-1.0) >= 0.20200421.0
BuildRequires:  qt5-qtmultimedia-gsttools

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 

make %{?_smp_mflags}

%install
%qmake5_install

%files
%defattr(-,root,root,-)
%license LICENSE.BSD
%{_libdir}/qt5/plugins/video/declarativevideobackend/libgstnemovideotexturebackend.so
