Name:		texlive-hyphen-latin
Version:	20190406
Release:	1
Summary:	Latin hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/lahyph.tex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-latin.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Latin in T1/EC and UTF-8 encodings,
mainly in modern spelling (u when u is needed and v when v is
needed), medieval spelling with the ligatures \ae and \oe and
the (uncial) lowercase 'v' written as a 'u' is also supported.
Apparently there is no conflict between the patterns of modern
Latin and those of medieval Latin.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-latin
%_texmf_language_def_d/hyphen-latin
%_texmf_language_lua_d/hyphen-latin

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-latin <<EOF
\%% from hyphen-latin:
latin loadhyph-la.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-latin
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-latin <<EOF
\%% from hyphen-latin:
\addlanguage{latin}{loadhyph-la.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-latin
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-latin <<EOF
-- from hyphen-latin:
	['latin'] = {
		loader = 'loadhyph-la.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-la.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1-4
+ Revision: 804803
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1-3
+ Revision: 767566
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1-2
+ Revision: 759926
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1-1
+ Revision: 718668
- texlive-hyphen-latin
- texlive-hyphen-latin
- texlive-hyphen-latin
- texlive-hyphen-latin

