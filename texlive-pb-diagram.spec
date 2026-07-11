%global tl_name pb-diagram
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.0
Release:	%{tl_revision}.1
Summary:	A commutative diagram package using LAMSTeX or Xy-pic fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pb-diagram
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pb-diagram.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A commutative diagram package using LAMSTeX or Xy-pic fonts

