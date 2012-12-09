# revision 22257
# category Package
# catalog-ctan /macros/latex/contrib/paresse
# catalog-date 2011-04-20 18:25:54 +0200
# catalog-license lppl
# catalog-version 4
Name:		texlive-paresse
Version:	4
Release:	2
Summary:	Defines simple macros for greek letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paresse
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paresse.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paresse.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paresse.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines macros using SS to type greek letters so that the user
may (for example) type SSa to get the effect of $\alpha$.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/paresse/paresse.sty
%{_texmfdistdir}/tex/latex/paresse/paresseold.sto
%{_texmfdistdir}/tex/latex/paresse/paresseutf8.sto
%doc %{_texmfdistdir}/doc/latex/paresse/paresse-en.pdf
%doc %{_texmfdistdir}/doc/latex/paresse/paresse-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/paresse/paresse-ex-fr.pdf
%doc %{_texmfdistdir}/doc/latex/paresse/paresse-fr.pdf
%doc %{_texmfdistdir}/doc/latex/paresse/paresse.pdf
#- source
%doc %{_texmfdistdir}/source/latex/paresse/LISEZMOI
%doc %{_texmfdistdir}/source/latex/paresse/Makefile
%doc %{_texmfdistdir}/source/latex/paresse/README
%doc %{_texmfdistdir}/source/latex/paresse/paresse-TEST.zip
%doc %{_texmfdistdir}/source/latex/paresse/paresse-doc.dtx
%doc %{_texmfdistdir}/source/latex/paresse/paresse.dtx
%doc %{_texmfdistdir}/source/latex/paresse/paresse.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4-2
+ Revision: 754645
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4-1
+ Revision: 719196
- texlive-paresse
- texlive-paresse
- texlive-paresse
- texlive-paresse

