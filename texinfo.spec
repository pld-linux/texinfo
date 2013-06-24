%include	/usr/lib/rpm/macros.perl
Summary:	Tools needed to create Texinfo format documentation files
Summary(de.UTF-8):	Tools zum Erstellen von texinfo-Dokumentationsdateien
Summary(es.UTF-8):	Formateador texinfo y lector de archivos info
Summary(fr.UTF-8):	Outils créant des documentations au format texinfo
Summary(pl.UTF-8):	Narzędzia potrzebne przy tworzeniu dokumentacji w formacie texinfo
Summary(pt_BR.UTF-8):	Formatador texinfo e leitor de arquivos info
Summary(ru.UTF-8):	Инструменты для создания файлов документации формата Texinfo
Summary(tr.UTF-8):	texinfo biçimleyici ve info okuyucu
Summary(uk.UTF-8):	Інструменти для створення файлів документації формату Texinfo
Name:		texinfo
Version:	5.1
Release:	1
License:	GPL v3+
Group:		Applications/Publishing
Source0:	http://ftp.gnu.org/gnu/texinfo/%{name}-%{version}.tar.xz
# Source0-md5:	52ee905a3b705020d2a1b6ec36d53ca6
Source1:	info.desktop
Patch0:		%{name}-info.patch
URL:		http://texinfo.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.12
BuildRequires:	gettext-devel >= 0.18.2
BuildRequires:	help2man
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-modules >= 1:5.8.0
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-perlprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	info = %{version}-%{release}
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

%description -l de.UTF-8
Texinfo ist ein Dokumentationssystem, das sowohl Online-Information
und gedruckte Ausgabe von einer einzigen Source-Datei erzeugen kann.
Normalerweise würden Sie zwei verschiedene Dokumente schreiben, eins
für Onlinehilfe und eins für ein gedrucktes Handbuch. Mit Texinfo
reicht es, ein Dokument zu schreiben (und später zu aktualisieren).
Das GNU-Projekt benutzt texinfo für den größten Teil seiner
Dokumentation.

%description -l es.UTF-8
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

%description -l fr.UTF-8
Texinfo est un système de documentation capable de produire de la
documentation online ou imprimée à partir d'un seul fichier.
Habituellement, il faut écrire deux documents : l'un orienté
hypertexte, l'autre axé sur une présentation de type PAO. En utilisant
texinfo, vous n'avez plus besoin que d'un seul fichier source. Le
projet GNU utilie le format de fichier Texinfo pour la plupart de ses
documentations.

%description -l pl.UTF-8
Texinfo jest systemem dokumentowania umożliwiającym wyprodukowanie
zarówno dokumentacji online jak i w postaci do wydruku z pojedynczego
pliku źródłowego. Bardzo często pisze się dwie dokumentacje: jedną do
przeglądania online i drugą do przyszykowania wysokiej jakości postaci
drukowanej. Używając Texinfo do powyższego potrzebujesz przygotować
dokumentację tylko w jednej postaci źródłowej. Podczas modyfikacji
dokumentacji modyfikujesz w takim razie tylko jeden dokument.
Większość projektów GNU używa do dokumentowania formatu Texinfo.

%description -l pt_BR.UTF-8
O texinfo é um sistema de documentação que pode produzir tanto
informação on-line como saída impressa a partir de um único
arquivo-fonte. Geralmente, você teria que escrever dois documentos
separados: um para ajuda on-line ou outro tipo de informação on-line,
e outro para um manual ou outro tipo de trabalho impresso. Usando o
Texinfo, basta escrever um único documento-fonte. Quando houver
necessidade de revisão, é preciso apenas revisar um único
documento-fonte. O projeto GNU usa o formato de arquivo texinfo para a
maioria da sua documentação.

%description -l ru.UTF-8
Проект GNU использует формат texinfo для большинства документации,
созданной в его рамках. Этот пакет включает инструменты, необходимые
для создания файлов .info из исходных файлов .texinfo и интерфейс к
emacs для всех этих инструментов.

