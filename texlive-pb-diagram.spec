# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pb-diagram
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 5.0
Name:		texlive-pb-diagram
Version:	5.0
Release:	5
Summary:	A commutative diagram package using LAMSTeX or Xy-pic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pb-diagram
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.0-2
+ Revision: 754725
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.0-1
+ Revision: 719210
- texlive-pb-diagram
- texlive-pb-diagram
- texlive-pb-diagram
- texlive-pb-diagram

