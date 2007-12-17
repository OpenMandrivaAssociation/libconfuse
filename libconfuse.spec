%define	major	0
%define libname	%mklibname confuse %{major}

Summary:	A library of functions for parsing configuration files in C
Name:		libconfuse
Version:	2.5
Release:	%mkrel 2
License:	LGPL
Group:		System/Libraries
URL:		http://www.nongnu.org/confuse/
Source0:	http://savannah.nongnu.org/download/confuse/confuse-%{version}.tar.gz
Source1:	http://savannah.nongnu.org/download/confuse/confuse-%{version}.tar.gz.sig

%description
libConfuse is a configuration file parser library, licensed under
the terms of the LGPL, and written in C. It supports sections and
(lists of) values (strings, integers, floats, booleans or other
sections), as well as some other features (such as 
single/double-quoted strings, environment variable expansion,
functions and nested include statements).

It makes it very easy to add configuration file capability to a
program using a simple API. The goal of libConfuse is not to be
the configuration file parser library with a gazillion of features.
Instead, it aims to be easy to use and quick to integrate with your
code.

%package -n	%{libname}
Summary:	A library of functions for parsing configuration files in C
Group:          System/Libraries

%description -n	%{libname}
libConfuse is a configuration file parser library, licensed under
the terms of the LGPL, and written in C. It supports sections and
(lists of) values (strings, integers, floats, booleans or other
sections), as well as some other features (such as 
single/double-quoted strings, environment variable expansion,
functions and nested include statements).

It makes it very easy to add configuration file capability to a
program using a simple API. The goal of libConfuse is not to be
the configuration file parser library with a gazillion of features.
Instead, it aims to be easy to use and quick to integrate with your
code.

%package -n	%{libname}-devel
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Provides:	%{libname}-devel = %{version}
Provides:	confuse-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
libConfuse is a configuration file parser library, licensed under
the terms of the LGPL, and written in C. It supports sections and
(lists of) values (strings, integers, floats, booleans or other
sections), as well as some other features (such as 
single/double-quoted strings, environment variable expansion,
functions and nested include statements).

It makes it very easy to add configuration file capability to a
program using a simple API. The goal of libConfuse is not to be
the configuration file parser library with a gazillion of features.
Instead, it aims to be easy to use and quick to integrate with your
code.

%prep

%setup -q -n confuse-%{version}

%build

%configure2_5x \
    --enable-shared \
    --enable-static \
    --disable-rpath

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_mandir}/man3
install -m0644 doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/

%find_lang confuse

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -n %{libname} -f confuse.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_libdir}/*.so.*
%{_mandir}/man3/*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc examples doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
