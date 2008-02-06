
%define realname   String-Escape
%define version    2002.001
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Registry of string functions, including backslash escapes
Source:     http://www.cpan.org/modules/by-module/String/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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



