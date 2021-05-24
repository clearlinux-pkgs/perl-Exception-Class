#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exception-Class
Version  : 1.45
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Exception-Class-1.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Exception-Class-1.45.tar.gz
Summary  : 'A module that allows you to declare real exception classes in Perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Exception-Class-license = %{version}-%{release}
Requires: perl-Exception-Class-perl = %{version}-%{release}
Requires: perl(Class::Data::Inheritable)
Requires: perl(Devel::StackTrace)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Devel::StackTrace)

%description
# NAME
Exception::Class - A module that allows you to declare real exception classes in Perl

%package dev
Summary: dev components for the perl-Exception-Class package.
Group: Development
Provides: perl-Exception-Class-devel = %{version}-%{release}
Requires: perl-Exception-Class = %{version}-%{release}

%description dev
dev components for the perl-Exception-Class package.


%package license
Summary: license components for the perl-Exception-Class package.
Group: Default

%description license
license components for the perl-Exception-Class package.


%package perl
Summary: perl components for the perl-Exception-Class package.
Group: Default
Requires: perl-Exception-Class = %{version}-%{release}

%description perl
perl components for the perl-Exception-Class package.


%prep
%setup -q -n Exception-Class-1.45
cd %{_builddir}/Exception-Class-1.45

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Exception-Class
cp %{_builddir}/Exception-Class-1.45/LICENSE %{buildroot}/usr/share/package-licenses/perl-Exception-Class/6debd6e696e6ad9179e4842cf2d3934ec887b08e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Exception::Class.3
/usr/share/man/man3/Exception::Class::Base.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Exception-Class/6debd6e696e6ad9179e4842cf2d3934ec887b08e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Exception/Class.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exception/Class/Base.pm
