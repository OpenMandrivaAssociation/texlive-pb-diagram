Name:		texlive-pb-diagram
Version:	15878
Release:	1
Summary:	A commutative diagram package using LAMSTeX or Xy-pic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pb-diagram
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pb-diagram package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pb-diagram/lamsarrow.sty
%{_texmfdistdir}/tex/latex/pb-diagram/pb-diagram.sty
%{_texmfdistdir}/tex/latex/pb-diagram/pb-lams.sty
%{_texmfdistdir}/tex/latex/pb-diagram/pb-xy.sty
%doc %{_texmfdistdir}/doc/latex/pb-diagram/COPYING
%doc %{_texmfdistdir}/doc/latex/pb-diagram/README
%doc %{_texmfdistdir}/doc/latex/pb-diagram/pb-examples.tex
%doc %{_texmfdistdir}/doc/latex/pb-diagram/pb-manual.pdf
%doc %{_texmfdistdir}/doc/latex/pb-diagram/pb-manual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
