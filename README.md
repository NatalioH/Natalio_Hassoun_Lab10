# Lab 10 - Python CI/CD with Jenkins

**Nathalio Hassoun**  
Software Tools Lab - Fall 2026-2027

[![Jenkins validation](https://github.com/NatalioH/Natalio_Hassoun_Lab10/actions/workflows/jenkins-validation.yml/badge.svg)](https://github.com/NatalioH/Natalio_Hassoun_Lab10/actions/workflows/jenkins-validation.yml)

This project uses Jenkins to check Python code style, run unit tests, measure
application coverage, scan production code with Bandit, and deploy a verified
local release. The same Jenkinsfile supports Windows and Linux agents.

## Submission files

| Requirement | File |
| --- | --- |
| Part 3 - repository URL | [GitHub_Submission_Link.txt](GitHub_Submission_Link.txt) |
| Part 4 - modified pipeline | [Jenkinsfile_Nathalio_Hassoun](Jenkinsfile_Nathalio_Hassoun) |
| Part 4 - changes and observed build output | [Lab10_Brief_Report.pdf](Lab10_Brief_Report.pdf) |
| Complete source, report and build evidence | [Lab10_Submission.zip](Lab10_Submission.zip) |

## Verified results

[Successful Windows and Linux Jenkins run #2](https://github.com/NatalioH/Natalio_Hassoun_Lab10/actions/runs/44186545389)
tested source commit `25a1a6699a0c2b7d3c6d0857a6c92b38a6fbb6e7`.
The pipeline and Python source in this submission match that tested revision.
Later changes organize documentation and evidence.

| Check | Windows Jenkins | Linux Jenkins |
| --- | --- | --- |
| Final result | SUCCESS | SUCCESS |
| Unit tests | 4 passed | 4 passed |
| Application statement coverage | 100% | 100% |
| Application branch coverage | 100% | 100% |
| Bandit findings / scan errors | 0 / 0 | 0 / 0 |
| Deployment checksum and smoke test | Passed | Passed |

The workflow starts an actual Jenkins 2.580.2 controller on each GitHub-hosted
runner, using Java 21 and Python 3.12. Jenkins loads and executes the submitted
pipeline from this Git repository. These hosted builds are separate from a
Jenkins service installed on a personal computer.

Full console logs, build metadata and archived reports are preserved in the
[evidence directory](evidence/README.md), the submission ZIP and the linked
run's downloadable artifacts.

## Pipeline stages

| Stage | Action and success condition |
| --- | --- |
| Checkout | Check out the configured Git revision into a clean workspace. |
| Setup | Create `venv`, install the pinned tools and log their versions. |
| Lint | Run flake8 on `app.py`, `deploy.py` and `tests/`; require no violations. |
| Test | Run four pytest tests and generate JUnit XML. |
| Coverage | Measure `app.py` statement and branch coverage; generate console, XML and HTML reports; require at least 90% coverage. |
| Security Scan | Scan `app.py` and `deploy.py` with Bandit; fail on findings or scan errors. |
| Deploy | Copy the application into a persistent release, verify its SHA-256 checksum and check the deployed program's greeting. |

Deployment runs only after the preceding stages pass. Reports are archived
before the workspace is deleted. The release remains at
`<Jenkins workspace>@deployments/<build number>/`, outside the cleaned workspace.
This is a local file deployment, not a continuously running web service.

## Run in Jenkins

Prerequisites: Java 21 for Jenkins, Python 3.10+ with pip and virtual-environment
support, and Git. Python and Git must be available to the account running the
Jenkins agent. Install the Pipeline and Git plugins; SSH Agent is also included
as requested by the lab, although local deployment does not use SSH.

1. Create a **Pipeline** job named `Python-CI-CD`.
2. Select **Pipeline script from SCM**, then **Git**.
3. Set Repository URL to `https://github.com/NatalioH/Natalio_Hassoun_Lab10.git`.
4. Set Branch Specifier to `*/main`.
5. Set Script Path to `Jenkinsfile_Nathalio_Hassoun`.
6. Save and select **Build Now**.
7. Open the build's **Console Output** and archived artifacts.

`PYTHON_COMMAND` defaults to `python`. If needed, use **Build with Parameters**
on subsequent runs and set it to `python3`, `py -3`, or a quoted full Python
executable path. On Windows, the Jenkins service account may not see a Python
installation that is available only to the interactive user. Restart the
service after changing its system PATH.

## Application and tests

Running `app.py` produces:

```text
Hello, World from Nathalio Hassoun!
```

The tests cover the World greeting, another name, the application's command-line
entry point, and the contents, checksum and execution of a deployed release.
The original lab's greeting/test mismatch has been corrected.

Coverage is scoped to the application (`app.py`). Bandit scans application and
deployment code, excluding tests and third-party dependencies. Zero findings
means this scan found no issues; it does not establish complete security.

## Project files

| Path | Purpose |
| --- | --- |
| `app.py` | Personalized greeting application. |
| `deploy.py` | Local release deployment and checksum manifest. |
| `tests/` | Application and deployment tests. |
| `requirements.txt` | Pinned flake8, pytest, coverage.py and Bandit versions. |
| `Jenkinsfile_Nathalio_Hassoun` | Graded Jenkins pipeline. |
| `.github/workflows/jenkins-validation.yml` | Starts Jenkins on Windows/Linux runners and preserves build evidence. |
| `evidence/` | Successful build logs and archived reports. |

