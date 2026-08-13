%global tl_name hyphen-latin
%global tl_revision 79618
%global tl_version 3.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

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


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-latin:
classiclatin loadhyph-la-x-classic.tex
latin loadhyph-la.tex
liturgicallatin loadhyph-la-x-liturgic.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-latin:
\addlanguage{classiclatin}{loadhyph-la-x-classic.tex}{}{2}{2}
\addlanguage{latin}{loadhyph-la.tex}{}{2}{2}
\addlanguage{liturgicallatin}{loadhyph-la-x-liturgic.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-latin:
['classiclatin'] = {
	loader = 'loadhyph-la-x-classic.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-la-x-classic.pat.txt',
},
['latin'] = {
	loader = 'loadhyph-la.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-la.pat.txt',
},
['liturgicallatin'] = {
	loader = 'loadhyph-la-x-liturgic.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-la-x-liturgic.pat.txt',
},
TL_HYPHEN_EOF
