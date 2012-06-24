Summary:	texinfo formatter and info reader
Summary(de):	texinfo-Formatier- und Leseprogramm
Summary(fr):	Formatteur texinfo et lecteur pour info.
Summary(pl):	Texinfo -- formatter plik�w texinfo
Summary(tr):	texinfo bi�imleyici ve info okuyucu
Name:		texinfo
Version:	3.12f
Release:	5
Copyright:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	info-dir
Source2:	info.wmconfig
Patch0:		texinfo-exe.patch
Patch1:		texinfo-fix.patch
Patch2:		texinfo-alpha-tioc.patch
Patch3:		texinfo-zlib.patch
Patch4:		texinfo-info.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

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
Prereq:		bash
Requires:	%{name} = %{version}

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr \
	--without-included-gettext
make
rm util/install-info
make -C util LIBS=-lz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,sbin}

make install prefix=$RPM_BUILD_ROOT/usr

install util/fix-info-dir $RPM_BUILD_ROOT/sbin

install %{SOURCE1} $RPM_BUILD_ROOT/etc/info-dir
ln -sf ../../etc/info-dir $RPM_BUILD_ROOT/usr/info/dir

mv -f $RPM_BUILD_ROOT/usr/bin/install-info $RPM_BUILD_ROOT/sbin

install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/info

gzip -9nf $RPM_BUILD_ROOT/usr/info/*info* \
	ChangeLog INTRODUCTION NEWS README info/README
%post
/sbin/install-info /usr/info/texinfo.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/texinfo.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,INTRODUCTION,NEWS,README,info/README}.gz
%attr(755,root,root) /usr/bin/*
/usr/info/info-stnd.info*
/usr/info/texinfo*
%lang(cs)    /usr/share/locale/cs/LC_MESSAGES/texinfo.mo
%lang(de)    /usr/share/locale/de/LC_MESSAGES/texinfo.mo
%lang(de_AT) /usr/share/locale/de_AT/LC_MESSAGES/texinfo.mo
%lang(fr)    /usr/share/locale/fr/LC_MESSAGES/texinfo.mo
%lang(nl)    /usr/share/locale/nl/LC_MESSAGES/texinfo.mo
%lang(no)    /usr/share/locale/no/LC_MESSAGES/texinfo.mo
%lang(ru)    /usr/share/locale/ru/LC_MESSAGES/texinfo.mo

%files -n info
%defattr(644,root,root,755)
%config(missingok) /etc/X11/wmconfig/info
%config(noreplace) %verify(not mtime size md5) /etc/info-dir
%config /usr/info/dir
%attr(755,root,root) /usr/bin/info
/usr/info/info.info*
%attr(755,root,root) /sbin/install-info
%attr(755,root,root) /sbin/fix-info-dir

%changelog
* Thu Apr  1 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.12f-5]
- removed man group from man pages,
- more locales (cs , de_AT, nl, no, ru),
- gzipping %doc
- added --without-included-gettext to ./configure parameters (smaler binary)
- added texinfo-info.patch,
- added /sbin/fix-info-dir.

* Fri Oct  9 1998 Ziemek Borowski <ziembor@faq-bot.ceu.edu.pl>
  [3.12-5]
- more restricted permision to binaries,
- added texinfo-3.12-fix.patch,
- fixed spec Polish translation. 

* Tue Oct 06 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- added pl translation,
- restricted ELF binaries permissions,
- minor modifications of the spec file.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean
- manhattan build

* Wed Mar 04 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 3.12
- added buildroot

* Sun Nov 09 1997 Donnie Barnes <djb@redhat.com>
- moved /usr/info/dir to /etc/info-dir and made /usr/info/dir a
  symlink to /etc/info-dir.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry for info

* Wed Oct 01 1997 Donnie Barnes <djb@redhat.com>
- stripped /sbin/install-info

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added info-dir to filelist

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- added patch from sopwith to let install-info understand gzip'ed info files
- use skeletal dir file from texinfo tarball (w/ bash entry to reduce
  dependency chain) instead (and install-info command everywhere else)
- patches install-info to handle .gz names correctly

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- patched install-info.c for glibc.
- added /usr/bin/install-info to the filelist

* Tue Feb 18 1997 Michael Fulbright <msf@redhat.com>
- upgraded to version 3.9.
