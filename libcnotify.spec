# m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support cross-platform C notification functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje powiadomień w C
Name:		libcnotify
Version:	20240414
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcnotify/releases
Source0:	https://github.com/libyal/libcnotify/releases/download/%{version}/%{name}-beta-%{version}.tar.gz
# Source0-md5:	a134777257b37356704c64b13cad34a5
URL:		https://github.com/libyal/libcnotify/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcnotify is a library to support cross-platform C notification
functions.

%description -l pl.UTF-8
libcnotify to biblioteka wspierająca wieloplatformowe funkcje
powiadomień w C.

%package devel
Summary:	Header files for libcnotify library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcnotify
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}

%description devel
Header files for libcnotify library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcnotify.

%package static
Summary:	Static libcnotify library
Summary(pl.UTF-8):	Statyczna biblioteka libcnotify
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcnotify library.

%description static -l pl.UTF-8
Statyczna biblioteka libcnotify.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcnotify.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcnotify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcnotify.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcnotify.so
%{_includedir}/libcnotify
%{_includedir}/libcnotify.h
%{_pkgconfigdir}/libcnotify.pc
%{_mandir}/man3/libcnotify.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcnotify.a
