# Based on: https://src.fedoraproject.org/rpms/fedora-release/tree/rawhide
Name:           ppos-release
Version:        38
Release:        1
Summary:        Trimmed and optimized fedora-release.

BuildArch:      noarch

License:        GPLv3
URL:            https://github.com/AP-Sensing/ppos-release

Source0:        90-default.preset
Source1:        90-default-user.preset
Source2:        80-workstation.preset
Source3:        org.projectatomic.rpmostree1.rules
Source4:        longer-default-shutdown-timeout.conf

BuildRequires:  systemd-rpm-macros


%description
PPOS release files such as various /etc/ files that define the release
and systemd preset files that determine which services are enabled by default.

%prep

%build

%install
install -Dm0644 %{SOURCE0} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE1} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE2} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

install -Dm0644 %{SOURCE3} -t %{buildroot}%{_datadir}/polkit-1/rules.d/

install -Dm0645 %{SOURCE4} -t %{buildroot}%{_prefix}/lib/systemd/system.conf.d/

%files
%attr(0644,root,root) %{_prefix}/lib/systemd/system-preset/80-workstation.preset
%attr(0644,root,root) %{_prefix}/lib/systemd/system-preset/90-default-user.preset
%attr(0644,root,root) %{_prefix}/lib/systemd/system-preset/90-default.preset

%attr(0644,root,root) %{_prefix}/share/polkit-1/rules.d/org.projectatomic.rpmostree1.rules

%attr(0644,root,root) %{_prefix}/lib/systemd/system.conf.d/longer-default-shutdown-timeout.conf


%changelog
* Fri Sep 01 2023 d-rens <daniel.renschler@apsensing.com> - %{autorelease}
- Trimmed down to ppos' needs.

