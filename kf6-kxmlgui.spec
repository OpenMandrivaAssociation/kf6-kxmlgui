%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6XmlGui
%define devname %mklibname KF6XmlGui -d
#define git 20240217

Name: kf6-kxmlgui
Version: 6.12.0
Release: %{?git:0.%{git}.}2
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kxmlgui/-/archive/master/kxmlgui-master.tar.bz2#/kxmlgui-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kxmlgui-%{version}.tar.xz
%endif
Summary: Framework for managing menu and toolbar actions
URL: https://invent.kde.org/frameworks/kxmlgui
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: python%{pyver}dist(build)
BuildRequires: cmake(Shiboken6)
BuildRequires: cmake(PySide6)
BuildRequires: pkgconfig(python3)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6GlobalAccel)
Requires: %{libname} = %{EVRD}
Obsoletes: kxmlgui-default-settings < %{EVRD}

%description
Framework for managing menu and toolbar actions

%package -n %{libname}
Summary: Framework for managing menu and toolbar actions
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Framework for managing menu and toolbar actions

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Framework for managing menu and toolbar actions

%package -n python-kxmlgui
Summary: Python bindings for KXmlGui
Group: Development/Python
Requires: %{libname} = %{EVRD}

%description -n python-kxmlgui
Python bindings for KXmlGui

%prep
%autosetup -p1 -n kxmlgui-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kxmlgui.*

%files -n %{devname}
%{_includedir}/KF6/KXmlGui
%{_libdir}/cmake/KF6XmlGui
%{_qtdir}/doc/KF6XmlGui.*

%files -n %{libname}
%{_libdir}/libKF6XmlGui.so*

%files -n python-kxmlgui
%{_libdir}/python%{pyver}/site-packages/KXmlGui.cpython-*.so

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kxmlgui6widgets.so
