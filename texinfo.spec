Summary:	texinfo formatter and info reader
Summary(de):	texinfo-Formatier- und Leseprogramm
Summary(fr):	Formatteur texinfo et lecteur pour info.
Summary(pl):	Texinfo -- formatter plik�w texinfo
Summary(tr):	texinfo bi�imleyici ve info okuyucu
Name:		texinfo
Version:	3.12s
Release:	1
Copyright:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	info.desktop
Patch1:		texinfo-fix.patch
Patch3:		texinfo-zlib.patch
Patch4:		texinfo-info.patch
Patch5:		texinfo-version.texi.patch
Patch6:		texinfo-DESTDIR.patch
Patch7:		texinfo-fix-info-dir.patch
BuildRequires:	zlib-devel
Prereq:		/sbin/install-info
Requires:	info = %{version}
Requires:	mktemp
Buildroot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc

%description
The GNU project uses the texinfo file format for much of its documentation. 
This package includes the tools necessary to create .info files from .texinfo 
source files, as well as an emacs interface to all these tools.

%description -l de
Das GNU-Projekt verwendet das Dateiformtat 'texinfo' f�r den Gro�teil der
Dokumentation. Dieses Paket enth�lt Tools zum Erstellen von .info-Dateien aus
.texinfo-Quelldateien und eine emacs-Schnittstelle f�r diese Tools.

%description -l fr
Le projet GBU utilise le format de fichier texinfo pour la plupart de sa
documentation. Ce paquetage contient les outils pour cr�er des fichiers .info
� partir des fichiers sources .texinfo, ainsi qu'une interface emacs pour tous
ces outils.

%description -l pl
Projekty GNU u�ywaj� formatu texinfo do tworzenia dokumentacji. W pakiecie 
tym znajduj� si� narz�dzia potrzebne do tworzenia plik�w info ze �r�d�owych 
*.texinfo, a tak�e interface dla GNU Emacs. 

%description -l tr
GNU projesi, belgelemesinin b�y�k b�l�m�nde texinfo dosyalar�n� kullan�r.
Bu paket, texinfo dosyalar�ndan info dosyalar�n�n t�retilmesini sa�layan
ara�larla birlikte, t�m bu ara�lar i�in bir emacs aray�z� de sunar.

%package -n info
Summary:	standalone tty based reader for GNU texinfo documents
Summary(de):	Unabh�ngiges tty-basiertes Leseprogramm f�r GNU-texinfo-Dokumente
Summary(fr):	Lecteur autonome de documents texinfo pour terminal.
Summary(pl):	Samodzielny, bazuj�cy na terminalu czytnik dokument�w GNU texinfo
Summary(tr):	GNU texinfo belgeleri i�in tty tabanl� g�r�nt�leyici
Group:		Utilities/System
Group(pl):	Narz�dzia/System

%description -n info
The GNU project uses the texinfo file format for much of its documentation. 
This package includes a standalone browser program to view these files.

%description -l de -n info
Das GNU-Projekt benutzt das texinfo-Dateiformat f�r den Gro�teil seiner
Dokumentation. Dieses Paket enth�lt ein selbst�ndiges Browser-Programm 
zum Einsehen dieser Dateien. 

%description -l fr -n info
Le projet GNU utilise le format de fichier texinfo pour la plupart de sa
documentation. Ce paquetage contient un navigateur pour visualiser ces
fichiers.

%description -l pl -n info
Projekty GNU u�ywaj� formatu texinfo do tworzenia dokumentacji.
Pakiet ten zawiera samodzieln� przegl�dark� tych�e plik�w.

%description -l tr -n info
Bu pakette, info bi�imindeki dosyalar� okumak i�in bir g�r�nt�leyici
bulunur.

%prep
%setup -q
%patch1 -p1
%patch3 -p1 
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1 

%build
ln -s version.texi doc/version2.texi
automake
gettextize --copy --force
aclocal
autoconf
LDFLAGS="-s -lz"; export LDFLAGS
%configure \
	--without-included-gettext
make
rm util/install-info
make -C util 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/X11R6/share/applnk/Utilities,%{_sbindir}} \
	$RPM_BUILD_ROOT{/sbin,%{_sysconfdir}}

make install DESTDIR=$RPM_BUILD_ROOT

install util/fix-info-dir $RPM_BUILD_ROOT%{_sbindir}

mv -f $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT%{_sbindir}
ln -s %{_sbindir}/install-info $RPM_BUILD_ROOT/sbin/install-info

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Utilities

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*info* \
	ChangeLog INTRODUCTION NEWS README info/README

%find_lang %{name}

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre -n info
if [ -e /usr/info ] && [ ! -L /usr/info ]; then
	cp -af /usr/info %{_infodir} 
fi

%post -n info
if [ -e /usr/info ] && [ ! -L /usr/info ]; then
	rm -rf /usr/info
	ln -sf %{_infodir} /usr/info
fi
if [ -L %{_infodir}/dir ]; then
	rm -f %{_infodir}/dir
fi
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,INTRODUCTION,NEWS,README,info/README}.gz
%attr(755,root,root) %{_bindir}/makeinfo
%attr(755,root,root) %{_bindir}/texi2dvi
%attr(755,root,root) %{_bindir}/texindex

%{_infodir}/texinfo*

%files -n info -f texinfo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/info
%attr(755,root,root) /sbin/install-info
%attr(755,root,root) %{_sbindir}/fix-info-dir
%attr(755,root,root) %{_sbindir}/install-info

/usr/X11R6/share/applnk/Utilities/info.desktop

%ghost %{_infodir}/dir
%{_infodir}/info.info*
%{_infodir}/info-stnd.info*
