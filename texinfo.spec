Summary:	Tools needed to create Texinfo format documentation files
Summary(de):	Tools zum Erstellen von texinfo-Dokumentationsdateien
Summary(es):	Formateador texinfo y lector de archivos info
Summary(fr):	Outils créant des documentations au format texinfo
Summary(pl):	Narzêdzia potrzebne przy tworzeniu dokumentacji w formacie texinfo
Summary(pt_BR):	Formatador texinfo e leitor de arquivos info
Summary(tr):	texinfo biçimleyici ve info okuyucu
Name:		texinfo
Version:	4.0f
Release:	3
License:	GPL
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikování
Group(da):	Programmer/Udgivelse
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Edición
Group(fr):	Applications/Edition
Group(it):	Applicazioni/Publishing
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥Ñ¥Ö¥ê¥Ã¥·¥ó¥°
Group(no):	Applikasjoner/Publisering
Group(pl):	Aplikacje/Publikowanie
Group(pt):	Aplicações/Publicação
Group(pt_BR):	Aplicações/Editoração
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/éÚÄÁÔÅÌØÓÔ×Ï
Group(sv):	Tillämpningar/Publicering
Source0:	ftp://alpha.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Source1:	info.desktop
Patch0:		%{name}-fix.patch
Patch1:		%{name}-zlib.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-version.texi.patch
Patch4:		%{name}-fileextension.patch
URL:		http://texinfo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	zlib-devel
Requires:	info = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. Normally,
you'd have to write two separate documents: one for online help or
other online information and the other for a typeset manual or other
printed work. Using Texinfo, you only need to write one source
document. Then when the work needs revision, you only have to revise
one source document. The GNU Project uses the Texinfo file format for
most of its documentation.

%description -l de
Texinfo ist ein Dokumentationssystem, das sowohl Online-Information
und gedruckte Ausgabe von einer einzigen Source-Datei erzeugen kann.
Normalerweise würden Sie zwei verschiedene Dokumente schreiben, eins
für Onlinehilfe und eins für ein gedrucktes Handbuch. Mit Texinfo
reicht es, ein Dokument zu schreiben (und später zu aktualisieren).
Das GNU-Projekt benutzt texinfo für den größten Teil seiner
Dokumentation.

%description -l es
Texinfo es un sistema de documentación que puede producir tanto,
información online como salida impresa a partir de un único archivo
fuente. Generalmente, tenía que escribir dos documentos por separado:
uno para la ayuda u otro tipo de información online, y otro para un
manual u otro tipo de trabajos impresos. Usando Texinfo, basta con
escribir un único documento fuente. El día que sea necesaria una
revisión del trabajo, sólo tendrá que revisar un único documento. El
Proyecto GNU usa el formato de archivo Texinfo para la mayoría de su
documentación.

Instale Texinfo si quiere un sistema de documentación para producir
tanto documentación online como impresa a partir del mismo archivo
fuente y si va a escribir documentación para el Proyecto GNU.

%description -l fr
Texinfo est un système de documentation capable de produire de la
documentation online ou imprimée à partir d'un seul fichier.
Habituellement, il faut écrire deux documents : l'un orienté
hypertexte, l'autre axé sur une présentation de type PAO. En utilisant
texinfo, vous n'avez plus besoin que d'un seul fichier source. Le
projet GNU utilie le format de fichier Texinfo pour la plupart de ses
documentations.

%description -l pl
Texinfo jest systemem dokumentowania umo¿liwiaj±cym wyprodukowanie
zarówno dokumentacji online jak i w postaci do wydruku z pojedynczego
pliku ¼ród³owego. Bardzo czêsto pisze siê dwie dokumentacje: jedn± do
przegl±dania online i drug± do przyszykowania wysokiej jako¶ci postaci
drukowanej. U¿ywaj±c Texinfo do powy¿szego potrzebujesz przygotowaæ
dokumentacjê tylko w jednej postaci ¼ród³owej. Podczas modyfikacji
dokumentacji modyfikujesz w takim razie tylko jeden dokument.
Wiêkszo¶æ projektów GNU u¿ywa do dokumentowania formatu Texinfo.

%description -l pt_BR
O texinfo é um sistema de documentação que pode produzir tanto
informação on-line como saída impressa a partir de um único
arquivo-fonte. Geralmente, você teria que escrever dois documentos
separados: um para ajuda on-line ou outro tipo de informação on-line,
e outro para um manual ou outro tipo de trabalho impresso. Usando o
Texinfo, basta escrever um único documento-fonte. Quando houver
necessidade de revisão, é preciso apenas revisar um único
documento-fonte. O projeto GNU usa o formato de arquivo texinfo para a
maioria da sua documentação.

