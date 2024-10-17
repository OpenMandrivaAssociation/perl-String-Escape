%define upstream_name    String-Escape
%define upstream_version 2010.002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Registry of string functions, including backslash escapes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a flexible calling interface to some
frequently-performed string conversion functions, including applying and
removing C/Unix-style backslash escapes like \n and \t, wrapping and
removing double-quotes, and truncating to fit within a desired length.

Furthermore, the escape() function provides for dynamic selection of
operations by using a package hash variable to map escape specification
strings to the functions which implement them. The lookup imposes a bit
of a performance penalty, but allows for some useful late-binding
behaviour. Compound specifications (ex. 'quoted uppercase') are expanded
to a list of functions to be applied in order. Other modules may also
register their functions here for later general use. (See the "CALLING
BY NAME" section below for more.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2010.2.0-2mdv2011.0
+ Revision: 655218
- rebuild for updated spec-helper

* Tue Feb 02 2010 Jérôme Quelin <jquelin@mandriva.org> 2010.2.0-1mdv2011.0
+ Revision: 499485
- update to 2010.002

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2002.1.0-2mdv2010.0
+ Revision: 430545
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2002.001-5mdv2009.0
+ Revision: 258391
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2002.001-4mdv2009.0
+ Revision: 246476
- rebuild

* Wed Feb 06 2008 Jérôme Quelin <jquelin@mandriva.org> 2002.001-2mdv2008.1
+ Revision: 163073
- wrapping description to fit in 80 columns

* Wed Feb 06 2008 Jérôme Quelin <jquelin@mandriva.org> 2002.001-1mdv2008.1
+ Revision: 163043
- import perl-String-Escape


