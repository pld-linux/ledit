Summary:	Line editor
Summary(pl):	Edytor liniowy
Name:		ledit
Version:	1.10
Release:	1
License:	GPL
Group:		Base
Group(de):	Gründsätzlich
Group(es):	Base
Group(pl):	Podstawowe
Group(pt_BR):	Base
Source0:	ftp://ftp.inria.fr/INRIA/Projects/cristal/Daniel.de_Rauglaudre/Tools/%{name}.tar.gz
URL:		http://www.inria.fr/~ddr
BuildRequires:	ncurses-devel
BuildRequires:	camlp4
BuildRequires:	ocaml	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
Program ledit allows to edit lines one by one when running an
interactive command. When typing a line, some keys with control or
meta are interpreted: it is possible to insert characters in the
middle of the line, go to the beginning or the end of the line, get a
previous line, search for a line with a pattern, etc.

%description -l pl
Program ledit pozwala edytowaæ linie tekstu wprowadzane w innym
interaktywnym programie. Pozwala na wprowadzanie znaków w ¶rodku
linii, przej¶cie na jej pocz±tek lub koniec, wyszukiwanie linii
spe³niaj±cej jaki¶ wzór, wybranie poprzednije linii, itd.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ledit.out $RPM_BUILD_ROOT%{_bindir}/ledit
install ledit.l $RPM_BUILD_ROOT%{_mandir}/man1/ledit.1

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_mandir}/man1/*
%attr(755, root, root) %{_bindir}/*
