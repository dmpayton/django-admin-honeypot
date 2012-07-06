import pep8
import sys
import unittest

from coverage import coverage, misc
from distutils import log
from StringIO import StringIO


class SetupTestSuite(unittest.TestSuite):
    """
    Test Suite configuring Django settings and using
    DjangoTestSuiteRunner as test runner.
    Also runs PEP8 and Coverage checks.
    """
    def __init__(self, *args, **kwargs):
        self.configure()
        self.cov = coverage()
        self.cov.start()
        self.packages = self.resolve_packages()

        super(SetupTestSuite, self).__init__(tests=self.build_tests(), \
                *args, **kwargs)

        # Setup testrunner.
        from django.test.simple import DjangoTestSuiteRunner
        self.test_runner = DjangoTestSuiteRunner(
            verbosity=1,
            interactive=True,
            failfast=False
        )
        self.test_runner.setup_test_environment()
        self.old_config = self.test_runner.setup_databases()

    def build_tests(self):
        """
        Build tests for inclusion in suite from resolved packages.
        """
        from django.core.exceptions import ImproperlyConfigured
        from django.db.models import get_app
        from django.test.simple import build_suite

        tests = []
        for package in self.packages:
            try:
                app_name = package.rsplit('.')[-1]
                app = get_app(app_name, emptyOK=True)
                tests.append(build_suite(app))
            except ImproperlyConfigured, e:
                raise
                log.info("Warning: %s" % e)
            except ImportError, e:
                raise
                log.info("Warning: %s" % e)
        return tests

    def configure(self):
        """
        Configures Django settings.
        """
        from django.conf import settings
        from django.utils.importlib import import_module
        try:
            test_settings = import_module('tests.test_settings')
        except ImportError, e:
            log.info('ImportError: Unable to import test settings: %s' % e)
            sys.exit(1)

        setting_attrs = {}
        for attr in dir(test_settings):
            if '__' not in attr:
                setting_attrs[attr] = getattr(test_settings, attr)

        if not settings.configured:
            settings.configure(**setting_attrs)

    def coverage_report(self):
        """
        Outputs Coverage report to screen and coverage.xml.
        """
        verbose = '--quiet' not in sys.argv
        self.cov.stop()
        if verbose:
            log.info("\nCoverage Report:")
            try:
                include = ['%s*' % package for package in self.packages]
                omit = ['*tests*']
                self.cov.report(include=include, omit=omit)
                self.cov.xml_report(include=include, omit=omit)
            except misc.CoverageException, e:
                log.info("Coverage Exception: %s" % e)

    def resolve_packages(self):
        from django.conf import settings
        
        packages = list()
        targets = self.get_target_packages()
        
        for app in settings.INSTALLED_APPS:
            for target in targets:
                if app.startswith(target):
                    packages.append(app)
        return packages
    
    def get_target_packages(self):
        """
        Frame hack to determine packages contained in module for testing.
        We ignore submodules (those containing '.')
        """
        f = sys._getframe()
        while f:
            if 'self' in f.f_locals:
                locals_self = f.f_locals['self']
                py_modules = getattr(locals_self, 'py_modules', None)
                packages = getattr(locals_self, 'packages', None)

                top_packages = []
                if py_modules or packages:
                    if py_modules:
                        for module in py_modules:
                            if '.' not in module:
                                top_packages.append(module)
                    if packages:
                        for package in packages:
                            if '.' not in package:
                                top_packages.append(package)

                    return list(set(top_packages))
            f = f.f_back

    def pep8_report(self):
        """
        Outputs PEP8 report to screen and pep8.txt.
        """
        verbose = '--quiet' not in sys.argv
        if verbose:
            # Hook into stdout.
            old_stdout = sys.stdout
            sys.stdout = mystdout = StringIO()

            # Run Pep8 checks.
            pep8_style = pep8.StyleGuide(ignore=['E2', 'E3', 'E4', 'E501', 'W'])
            pep8_style.check_files([pkg.replace('.', '/') for pkg in self.packages])

            # Restore stdout.
            sys.stdout = old_stdout

            # Save result to pep8.txt.
            result = mystdout.getvalue()
            output = open('pep8.txt', 'w')
            output.write(result)
            output.close()

            # Return Pep8 result
            if result:
                log.info("\nPEP8 Report:")
                log.info(result)

    def run(self, *args, **kwargs):
        """
        Run the test, teardown the environment and generate reports.
        """
        result = super(SetupTestSuite, self).run(*args, **kwargs)
        self.test_runner.teardown_databases(self.old_config)
        self.test_runner.teardown_test_environment()
        self.coverage_report()
        self.pep8_report()
        return result

