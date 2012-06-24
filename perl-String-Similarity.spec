#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Similarity
Summary:	String::Similarity - calculate the similarity of two strings
Summary(pl):	String::Similarity - obliczanie podobie�stwa dw�ch �a�cuch�w
Name:		perl-String-Similarity
Version:	0.02
Release:	3
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'similarity'-function calculates the similarity index of its two
arguments. A value of '0' means that the strings are entirely
different. A value of '1' means that the strings are identical.
Everything else lies between 0 and 1 and describes the amount of
similarity between the strings.

%description -l pl
Funkcja similarity oblicza indeks podobie�stwa pomi�dzy dwoma
parametrami. Warto�� '0' oznacza, �e �a�cuchy s� ca�kowicie r�ne.
Warto�� '1' oznacza, �e s� identyczne. Wszystko inne zawiera si�
mi�dzy 0 a 1 i opisuje stopie� podobie�stwa pomi�dzy �a�cuchami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
