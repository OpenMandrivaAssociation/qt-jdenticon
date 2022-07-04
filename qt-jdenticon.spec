%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$
 
Name: qt-jdenticon
Version: 0.3.0
Release: 1
License: MIT
Summary: Jdenticon Qt5 plugin
URL: https://github.com/Nheko-Reborn/qt-jdenticon
Source0: https://github.com/Nheko-Reborn/qt-jdenticon/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: make
BuildRequires: qt5-qtbase-devel
 
%description
Special Qt5/C++14 port of Jdenticon distributed as a Qt plugin.
 
The eventual plan for this is that it will be made into a Qt5 library that can
be used in other applications with a command-line application for use as a
standalone generator.
 
%prep
%autosetup -p1
 
%build
%qmake_qt5 PREFIX=%{_prefix} QtIdenticon.pro
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
 
%files
%doc README.md
%license LICENSE
%{_qt5_plugindir}/libqtjdenticon.so
