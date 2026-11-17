# Successful Jenkins build evidence

The final pipeline passed on both Windows and Linux in
[GitHub Actions run #2](https://github.com/NatalioH/Natalio_Hassoun_Lab10/actions/runs/44186545389),
at source commit `25a1a6699a0c2b7d3c6d0857a6c92b38a6fbb6e7`.

| Platform | Complete archived evidence |
| --- | --- |
| Windows | [Jenkins_Windows_Evidence.zip](Jenkins_Windows_Evidence.zip) |
| Linux | [Jenkins_Linux_Evidence.zip](Jenkins_Linux_Evidence.zip) |

Each archive contains the actual Jenkins console log, build metadata, JUnit
test results, coverage XML and HTML, Bandit JSON, and deployment output and
checksum manifest. Both builds finished with `SUCCESS`, four passing tests,
100% application statement and branch coverage, and zero Bandit findings.

[Cross_Platform_Build_Summary.json](Cross_Platform_Build_Summary.json) provides
a compact index. The same evidence is included in the root submission ZIP.

`Jenkins_Console_Output.txt` and `build-summary.json` at this directory's root
record the earlier isolated Linux validation. They are retained as historical
evidence. Use the two platform archives above for the final cross-platform
results. These hosted builds do not represent execution on a personal Windows
Jenkins service.
