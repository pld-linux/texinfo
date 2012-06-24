Summary:	Tools needed to create Texinfo format documentation files
Summary(de):	Tools zum Erstellen von texinfo-Dokumentationsdateien
Summary(es):	Formateador texinfo y lector de archivos info
Summary(fr):	Outils cr�ant des documentations au format texinfo
Summary(pl):	Narz�dzia potrzebne przy tworzeniu dokumentacji w formacie texinfo
Summary(pt_BR):	Formatador texinfo e leitor de arquivos info
Summary(ru):	����������� ��� �������� ������ ������������ ������� Texinfo
Summary(tr):	texinfo bi�imleyici ve info okuyucu
Summary(uk):	����������� ��� ��������� ���̦� ���������æ� ������� Texinfo
Name:		texinfo
Version:	4.7
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.gnu.org/gnu/texinfo/%{name}-%{version}.tar.bz2
# Source0-md5:	c2fa2ef957f0d728f821ae9b2362ef4e
Source1:	info.desktop
Patch0:		%{name}-fix.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-pl.po-update.patch
URL:		http://texinfo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.8
BuildRequires:	gettext-devel
BuildRequires:	gettext-autopoint >= 0.14.1
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	sed >= 4.0
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

%description -l de
Texinfo ist ein Dokumentationssystem, das sowohl Online-Information
und gedruckte Ausgabe von einer einzigen Source-Datei erzeugen kann.
Normalerweise w�rden Sie zwei verschiedene Dokumente schreiben, eins
f�r Onlinehilfe und eins f�r ein gedrucktes Handbuch. Mit Texinfo
reicht es, ein Dokument zu schreiben (und sp�ter zu aktualisieren).
Das GNU-Projekt benutzt texinfo f�r den gr��ten Teil seiner
Dokumentation.

%description -l es
Texinfo es un sistema de documentaci�n que puede producir tanto,
informaci�n online como salida impresa a partir de un �nico archivo
fuente. Generalmente, ten�a que escribir dos documentos por separado:
uno para la ayuda u otro tipo de informaci�n online, y otro para un
manual u otro tipo de trabajos impresos. Usando Texinfo, basta con
escribir un �nico documento fuente. El d�a que sea necesaria una
revisi�n del trabajo, s�lo tendr� que revisar un �nico documento. El
Proyecto GNU usa el formato de archivo Texinfo para la mayor�a de su
documentaci�n.

Instale Texinfo si quiere un sistema de documentaci�n para producir
tanto documentaci�n online como impresa a partir del mismo archivo
fuente y si va a escribir documentaci�n para el Proyecto GNU.

%description -l fr
Texinfo est un syst�me de documentation capable de produire de la
documentation online ou imprim�e � partir d'un seul fichier.
Habituellement, il faut �crire deux documents : l'un orient�
hypertexte, l'autre ax� sur une pr�sentation de type PAO. En utilisant
texinfo, vous n'avez plus besoin que d'un seul fichier source. Le
projet GNU utilie le format de fichier Texinfo pour la plupart de ses
documentations.

%description -l pl
Texinfo jest systemem dokumentowania umo�liwiaj�cym wyprodukowanie
zar�wno dokumentacji online jak i w postaci do wydruku z pojedynczego
pliku �r�d�owego. Bardzo cz�sto pisze si� dwie dokumentacje: jedn� do
przegl�dania online i drug� do przyszykowania wysokiej jako�ci postaci
drukowanej. U�ywaj�c Texinfo do powy�szego potrzebujesz przygotowa�
dokumentacj� tylko w jednej postaci �r�d�owej. Podczas modyfikacji
dokumentacji modyfikujesz w takim razie tylko jeden dokument.
Wi�kszo�� projekt�w GNU u�ywa do dokumentowania formatu Texinfo.

%description -l pt_BR
O texinfo � um sistema de documenta��o que pode produzir tanto
informa��o on-line como sa�da impressa a partir de um �nico
arquivo-fonte. Geralmente, voc� teria que escrever dois documentos
separados: um para ajuda on-line ou outro tipo de informa��o on-line,
e outro para um manual ou outro tipo de trabalho impresso. Usando o
Texinfo, basta escrever um �nico documento-fonte. Quando houver
necessidade de revis�o, � preciso apenas revisar um �nico
documento-fonte. O projeto GNU usa o formato de arquivo texinfo para a
maioria da sua documenta��o.

