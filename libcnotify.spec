Summary:	Library to support cross-platform C notification functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje powiadomień w C
Name:		libcnotify
Version:	20150101
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libcnotify/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	32e59a8fff5917ee3d62018c5a9f4439
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcnotify/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
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
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425

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
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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