%description -l tr.UTF-8
[6~GNU projesi, belgelemesinin büyük bölümünde texinfo dosyalarını
kullanır. Bu paket, texinfo dosyalarından info dosyalarının
türetilmesini sağlayan araçlarla birlikte, tüm bu araçlar için bir
emacs arayüzü de sunar.

%description -l uk.UTF-8
Проект GNU використовує формат texinfo для більшості документації,
створеної в його рамках. Цей пакет містить інструменти, потрібні для
створення файлів .info з вхідних файлів .texinfo та інтерфейс до emacs
для всіх цих інструментів.

%package -n info
Summary:	A stand-alone TTY-based reader for GNU texinfo documentation
Summary(de.UTF-8):	Ein TTY-basiertes Leseprogramm für GNU info-Dokumentation
Summary(es.UTF-8):	Lector basado en tty para documentos texinfo GNU
Summary(fr.UTF-8):	un lecteur de documentations info
Summary(pl.UTF-8):	Samodzielny, terminalowy czytnik dokumentów GNU texinfo
Summary(pt_BR.UTF-8):	Leitor baseado em tty para documentos texinfo GNU
Summary(ru.UTF-8):	Программа для просмотра документов в формате GNU texinfo на текстовой консоли
Summary(tr.UTF-8):	GNU texinfo belgeleri için tty tabanlı görüntüleyici
Summary(uk.UTF-8):	Програма для перегляду документів в форматі GNU texinfo на текстовому терміналі
Group:		Applications/System
Requires:	fix-info-dir
Obsoletes:	info-install

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. This package includes a standalone browser program to
view these files.

%description -n info -l de.UTF-8
Das GNU-Projekt benutzt das texinfo-Dateiformat für den Großteil
seiner Dokumentation. Dieses Paket enthält ein selbständiges
Browser-Programm zum Einsehen dieser Dateien.

%description -n info -l fr.UTF-8
Le projet GNU utilise le format de fichier texinfo pour la plupart de
sa documentation. Ce paquetage contient un navigateur pour visualiser
ces fichiers.

%description -n info -l pl.UTF-8
Projekty GNU używają formatu texinfo do tworzenia dokumentacji. Pakiet
ten zawiera samodzielną przeglądarkę tychże plików.

%description -n info -l pt_BR.UTF-8
O projeto GNU usa o formato de arquivos texinfo para a maioria de sua
documentação. Este pacote inclui um browser para visualização destes
arquivos.

%description -n info -l ru.UTF-8
Проект GNU использует формат texinfo для большинства документации,
созданной в его рамках. Этот пакет включает программу для просмотра
документов в формате GNU texinfo на текстовой консоли.

%description -n info -l tr.UTF-8
Bu pakette, info biçimindeki dosyaları okumak için bir görüntüleyici
bulunur.

%description -n info -l uk.UTF-8
Проект GNU використовує формат texinfo для більшості документації,
створеної в його рамках. Цей пакет містить програму для перегляду
документів в форматі GNU texinfo на текстовому терміналі.

%package texi2dvi
Summary:	Texinfo to dvi conversion tool
Summary(pl.UTF-8):	Narzędzie do konwersji texinfo na dvi
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}
Requires:	texlive
Requires:	texlive-fonts-latex
Requires:	texlive-plain

%description texi2dvi
Texinfo to dvi conversion tool.

%description texi2dvi -l pl.UTF-8
Narzędzie do konwersji plików texinfo na dvi.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I gnulib/m4
%{__autoconf}
%{__automake}
%configure

PATH="$PATH:../util" %{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_sbindir},/sbin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{_sbindir}/install-info $RPM_BUILD_ROOT/sbin/install-info

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{de.us-ascii,de}/LC_MESSAGES/texinfo_document.mo
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{es.us-ascii,es}/LC_MESSAGES/texinfo_document.mo
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{no.us-ascii,nb}/LC_MESSAGES/texinfo_document.mo
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{pt.us-ascii,pt}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{pt_BR.us-ascii,pt_BR}

%find_lang %{name}
%find_lang texinfo_document

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f texinfo_document.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/makeinfo
%attr(755,root,root) %{_bindir}/pod2texi
%attr(755,root,root) %{_bindir}/texi2any
%attr(755,root,root) %{_bindir}/texindex
%{_datadir}/texinfo

%{_infodir}/texinfo*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man1/pod2texi.1*
%{_mandir}/man1/texi2any.1*
%{_mandir}/man1/texindex.1*
%{_mandir}/man5/texinfo.5*

%files -n info -f texinfo.lang
%defattr(644,root,root,755)
%doc info/README
%attr(755,root,root) %{_bindir}/info
%attr(755,root,root) %{_bindir}/infokey
%attr(755,root,root) /sbin/install-info
%attr(755,root,root) %{_sbindir}/install-info

%{_desktopdir}/info.desktop

%{_infodir}/info.info*
%{_infodir}/info-stnd.info*

%{_mandir}/man1/info.1*
%{_mandir}/man1/infokey.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*

%files texi2dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdftexi2dvi
%attr(755,root,root) %{_bindir}/texi2dvi
%attr(755,root,root) %{_bindir}/texi2pdf
%{_mandir}/man1/pdftexi2dvi.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texi2pdf.1*
