#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Similarity
Summary:	String::Similarity - calculate the similarity of two strings
Summary(pl):	String::Similarity - obliczanie podobieñstwa dwóch ³añcuchów
Name:		perl-String-Similarity
Version:	1
Release:	1
# C files say GPL v2+
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6a57128e7d4365a89b57f243cb50b072
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'similarity'-function calculates the similarity index of its two
arguments. A value of '0' means that the strings are entirely
different. A value of '1' means that the strings are identical.
Everything else lies between 0 and 1 and describes the amount of
similarity between the strings.

%description -l pl
Funkcja similarity oblicza indeks podobieñstwa pomiêdzy dwoma
parametrami. Warto¶æ '0' oznacza, ¿e ³añcuchy s± ca³kowicie ró¿ne.
Warto¶æ '1' oznacza, ¿e s± identyczne. Wszystko inne zawiera siê
miêdzy 0 a 1 i opisuje stopieñ podobieñstwa pomiêdzy ³añcuchami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
