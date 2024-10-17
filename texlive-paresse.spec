Name:		texlive-paresse
Version:	59228
Release:	2
Summary:	Define simple macros for greek letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/paresse
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paresse.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paresse.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paresse.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines macros using SS to type greek letters. so
that the user may (for example) type SSa to get the effect of
$\alpha$.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/paresse
%doc %{_texmfdistdir}/doc/latex/paresse
#- source
%doc %{_texmfdistdir}/source/latex/paresse

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
