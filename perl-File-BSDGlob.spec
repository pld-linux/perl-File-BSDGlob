%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	BSDGlob
Summary:	File::BSDGlob perl module
Summary(pl):	Modu³ perla File::BSDGlob
Name:		perl-File-BSDGlob
Version:	0.94
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::BSDGlob - Perl extension for BSD glob routine.

%description -l pl
File::BSDGlob - rozszerzenie perla dla rutyny BSD glob.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/File/BSDGlob.pm
%dir %{perl_sitearch}/auto/File/BSDGlob
%{perl_sitearch}/auto/File/BSDGlob/autosplit.ix
%{perl_sitearch}/auto/File/BSDGlob/BSDGlob.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/BSDGlob/BSDGlob.so
%{_mandir}/man3/*
