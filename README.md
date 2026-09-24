# Vulnerable Requests Happy-Path Fixture

Controlled public test fixture for the Autonomous Vulnerability Remediation Agent.

The repository intentionally pins a known vulnerable Requests version so the agent can:

1. detect the dependency vulnerability using OSV,
2. upgrade to a fixed version,
3. execute the tests inside an isolated virtual environment,
4. verify that the application still works,
5. re-query OSV to verify remediation.

This repository is intentionally small and is used only for evaluation/testing.
