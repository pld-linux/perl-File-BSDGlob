%include	/usr/lib/rpm/macros.perl
Summary:	File-BSDGlob perl module
Summary(pl):	Modu³ perla File-BSDGlob
Name:		perl-File-BSDGlob
Version:	0.94
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-BSDGlob-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-BSDGlob - Perl extension for BSD glob routine.

%description -l pl
File-BSDGlob - rozszerzenie perla dla rutyny BSD glob.

%prep
%setup -q -n File-BSDGlob-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/File/BSDGlob/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/BSDGlob
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitearch}/File/BSDGlob.pm

%dir %{perl_sitearch}/auto/File/BSDGlob
%{perl_sitearch}/auto/File/BSDGlob/.packlist
%{perl_sitearch}/auto/File/BSDGlob/autosplit.ix
%{perl_sitearch}/auto/File/BSDGlob/BSDGlob.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/BSDGlob/BSDGlob.so

%{_mandir}/man3/*
