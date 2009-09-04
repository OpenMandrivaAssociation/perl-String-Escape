%define upstream_name    String-Escape
%define upstream_version 2002.001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Registry of string functions, including backslash escapes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*
