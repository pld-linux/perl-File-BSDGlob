%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	BSDGlob
Summary:	File::BSDGlob perl module
Summary(pl):	Modu� perla File::BSDGlob
Name:		perl-File-BSDGlob
Version:	0.94
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::BSDGlob - Perl extension for BSD glob routine.

%description -l pl
File::BSDGlob - rozszerzenie perla dla rutyny BSD glob.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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