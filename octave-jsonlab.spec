%global octpkg jsonlab
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$
%global upstream_version 1.1

Name:           octave-%{octpkg}
Version:        1.1.0
Release:        1%{?dist}
Summary:        JSON/UBJSON encoder and a decoder in the native matlab/octave language
License:        GPLv3+ or BSD
URL:            http://iso2mesh.sourceforge.net/cgi-bin/index.cgi?jsonlab
Source0:        http://downloads.sourceforge.net/iso2mesh/%{octpkg}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave
Requires(post): octave
Requires(postun): octave

%description
JSONlab is a free and open-source implementation of a JSON/UBJSON encoder and
a decoder in the native MATLAB language. It can be used to convert a MATLAB
data structure (array, struct, cell, struct array and cell array) into
JSON/UBJSON formatted string, or decode a JSON/UBJSON file into MATLAB data.
JSONlab supports both MATLAB and GNU Octave (a free MATLAB clone). 

%prep
%autosetup -n %{octpkg}

cp LICENSE_GPLv3.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangq@nmr.mgh.harvard.edu>
Maintainer: Qianqian Fang <fangq@nmr.mgh.harvard.edu>
Description: JSONlab is a free and open-source implementation of a JSON/UBJSON encoder and
 a decoder in the native MATLAB language. It can be used to convert a MATLAB
 data structure (array, struct, cell, struct array and cell array) into
 JSON/UBJSON formatted string, or decode a JSON/UBJSON file into MATLAB data.
 JSONlab supports both MATLAB and GNU Octave (a free MATLAB clone). 
Categories: JSON
EOF

cat > INDEX << EOF
jsonlab >> JSONLab
JSONLab
 jsonopt
 loadjson
 loadubjson
 mergestruct
 savejson
 saveubjson
 struct2jdata
 varargin2struct
EOF

mkdir -p inst/
mv *.m inst/

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE_GPLv3.txt LICENSE_BSD.txt
%doc examples
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-1
- Initial package
