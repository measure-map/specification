# Schema tests

`test_schemas.py` validates every MeasureMap in `valid/` (must pass) and `invalid/` (must fail) against `measuremap.schema.json`. `$ref`s resolve to the local `measure.schema.json`, never to the published URL, so the tests check the working tree. The tests also check that both `$id`s name their own file and carry the same version.

```bash
pip install -r tests/requirements.txt
pytest tests
```

Each fixture tests one rule, named by its file name. Add a fixture when you add or change a constraint.

Some cases are less obvious:

- `valid/integer_valued_float.json`: `1.0` counts as an integer. Since draft-06, JSON Schema treats any number with a zero fractional part as an integer.
- `invalid/next_ids_without_id.json`, `next_counts_without_count.json`: `next` lists only IDs (which requires `ID`) or only counts (which requires `count`).
