Summary:	Line editor
Summary(pl.UTF-8):	Edytor liniowy
Name:		ledit
Version:	2.02.1
Release:	2
License:	BSD
Group:		Base
Source0:	http://cristal.inria.fr/~ddr/ledit/distrib/src/%{name}-%{version}.tgz
# Source0-md5:	f8d51a92bfe78d6e5bd5a94a131c96f8
URL:		http://cristal.inria.fr/~ddr/ledit/
BuildRequires:	ncurses-devel
BuildRequires:	ocaml
BuildRequires:	camlp5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program ledit allows to edit lines one by one when running an
interactive command. When typing a line, some keys with control or
meta are interpreted: it is possible to insert characters in the
middle of the line, go to the beginning or the end of the line, get a
previous line, search for a line with a pattern, etc.

%description -l pl.UTF-8
Program ledit pozwala modyfikować linie tekstu wprowadzane w innym
interaktywnym programie. Pozwala na wprowadzanie znaków w środku
linii, przejście na jej początek lub koniec, wyszukiwanie linii
spełniającej jakiś wzór, wybranie poprzedniej linii, itd.

%prep
%setup -q

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/skel}

install ledit.out $RPM_BUILD_ROOT%{_bindir}/ledit
install -p ledit.1 $RPM_BUILD_ROOT%{_mandir}/man1/ledit.1
install -p leditrc $RPM_BUILD_ROOT/etc/skel/.leditrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
/etc/skel/.leditrc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
