%define	major	0
%define libname			%mklibname confuse %{major}
%define libname_devel		%mklibname confuse -d
%define libname_devel_static	%mklibname confuse -d -s

Summary:	A library for parsing configuration files in C
Name:		libconfuse
Version:	2.7
Release:	%mkrel 2
License:	ISC
Group:		System/Libraries
URL:		http://www.nongnu.org/confuse/
Source0:	http://bzero.se/confuse/confuse-%{version}.tar.gz
#Patch0:		confuse-2.6-no-Werror.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%package -n	%{libname}
Summary:	A library of functions for parsing configuration files in C
Group:          System/Libraries

%description -n	%{libname}
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

%package -n	%{libname_devel}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	confuse-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}confuse0-devel <= 2.5-2mdv2008.0

%description -n	%{libname_devel}
Development library and header files for the %{name} library


%package -n	%{libname_devel_static}
Summary:	Development files for the %{name} library (static)
Group:		Development/C
Provides:	confuse-static-devel = %{version}
Requires:	%{libname_devel} = %{version}

%description -n	%{libname_devel_static}
Static development library for %{libname}

%prep

%setup -q -n confuse-%{version}
#%patch0 -p1 -b .werror

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -n %{libname} -f confuse.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_libdir}/*.so.%{major}*
%{_mandir}/man3/*

%files -n %{libname_devel}
%defattr(-,root,root)
%doc examples doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

%files -n %{libname_devel_static}
%defattr(-,root,root)
%{_libdir}/*.a
