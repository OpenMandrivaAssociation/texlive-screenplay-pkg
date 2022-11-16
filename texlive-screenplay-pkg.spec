Name:		texlive-screenplay-pkg
Version:	44965
Release:	1
Summary:	Package version of the screenplay document class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/screenplay-pkg
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay-pkg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay-pkg.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements the tools of the screenplay document
class in the form of a package so that screenplay fragments can
be included within another document class. For full
documentation of the available commands, please consult the
screenplay class documentation in addition to the included
package documentation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/screenplay-pkg
%doc %{_texmfdistdir}/doc/latex/screenplay-pkg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
