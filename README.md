# Lab 10 - Python CI/CD with Jenkins

Student: Nathalio Hassoun

Python 3.10+ and Git must be available to the Jenkins service account.
The pipeline supports Windows and Linux agents. It installs its own isolated
virtual environment; Java is only the Jenkins prerequisite.

## Configure the graded job

1. Use this repository: `https://github.com/NatalioH/Natalio_Hassoun_Lab10.git`.
   The pipeline files are at the repository root on `main`.
2. In Jenkins, install Pipeline and Git plugins. The lab also requests SSH
   Agent; it is not used by this local deployment implementation.
3. New Item -> `Python-CI-CD` -> Pipeline.
4. Pipeline definition: **Pipeline script from SCM**; SCM: **Git**.
5. Enter the repository HTTPS URL and the branch `*/main`.
   Add credentials only if the repository is private.
6. Script Path: `Jenkinsfile_Nathalio_Hassoun`.
7. Save -> Build Now. Subsequent runs can use Build with Parameters.
   `PYTHON_COMMAND` defaults to `python`. If Windows cannot find it, set the
   parameter to a quoted full Python executable path, such as
   `"C:\Program Files\Python312\python.exe"`, or `py -3` when the launcher
   is installed for the service account. A Python installation available only
   to your interactive Windows user may not be visible to LocalSystem.
8. Open build number -> Console Output. A successful run ends with
   `Finished: SUCCESS`. Download the archived `reports` artifacts.

Jenkins is already installed as a Windows service, so no WAR launch command
is needed. Restart the Jenkins service if system PATH was changed after it
started. Check `git --version` and `python --version` from a Jenkins job when
troubleshooting service-account PATH access.

## Stage behavior

- Checkout: checks out the repository from SCM into a clean workspace.
- Setup: creates `venv`, installs the pinned tools and logs their versions.
- Lint: flake8 scans application, deployment script and tests.
- Test: pytest runs four tests and writes JUnit XML.
- Coverage: reruns the tests under coverage.py, writes HTML/XML reports,
  measures application statement and branch coverage, and requires >=90%.
- Security Scan: Bandit scans `app.py` and `deploy.py`; findings or scan errors
  fail the build. Test assertions and third-party virtual environment code
  are outside this production-code scan.
- Deploy: copies `app.py` into a build-numbered local release, verifies its
  SHA-256 checksum, writes a manifest and executes the deployed application.
  The output must match the personalized greeting.

Releases persist at `<Jenkins workspace>@deployments/<build number>/`, outside
the workspace. This is a local file deployment, not a continuously running web
service. Workspace cleanup therefore does not delete deployed releases.
Reports are archived before cleanup. Core `deleteDir()` avoids requiring the
Workspace Cleanup plugin.

## Submission evidence

See the accompanying report and evidence directory for the exact environment
and observed results. The included successful isolated Linux Jenkins run verifies
that branch of the Jenkinsfile; it does not demonstrate a run on your Windows
service. Preserve your Windows Console Output too if the instructor requires
evidence from your own installation.

Part 3 submission: `GitHub_Submission_Link.txt` contains this repository URL.

## Automated Jenkins builds

The GitHub Actions workflow starts an actual Jenkins 2.580.2 instance on both
Windows and Linux and executes the submitted Jenkinsfile at the triggering
commit. Each successful job uploads its console log, test, coverage, Bandit
and deployment reports. Check the Actions tab for the latest verified result.
These hosted runs are separate from the student's Windows Jenkins service.
