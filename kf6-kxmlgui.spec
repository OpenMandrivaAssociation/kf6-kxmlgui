%define libname %mklibname KF6XmlGui
%define devname %mklibname KF6XmlGui -d
%define git 20230927

Name: kf6-kxmlgui
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kxmlgui/-/archive/master/kxmlgui-master.tar.bz2#/kxmlgui-%{git}.tar.bz2
Summary: Framework for managing menu and toolbar actions
URL: https://invent.kde.org/frameworks/kxmlgui
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: cmake(KF6GlobalAccel)
# Just to make sure we don't pull in plasma5's xdg-desktop-portal-kde
BuildRequires: plasma6-xdg-desktop-portal-kde
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
%{_qtdir}/mkspecs/modules/qt_KXmlGui.pri
%{_qtdir}/doc/KF6XmlGui.*

%files -n %{libname}
%{_libdir}/libKF6XmlGui.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kxmlgui6widgets.so
