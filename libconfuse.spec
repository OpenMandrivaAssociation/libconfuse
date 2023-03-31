%define	major	2
%define	libname	%mklibname confuse %{major}
%define	devname	%mklibname confuse -d

Summary:	A library for parsing configuration files in C
Name:		libconfuse
Version:	3.3
Release:	2
License:	ISC
Group:		System/Libraries
Url:		https://github.com/martinh/libconfuse
Source0:	https://github.com/martinh/libconfuse/releases/download/v%{version}/confuse-%{version}.tar.gz
Conflicts:	%{_lib}confuse0 < 2.7-4

%description
libConfuse is a configuration file parser library, licensed under the terms
of the ISC license, and written in C. It supports sections and (lists of)
values (strings, integers, floats, booleans or other sections), as well as
some other features (such as single/double-quoted strings, environment
variable expansion, functions and nested include statements). It makes it
very easy to add configuration file capability to a program using a simple
API.

The goal of libConfuse is not to be the configuration file parser library
with a gazillion of features. Instead, it aims to be easy to use and quick
to integrate with your code. libConfuse was called libcfg before, but was
changed to not confuse with other similar libraries.

%files -f confuse.lang

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A library of functions for parsing configuration files in C
Group:		System/Libraries
Suggests:	%{name}

%description -n %{libname}
libConfuse is a configuration file parser library, licensed under the terms
of the ISC license, and written in C. It supports sections and (lists of)
values (strings, integers, floats, booleans or other sections), as well as
some other features (such as single/double-quoted strings, environment
variable expansion, functions and nested include statements). It makes it
very easy to add configuration file capability to a program using a simple
API.

The goal of libConfuse is not to be the configuration file parser library
with a gazillion of features. Instead, it aims to be easy to use and quick
to integrate with your code. libConfuse was called libcfg before, but was
changed to not confuse with other similar libraries.

%files -n %{libname}
%{_libdir}/libconfuse.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	confuse-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{_lib}confuse-static-devel < 2.7-4
Conflicts:	%{_lib}confuse0 < 2.7-4

%description -n %{devname}
Development library and header files for the %{name} library

%files -n %{devname}
%{_includedir}/confuse.h
%{_libdir}/libconfuse.so
%{_libdir}/pkgconfig/libconfuse.pc
%{_mandir}/man3/*

#----------------------------------------------------------------------------

%prep
%setup -q -n confuse-%{version}

%build
%configure	--enable-shared

%make

%install
%makeinstall_std

install -d %{buildroot}%{_mandir}/man3
install -m644 doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/
rm -rf %{buildroot}/%{_datadir}/doc/confuse/

%find_lang confuse
