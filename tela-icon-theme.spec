#
# spec file for package tela-icon-theme
#
# Copyright (c) 2024 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           tela-icon-theme
Version:        1719755616.c1b9a41
Release:        0
Summary:        Tela Icon Theme
License:        GPL-3.0-or-later
Url:            https://github.com/vinceliuice/Tela-icon-theme
Source:         https://github.com/vinceliuice/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gtk3-tools
BuildRequires:  sed
BuildArch:      noarch

%description
A flat, colorful icon theme

%prep
%autosetup

%install
chmod 755 ./install.sh
TELA_DEST_DIR=%{buildroot}%{_datadir}/icons/ ./install.sh
mv AUTHORS CREDITS
mkdir -pv %{buildroot}%{_defaultdocdir}/%{name}
for i in README.md COPYING CREDITS
do
 cp "$i" %{buildroot}%{_defaultdocdir}/%{name}/
done
%fdupes %{buildroot}%{_datadir}/icons/

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore.

%files
%defattr(-,root,root)
%doc COPYING CREDITS README.md
%{_datadir}/icons/*
%dir %{_datadir}/icons

%changelog