Instale o Texinfo se você quiser um sistema de documentação para
produzir tanto documentação on-line como impressa a partir do mesmo
arquivo-fonte y se for escrever documentação para o Projeto GNU.

%description -l tr
[6~GNU projesi, belgelemesinin büyük bölümünde texinfo dosyalarýný
kullanýr. Bu paket, texinfo dosyalarýndan info dosyalarýnýn
türetilmesini saðlayan araçlarla birlikte, tüm bu araçlar için bir
emacs arayüzü de sunar.

%package -n info
Summary:	A stand-alone TTY-based reader for GNU texinfo documentation
Summary(de):	Ein TTY-basiertes Leseprogramm für GNU info-Dokumentation
Summary(es):	Lector basado en tty para documentos texinfo GNU
Summary(fr):	un lecteur de documentations info
Summary(pl):	Samodzielny, terminalowy czytnik dokumentów GNU texinfo
Summary(pt_BR):	Leitor baseado em tty para documentos texinfo GNU
Summary(tr):	GNU texinfo belgeleri için tty tabanlý görüntüleyici
Group:		Applications/System
Group(cs):	Aplikace/Systém
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/Système
Group(it):	Applicazioni/Sistema
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥·¥¹¥Æ¥à
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	Aplicações/Sistema
Group(pt_BR):	Aplicações/Sistema
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/óÉÓÔÅÍÁ
Group(sv):	Tillämpningar/System
Prereq:		fix-info-dir
Obsoletes:	info-install

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. This package includes a standalone browser program to
view these files.

%description -n info -l de
Das GNU-Projekt benutzt das texinfo-Dateiformat für den Großteil
seiner Dokumentation. Dieses Paket enthält ein selbständiges
Browser-Programm zum Einsehen dieser Dateien.

%description -n info -l fr
Le projet GNU utilise le format de fichier texinfo pour la plupart de
sa documentation. Ce paquetage contient un navigateur pour visualiser
ces fichiers.

%description -n info -l pl
Projekty GNU u¿ywaj± formatu texinfo do tworzenia dokumentacji. Pakiet
ten zawiera samodzieln± przegl±darkê tych¿e plików.

%description -n info -l pt_BR
O projeto GNU usa o formato de arquivos texinfo para a maioria de sua
documentação. Este pacote inclui um browser para visualização destes
arquivos.

%description -n info -l tr
Bu pakette, info biçimindeki dosyalarý okumak için bir görüntüleyici
bulunur.

%package texi2dvi
Summary:	Texinfo to dvi conversion tool
Summary(pl):	Narzêdzie do konwersji texinfo na dvi
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikování
Group(da):	Programmer/Udgivelse
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Edición
Group(fr):	Applications/Edition
Group(it):	Applicazioni/Publishing
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥Ñ¥Ö¥ê¥Ã¥·¥ó¥°
Group(no):	Applikasjoner/Publisering
Group(pl):	Aplikacje/Publikowanie
Group(pt):	Aplicações/Publicação
Group(pt_BR):	Aplicações/Editoração
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/éÚÄÁÔÅÌØÓÔ×Ï
Group(sv):	Tillämpningar/Publicering
Requires:	%{name} = %{version}
Requires:	tetex

%description texi2dvi
Texinfo to dvi conversion tool.

%description texi2dvi -l pl
Narzêdzie do konwersji plików texinfo na dvi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
ln -sf version.texi doc/version2.texi
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--without-included-gettext
%{__make} -C doc distclean-aminfo
%{__make}
rm -f util/install-info
%{__make} -C util 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Help,%{_sbindir},/sbin}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{_sbindir}/install-info $RPM_BUILD_ROOT/sbin/install-info

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Help

gzip -9nf ChangeLog INTRODUCTION NEWS README info/README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post -n info
/usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/makeinfo
%attr(755,root,root) %{_bindir}/texindex
%{_datadir}/texinfo

%{_infodir}/texinfo*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man1/texindex.1*
%{_mandir}/man5/texinfo.5*

%files -n info -f texinfo.lang
%defattr(644,root,root,755)
%doc info/*.gz
%attr(755,root,root) %{_bindir}/info
%attr(755,root,root) %{_bindir}/infokey
%attr(755,root,root) /sbin/install-info
%attr(755,root,root) %{_sbindir}/install-info

%{_applnkdir}/Help/info.desktop

%{_infodir}/info.info*
%{_infodir}/info-stnd.info*

%{_mandir}/man1/info.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*

%files texi2dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texi2dvi
%{_mandir}/man1/texi2dvi.1*
