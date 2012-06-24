Summary:	Line editor
Summary(pl):	Edytor liniowy
Name:		ledit
Version:	1.11
Release:	1
License:	GPL
Group:		Base
Source0:	http://caml.inria.fr/distrib/bazar-ocaml/%{name}.tar.gz
# Source0-md5:	a2d38ba641682509c1e964ad699a9dd2
Patch0:		%{name}-ocaml3.09.patch
URL:		http://www.inria.fr/~ddr/
BuildRequires:	ncurses-devel
BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
Program ledit allows to edit lines one by one when running an
interactive command. When typing a line, some keys with control or
meta are interpreted: it is possible to insert characters in the
middle of the line, go to the beginning or the end of the line, get a
previous line, search for a line with a pattern, etc.

%description -l pl
Program ledit pozwala modyfikowa� linie tekstu wprowadzane w innym
interaktywnym programie. Pozwala na wprowadzanie znak�w w �rodku
linii, przej�cie na jej pocz�tek lub koniec, wyszukiwanie linii
spe�niaj�cej jaki� wz�r, wybranie poprzedniej linii, itd.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ledit.out $RPM_BUILD_ROOT%{_bindir}/ledit
install ledit.l $RPM_BUILD_ROOT%{_mandir}/man1/ledit.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
