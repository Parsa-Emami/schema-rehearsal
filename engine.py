def evaluate(data, fixture_path):
    lock = data["lock_ms"]
    budget = data["lock_budget_ms"]
    if any(type(value) is not int or value < 0 for value in (lock, budget)):
        raise ValueError("lock timings must be non-negative integers")
    findings = []
    for table, original in sorted(data["before"].items()):
        for column in sorted(set(original) - set(data["after"].get(table, []))):
            findings.append({"code": "column_removed", "table": table, "column": column})
    for table, required in sorted(data["required_by_old_client"].items()):
        for column in sorted(set(required) - set(data["after"].get(table, []))):
            findings.append({"code": "old_client_column_missing", "table": table, "column": column})
    if lock > budget:
        findings.append({"code": "lock_budget_exceeded", "milliseconds": lock, "budget": budget})
    return findings
