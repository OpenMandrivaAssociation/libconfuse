%define	major	0
%define libname			%mklibname confuse %{major}
%define libname_devel		%mklibname confuse -d
%define libname_devel_static	%mklibname confuse -d -s

Summary:	A library for parsing configuration files in C
Name:		libconfuse
Version:	2.7
Release:	3
License:	ISC
Group:		System/Libraries
URL:		http://www.nongnu.org/confuse/
Source0:	http://bzero.se/confuse/confuse-%{version}.tar.gz
#Patch0:		confuse-2.6-no-Werror.patch

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
%makeinstall_std

install -d %{buildroot}%{_mandir}/man3
install -m0644 doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/

%find_lang confuse

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
%{_libdir}/pkgconfig/*.pc

%files -n %{libname_devel_static}
%defattr(-,root,root)
%{_libdir}/*.a


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.7-2mdv2011.0
+ Revision: 609737
- rebuild

* Sat Mar 20 2010 Emmanuel Andry <eandry@mandriva.org> 2.7-1mdv2010.1
+ Revision: 525431
- New version 2.7
- drop patch (now useless)

* Sat Sep 12 2009 Thierry Vignaud <tv@mandriva.org> 2.6-6mdv2010.0
+ Revision: 438538
- rebuild

* Tue Mar 17 2009 Emmanuel Andry <eandry@mandriva.org> 2.6-5mdv2009.1
+ Revision: 356580
- protect major

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Feb 15 2008 Anssi Hannula <anssi@mandriva.org> 2.6-3mdv2008.1
+ Revision: 169129
- fix provides of static devel package

* Wed Feb 13 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.6-2mdv2008.1
+ Revision: 167130
- fix obsoletes tag (thanks to Adam Williamson for
  spotting this)

* Wed Feb 13 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.6-1mdv2008.1
+ Revision: 167057
- new upstream version: 2.6
- new license: ISC
- new library policy
- added static-devel subpackage
- added no-Werror.patch, the compilation was failing due to a
  non-important warning
- update descriptions and summaries

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5-2mdv2008.0
+ Revision: 49072
- Import libconfuse



* Mon Jun 26 2006 Oden Eriksson <oeriksson@mandriva.com> 2.5-2mdv2007.0
- rebuild

* Fri May 06 2005 Oden Eriksson <oeriksson@mandriva.com> 2.5-1mdk
- 2.5

* Sat Aug 09 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.1-1mdk
- initial cooker contrib
