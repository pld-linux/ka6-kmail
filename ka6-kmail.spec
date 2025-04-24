#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmail
Summary:	kmail
Name:		ka6-%{kaname}
Version:	25.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d9e3ac259366711679fa512605a0e70d
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Positioning-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebChannel-devel >= 5.11.1
BuildRequires:	Qt6WebEngine-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.8.0
BuildRequires:	ka6-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka6-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka6-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka6-kldap-devel >= %{kdeappsver}
BuildRequires:	ka6-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka6-kmime-devel >= %{kdeappsver}
BuildRequires:	ka6-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka6-ktnef-devel >= %{kdeappsver}
BuildRequires:	ka6-libgravatar-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka6-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka6-libksieve-devel >= %{kdeappsver}
BuildRequires:	ka6-mailcommon-devel >= %{kdeappsver}
BuildRequires:	ka6-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka6-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka6-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kbookmarks-devel >= %{kframever}
BuildRequires:	kf6-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcontacts-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kguiaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kitemviews-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-kservice-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Obsoletes:	ka5-%{kaname} < %{version}
ExcludeArch:	x32 i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMail is the email component of Kontact, the integrated personal
information manager from KDE.

%description -l pl.UTF-8
KMail jest komponentem poczty Kontaktu, zintegrowanego menadżera
informacji osobistej dla KDE.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
/sbin/ldconfig

%postun
%update_icon_cache hicolor
/sbin/ldconfig

%post data
%update_desktop_database_post

%postun data
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_archivemail_agent
%attr(755,root,root) %{_bindir}/akonadi_followupreminder_agent
%attr(755,root,root) %{_bindir}/akonadi_mailfilter_agent
%attr(755,root,root) %{_bindir}/akonadi_mailmerge_agent
%attr(755,root,root) %{_bindir}/akonadi_sendlater_agent
%attr(755,root,root) %{_bindir}/akonadi_unifiedmailbox_agent
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmail-refresh-settings
%attr(755,root,root) %{_bindir}/ktnef
%attr(755,root,root) %{_libdir}/libkmailprivate.so.*.*
%ghost %{_libdir}/libkmailprivate.so.6
%attr(755,root,root) %{_libdir}/libmailfilteragentprivate.so.*.*
%ghost %{_libdir}/libmailfilteragentprivate.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/kmailpart.so
%dir %{_libdir}/qt6/plugins/pim6/akonadi/config
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/archivemailagentconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/followupreminderagentconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/sendlateragentconfig.so
%dir %{_libdir}/qt6/plugins/pim6/kcms/kmail
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kmail/kcm_kmail_accounts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kmail/kcm_kmail_appearance.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kmail/kcm_kmail_composer.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kmail/kcm_kmail_misc.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kmail/kcm_kmail_plugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kmail/kcm_kmail_security.so
%dir %{_libdir}/qt6/plugins/pim6/kcms/summary
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/summary/kcmkmailsummary.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/summary/kcmkontactsummary.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kontact/kontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kontact/kontact_summaryplugin.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/akonadi/agents/followupreminder.desktop
%{_datadir}/akonadi/agents/mailfilteragent.desktop
%{_datadir}/akonadi/agents/mailmergeagent.desktop
%{_datadir}/akonadi/agents/sendlateragent.desktop
%{_datadir}/akonadi/agents/unifiedmailboxagent.desktop
%{_desktopdir}/kmail_view.desktop
%{_desktopdir}/org.kde.kmail-refresh-settings.desktop
%{_desktopdir}/org.kde.kmail2.desktop
%{_desktopdir}/org.kde.ktnef.desktop
%{_datadir}/config.kcfg/archivemailagentsettings.kcfg
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmail.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
%{_datadir}/dbus-1/services/org.kde.kmail.service
%dir %{_iconsdir}/breeze-dark/16x16
%dir %{_iconsdir}/breeze-dark/16x16/emblems
%dir %{_iconsdir}/breeze-dark/22x22
%dir %{_iconsdir}/breeze-dark/22x22/emblems
%dir %{_iconsdir}/breeze-dark/8x8
%dir %{_iconsdir}/breeze-dark/8x8/emblems
%{_iconsdir}/breeze-dark/*x*/emblems/*.svg
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/emblems/*.svg
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_iconsdir}/hicolor/scalable/apps/kmail.svg
%dir %{_datadir}/kmail2
%dir %{_datadir}/kmail2/pics
%{_datadir}/kmail2/pics/pgp-keys.png
%{_datadir}/knotifications6/akonadi_archivemail_agent.notifyrc
%{_datadir}/knotifications6/akonadi_followupreminder_agent.notifyrc
%{_datadir}/knotifications6/akonadi_mailfilter_agent.notifyrc
%{_datadir}/knotifications6/akonadi_mailmerge_agent.notifyrc
%{_datadir}/knotifications6/akonadi_sendlater_agent.notifyrc
%{_datadir}/knotifications6/kmail2.notifyrc
%{_datadir}/metainfo/org.kde.kmail2.appdata.xml
%{_datadir}/qlogging-categories6/kmail.categories
%{_datadir}/qlogging-categories6/kmail.renamecategories
