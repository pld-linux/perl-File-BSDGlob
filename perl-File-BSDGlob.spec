#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	BSDGlob
Summary:	File::BSDGlob - Perl extension for BSD glob routine
Summary(pl.UTF-8):	File::BSDGlob - rozszerzenie Perla o funkcję BSD glob
Name:		perl-File-BSDGlob
Version:	0.94
Release:	9
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	18e95f120d8096d8c55aaa47c06681bc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::BSDGlob Perl module implements the FreeBSD glob(3) routine,
which is a superset of the POSIX glob() (described in IEEE Std 1003.2
"POSIX.2").

%description -l pl.UTF-8
Moduł Perla File::BSDGlob stanowi implementację funkcji glob(3) z
FreeBSD, która jest nadzbiorem glob() z POSIX-a (opisanej w IEEE Std
1003.2 "POSIX.2").

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/File/BSDGlob.pm
%dir %{perl_vendorarch}/auto/File/BSDGlob
%{perl_vendorarch}/auto/File/BSDGlob/autosplit.ix
%{perl_vendorarch}/auto/File/BSDGlob/BSDGlob.bs
%attr(755,root,root) %{perl_vendorarch}/auto/File/BSDGlob/BSDGlob.so
%{_mandir}/man3/*
