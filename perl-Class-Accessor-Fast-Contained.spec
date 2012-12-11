# $Id: perl-Class-Accessor-Fast-Contained.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Oliver Gorwits <oliver,gorwits$oucs,ox,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Fast-Contained

Summary:	Fast accessors with data containment
Name:		perl-Class-Accessor-Fast-Contained
Version:	1.01
Release:	2
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Class-Accessor-Fast-Contained/
Source:		http://www.cpan.org/modules/by-module/Class/Class-Accessor-Fast-Contained-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

BuildArch:	noarch

%description
Fast accessors with data containment.

%prep
%setup -q -n %{real_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
make

%install
make pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec rm {} \;

### Clean up docs
find examples/ -type f -exec chmod a-x {} \;

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Class::Accessor::Fast::Contained.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Accessor/
%dir %{perl_vendorlib}/Class/Accessor/Fast/
%{perl_vendorlib}/Class/Accessor/Fast/Contained.pm



%changelog
* Tue Sep 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.01-1mdv2012.0
+ Revision: 701474
- first mandriva version
- Created package structure for 'perl-Class-Accessor-Fast-Contained'.