%description -l ru
������ GNU ���������� ������ texinfo ��� ����������� ������������,
��������� � ��� ������. ���� ����� �������� �����������, �����������
��� �������� ������ .info �� �������� ������ .texinfo � ��������� �
emacs ��� ���� ���� ������������.

%description -l tr
[6~GNU projesi, belgelemesinin b�y�k b�l�m�nde texinfo dosyalar�n�
kullan�r. Bu paket, texinfo dosyalar�ndan info dosyalar�n�n
t�retilmesini sa�layan ara�larla birlikte, t�m bu ara�lar i�in bir
emacs aray�z� de sunar.

%description -l uk
������ GNU ����������դ ������ texinfo ��� ¦�����Ԧ ���������æ�,
�������ϧ � ���� ������. ��� ����� ͦ����� �����������, ���Ҧ�Φ ���
��������� ���̦� .info � �Ȧ���� ���̦� .texinfo �� ��������� �� emacs
��� �Ӧ� ��� ���������Ԧ�.

%package -n info
Summary:	A stand-alone TTY-based reader for GNU texinfo documentation
Summary(de):	Ein TTY-basiertes Leseprogramm f�r GNU info-Dokumentation
Summary(es):	Lector basado en tty para documentos texinfo GNU
Summary(fr):	un lecteur de documentations info
Summary(pl):	Samodzielny, terminalowy czytnik dokument�w GNU texinfo
Summary(pt_BR):	Leitor baseado em tty para documentos texinfo GNU
Summary(ru):	��������� ��� ��������� ���������� � ������� GNU texinfo �� ��������� �������
Summary(tr):	GNU texinfo belgeleri i�in tty tabanl� g�r�nt�leyici
Summary(uk):	�������� ��� ��������� �������Ԧ� � �����Ԧ GNU texinfo �� ���������� ���ͦ��̦
Group:		Applications/System
PreReq:		fix-info-dir
Obsoletes:	info-install

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. This package includes a standalone browser program to
view these files.

%description -n info -l de
Das GNU-Projekt benutzt das texinfo-Dateiformat f�r den Gro�teil
seiner Dokumentation. Dieses Paket enth�lt ein selbst�ndiges
Browser-Programm zum Einsehen dieser Dateien.

%description -n info -l fr
Le projet GNU utilise le format de fichier texinfo pour la plupart de
sa documentation. Ce paquetage contient un navigateur pour visualiser
ces fichiers.

%description -n info -l pl
Projekty GNU u�ywaj� formatu texinfo do tworzenia dokumentacji. Pakiet
ten zawiera samodzieln� przegl�dark� tych�e plik�w.

%description -n info -l pt_BR
O projeto GNU usa o formato de arquivos texinfo para a maioria de sua
documenta��o. Este pacote inclui um browser para visualiza��o destes
arquivos.

%description -n info -l ru
������ GNU ���������� ������ texinfo ��� ����������� ������������,
��������� � ��� ������. ���� ����� �������� ��������� ��� ���������
���������� � ������� GNU texinfo �� ��������� �������.

%description -n info -l tr
Bu pakette, info bi�imindeki dosyalar� okumak i�in bir g�r�nt�leyici
bulunur.

%description -n info -l uk
������ GNU ����������դ ������ texinfo ��� ¦�����Ԧ ���������æ�,
�������ϧ � ���� ������. ��� ����� ͦ����� �������� ��� ���������
�������Ԧ� � �����Ԧ GNU texinfo �� ���������� ���ͦ��̦.

%package texi2dvi
Summary:	Texinfo to dvi conversion tool
Summary(pl):	Narz�dzie do konwersji texinfo na dvi
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}
Requires:	tetex

%description texi2dvi
Texinfo to dvi conversion tool.

%description texi2dvi -l pl
Narz�dzie do konwersji plik�w texinfo na dvi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# nb was added but outdated no not removed
sed -i -e '/^no$/d' po/LINGUAS

rm -f po/stamp-po

%build
%{__autopoint}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_sbindir},/sbin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{_sbindir}/install-info $RPM_BUILD_ROOT/sbin/install-info

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

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
%doc AUTHORS ChangeLog INTRODUCTION NEWS README TODO
%attr(755,root,root) %{_bindir}/makeinfo
%attr(755,root,root) %{_bindir}/texindex
%{_datadir}/texinfo

%{_infodir}/texinfo*
%{_mandir}/man1/makeinfo.1*
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
%attr(755,root,root) %{_bindir}/texi2dvi
%{_mandir}/man1/texi2dvi.1*
