%define upstream_name    POE-Component-Client-HTTP
%define upstream_version 0.948

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Non-blocking/parallel web requests engine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Component-Client-HTTP-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Net::HTTP::Methods)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Component::Client::Keepalive)
BuildRequires:	perl(Test::POE::Server::TCP)
BuildRequires:	perl(Socket::GetAddrInfo)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
The HTTPHead filter turns stream data that has the appropriate format
into a HTTP::Response object. In an all-POE world, this would sit on
the other end of a connection as POE::Filter::HTTPD/

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
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/POE


%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.943.0-1mdv2011.0
+ Revision: 672860
- update to new version 0.943

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.895.0-1mdv2011.0
+ Revision: 506243
- update to 0.895

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.894.0-1mdv2010.1
+ Revision: 498984
- update to 0.894

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.893.0-1mdv2010.1
+ Revision: 473722
- update to 0.893

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.892.0-1mdv2010.1
+ Revision: 466754
- update to 0.892
- update to 0.892

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.891.0-1mdv2010.1
+ Revision: 461346
- update to 0.891

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.890.0-1mdv2010.0
+ Revision: 408854
- update to 0.890

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2010.0
+ Revision: 404347
- rebuild using %%perl_convert_version

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.88-1mdv2009.1
+ Revision: 343836
- update to new version 0.88

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.87-1mdv2009.1
+ Revision: 314307
- update to new version 0.87

* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.85-1mdv2009.0
+ Revision: 235606
- update to new version 0.85

* Thu May 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-2mdv2009.0
+ Revision: 212953
- spec and description cleanup

* Thu May 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2009.0
+ Revision: 212936
- update to new version 0.84

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-1mdv2009.0
+ Revision: 196166
- update to new version 0.83

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Jérôme Quelin <jquelin@mandriva.org> 0.82-1mdv2008.1
+ Revision: 108703
- import perl-POE-Component-Client-HTTP



