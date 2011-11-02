Name:		texlive-pb-diagram
Version:	5.0
Release:	1
Summary:	A commutative diagram package using LAMSTeX or Xy-pic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pb-diagram
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive pb-diagram package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}