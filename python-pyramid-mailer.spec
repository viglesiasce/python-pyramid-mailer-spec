%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-pyramid-mailer
Version:        0.13
Release:        0.1%{?dist}
Summary:        Sends emails from a Pyramid project

License:        BSD 
URL:            https://pypi.python.org/pypi/pyramid_mailer
Source0:        https://pypi.python.org/packages/source/p/pyramid_mailer/pyramid_mailer-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-repoze-sendmail


%description
pyramid_mailer is a package for taking the pain out of sending emails
in your Pyramid project.  It is compatible with Python 2.5, 2.6, 2.7,
and 3.2.

This includes:

Wrapping the low-level Python email library with an easy-to-use API, which
includes attachments and mulipart content.  Send emails immediately or
to add to a maildir queue.  Managing email sends inside a transaction,
to prevent emails being sent if your code fails.  Features to help
with unit testing.  pyramid_mailer uses the repoze_sendmail library for
managing email sending and transacton management, and borrows code from
Zed Shaw's Lamson for wrapping email messages.

%prep
%setup -q -n pyramid_mailer-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc README.txt LICENSE.txt
%{python_sitelib}/*


%changelog
* Mon Jan 20 2014 Vic Iglesias <viglesiasce@gmail.com> 0.13-0.1
- Initial release 
