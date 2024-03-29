Summary:	Presentations with pdftex
Summary(pl.UTF-8):	Prezentacje przy użyciu pdftexa
%define		short_name	pdfslide
Name:		tetex-latex-%{short_name}
Version:	0.5
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
# Original source (probably on-fly autogenerated tar):
# http://www.tug.org/cgi-bin/dirarchive/tex-archive/macros/latex/contrib/%{short_name}.tgz
Source0:	http://www.blues.gda.pl/%{short_name}.tgz
# Source0-md5:	77c06d875b825acb6d8f463628b018df
Source1:	http://sarovar.org/download.php/106/%{short_name}-%{version}.sty
# Source1-md5:	81ccc91f65630f01d6ac0e2728e7c5ba
Source2:	http://sarovar.org/download.php/108/manual-%{version}.pdf
# Source2-md5:	4a5ab5ad590ed89b421625763f9654d3
Source3:	http://sarovar.org/download.php/107/manual-%{version}.tex
# Source3-md5:	6c4b69787c136aadcd08a9312b4067e6
URL:		http://sarovar.org/projects/pdfslide/
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-format-pdflatex
Requires:	tetex-latex
Requires:	tetex-pdftex
Obsoletes:	pdfslide
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
Presentations with pdftex.

%description -l pl.UTF-8
Prezentacje przy użyciu pdftexa.

%prep
%setup -q -n %{short_name}
install %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}/%{short_name}.sty
install *.clo $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install meta*.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install mpgraph.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.jpg $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc demo.pdf manual* *.mp *.cfg
%dir %{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}/*.sty
%{_datadir}/texmf/tex/latex/%{short_name}/*.clo
%{_datadir}/texmf/tex/latex/%{short_name}/*.pdf
%{_datadir}/texmf/tex/latex/%{short_name}/*.jpg
