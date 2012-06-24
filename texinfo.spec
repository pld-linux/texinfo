Summary:	Tools needed to create Texinfo format documentation files
Summary(de):	Tools zum Erstellen von texinfo-Dokumentationsdateien
Summary(fr):	Outils cr�ant des documentations au format texinfo
Summary(pl):	Narz�dzia potrzebne przy tworzeniu dokumentacji w formacie texinfo
Summary(tr):	texinfo bi�imleyici ve info okuyucu
Name:		texinfo
Version:	4.0
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
BuildRequires:	ncurses-devel
Prereq:		/usr/sbin/fix-info-dir
Requires:	info = %{version}
Requires:	mktemp
Buildroot:	/tmp/%{name}-%{version}-root

%description
Texinfo is a documentation system that can produce both online information
and printed output from a single source file. Normally, you'd have to write
two separate documents: one for online help or other online information and
the other for a typeset manual or other printed work. Using Texinfo, you
only need to write one source document. Then when the work needs revision,
you only have to revise one source document. The GNU Project uses the
Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both online
and print documentation from the same source file and/or if you are going to
write documentation for the GNU Project.

%description -l de
Texinfo ist ein Dokumentationssystem, das sowohl Online-Information und
gedruckte Ausgabe von einer einzigen Source-Datei erzeugen kann.
Normalerweise w�rden Sie zwei verschiedene Dokumente schreiben, eins f�r
Onlinehilfe und eins f�r ein gedrucktes Handbuch. Mit Texinfo reicht es, ein
Dokument zu schreiben (und sp�ter zu aktualisieren). Das GNU-Projekt benutzt
texinfo f�r den gr��ten Teil seiner Dokumentation.

Installieren Sie texinfo, wenn Sie ein Dokumentationssystem f�r Online- und
gedruckte Dokumentation brauchen, oder wenn Sie Dokumentationen f�r das
GNU-Projekt schreiben wollen.

%description -l fr
Texinfo est un syst�me de documentation capable de produire de la
documentation online ou imprim�e � partir d'un seul fichier. 
Habituellement, il faut �crire deux documents : l'un orient� hypertexte,
l'autre ax� sur une pr�sentation de type PAO. En utilisant texinfo, vous
n'avez plus besoin que d'un seul fichier source. Le projet GNU utilie le
format de fichier Texinfo pour la plupart de ses documentations.

Vous devriez installer texinfo si vous compter �crire des documents en ligne
et sur papier � partir du m�me fichier ou si vous d�sirez �crire une
documentation pour le projet GNU.

%description -l pl
Texinfo jest systemem dokumentowania umo�liwiaj�cym wyprodukowanie zar�wno
dokumentacji online jak i postaci do wydruku z pojedynczego pliku
�r�d�owego. bardzo cz�sto pisz� siedwie dokumentacje: jedna do przegl�dania
online i inna do przyszykowanai wysokiej jako�ci postaci drukowane. U�ywaj�c
Texinfo do powy�szego potzrebujesz przygotowa� dokumentacj� tylko w jednej
postaci �r�d�owej. Podczas modyfikacji dokumentacji modyfikujesz w takim
razie tylko jeden dokument. Wi�kszo�� projekt�w GNU u�ywa do dukumentowania
formatu Texinfo.

Zainstaluj Texinfo je�eli potzrebujesz sporz�dza� dokumentacj� kt�ra b�dzie
przegl�dana zar�wno online jak i b�dzie drukowan lub je�eli zamierzasz pisa�
dokumentacj� do projekt�w GNU.

%description -l tr
GNU projesi, belgelemesinin b�y�k b�l�m�nde texinfo dosyalar�n� kullan�r.
Bu paket, texinfo dosyalar�ndan info dosyalar�n�n t�retilmesini sa�layan
ara�larla birlikte, t�m bu ara�lar i�in bir emacs aray�z� de sunar.

%package -n info
Summary:	A stand-alone TTY-based reader for GNU texinfo documentation.
Summary(de):	Ein TTY-basiertes Leseprogramm f�r GNU info-Dokumentation.
Summary(fr):	un lecteur de documentations info
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
make -C doc distclean-aminfo
make
rm util/install-info
make -C util 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/X11R6/share/applnk/Utilities,%{_sbindir},/sbin}

make install DESTDIR=$RPM_BUILD_ROOT

install util/fix-info-dir $RPM_BUILD_ROOT%{_sbindir}

mv -f $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT%{_sbindir}
ln -s %{_sbindir}/install-info $RPM_BUILD_ROOT/sbin/install-info

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Utilities

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man?/*} \
	ChangeLog INTRODUCTION NEWS README info/README

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
touch $RPM_BUILD_ROOT%{_infodir}/dir

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
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texindex.1*
%{_mandir}/man5/texinfo.5*

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

%{_mandir}/man1/info.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*
