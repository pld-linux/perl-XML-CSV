#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define pnam	CSV
Summary:	XML::CSV - Perl extension converting CSV files to XML
Summary(pl):	XML::CSV - rozszerzenie Perla do konwersji plik�w CSV do XML-a
Name:		perl-XML-CSV
Version:	0.15
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b53561db36721fb1b1965d82b869d3e7
BuildRequires:	perl-Text-CSV_XS >= 0.21
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module designed for converting CSV files into XML.

%description(pl):
Modu� Perla s�u��cy do konwersji plik�w w formacie CSV do XML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/XML/CSV.pm
%{_mandir}/man3/*
