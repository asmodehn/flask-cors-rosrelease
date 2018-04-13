Name:           ros-kinetic-flask-cors
Version:        3.0.3
Release:        2%{?dist}
Summary:        ROS flask_cors package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-flask >= 0.10.1
Requires:       python-six >= 1.5.2
BuildRequires:  python-flask >= 0.10.1
BuildRequires:  python-six >= 1.5.2
BuildRequires:  ros-kinetic-catkin >= 0.6.18
BuildRequires:  ros-kinetic-catkin-pip >= 0.2.0

%description
Cross Origin Resource Sharing ( CORS ) support for Flask

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Apr 13 2018 AlexV <asmodehn@gmail.com> - 3.0.3-2
- Autogenerated by Bloom

* Fri Apr 13 2018 AlexV <asmodehn@gmail.com> - 3.0.3-1
- Autogenerated by Bloom

* Fri Apr 13 2018 AlexV <asmodehn@gmail.com> - 3.0.3-0
- Autogenerated by Bloom

