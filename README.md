# SchemaRehearsal

Assess schema change evidence from isolated PostgreSQL rehearsals.

**Status** Local proof of concept. See the [roadmap](ROADMAP.md) for product acceptance criteria and release status.

## Overview

Database and backend teams need evidence on data preservation, lock duration and old-client compatibility before a migration.

## Quickstart

Requires Python 3.11 or later. Use a system Python installation. The core uses only its standard library and reads local files.


```sh
git clone https://github.com/Parsa-Emami/schema-rehearsal.git
cd schema-rehearsal
python3 check.py examples/pass.json
python3 check.py examples/finding.json
python3 -m unittest discover -s tests -v
```

The second command deliberately exits with status 1 and reports `lock_budget_exceeded`.

- [CLI contract and examples](docs/cli.md)
- [Architecture](docs/architecture.md) and [threat model](docs/threat-model.md)
- [Project rules](RULES.md), [roadmap](ROADMAP.md), and [contributing](CONTRIBUTING.md)
- [Security reporting](SECURITY.md) and [license](LICENSE)
