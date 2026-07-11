%global tl_name hyphen-latin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Latin hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/lahyph.tex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-latin.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Latin in T1/EC and UTF-8 encodings, mainly in
modern spelling (u when u is needed and v when v is needed), medieval
spelling with the ligatures \ae and \oe and the (uncial) lowercase 'v'
written as a 'u' is also supported. Apparently there is no conflict
between the patterns of modern Latin and those of medieval Latin.
Hyphenation patterns for the Classical Latin in T1/EC and UTF-8
encodings. Classical Latin hyphenation patterns are different from those
of 'plain' Latin, the latter being more adapted to modern Latin.
Hyphenation patterns for the Liturgical Latin in T1/EC and UTF-8
encodings.

