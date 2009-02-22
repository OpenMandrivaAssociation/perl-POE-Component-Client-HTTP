%define module  POE-Component-Client-HTTP
%define version 0.88
%define release %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    non-blocking/parallel web requests engine
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.gz
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(Net::HTTP::Methods)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Component::Client::Keepalive)
BuildRequires: perl(Test::POE::Server::TCP)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The HTTPHead filter turns stream data that has the appropriate format
into a HTTP::Response object. In an all-POE world, this would sit on
the other end of a connection as POE::Filter::HTTPD/

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/POE
