%global commit0 218bb4aaf1a1d9fcd89a71a14c8bf99cfd94ba1e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global _vpath_srcdir subprojects/appmenu-glib-translator

%define libname %mklibname appmenu-glib-translator
%define devname %mklibname appmenu-glib-translator -d

Name:           appmenu-glib-translator
Version:        24.05^1.git%{shortcommit0}
Release:        1
Summary:        glib translator portion of the Vala global menu
Group:          System/Libraries
License:        LGPL-3.0-or-later
URL:            https://github.com/rilian-la-te/vala-panel-appmenu/blob/master/subprojects/appmenu-glib-translator
Source:         https://github.com/rilian-la-te/vala-panel-appmenu/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz


BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description

%package -n %{libname}
Summary:    GTK4 related files
Group:      System/Libraries
Provides:   %{libname} = %{EVRD}

%description -n %{libname}

%package -n %{devname}
Summary:  Development files for %{name}
Group:    Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}

%prep
%autosetup -n vala-panel-appmenu-%{commit0} -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license LICENSE
%{_libdir}/girepository-1.0/AppmenuGLibTranslator-24.02.typelib
%{_libdir}/libappmenu-glib-translator.so.0
%{_libdir}/libappmenu-glib-translator.so.24.02

%files -n %{devname}
%{_datadir}/gir-1.0/AppmenuGLibTranslator-24.02.gir
%{_datadir}/vala/vapi/appmenu-glib-translator.deps
%{_datadir}/vala/vapi/appmenu-glib-translator.vapi
%{_includedir}/appmenu-glib-translator/
%{_libdir}/libappmenu-glib-translator.so
%{_libdir}/pkgconfig/appmenu-glib-translator.pc




