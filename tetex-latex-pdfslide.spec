%define		short_name	pdfslide
%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
Summary:	Presentations with pdftex
Name:		tetex-latex-%{short_name}
Version:	0.5
Release:	0.1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://sarovar.org/download.php/106/%{short_name}-%{version}.sty
# Source0-md5:	81ccc91f65630f01d6ac0e2728e7c5ba
Source1:	http://sarovar.org/download.php/108/manual-%{version}.pdf
# Source1-md5:	4a5ab5ad590ed89b421625763f9654d3
Source2:	http://sarovar.org/download.php/107/manual-%{version}.tex
# Source2-md5:	6c4b69787c136aadcd08a9312b4067e6
Requires:	tetex-latex
Requires:	tetex-pdftex
Requires(post,postun):	/usr/bin/texhash
Obsoletes:	pdfslide
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Presentations with pdftex.

%prep
%setup -q -c -T
install %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}/%{short_name}.sty

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc *.tex *.pdf
%dir %{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}/*.sty
