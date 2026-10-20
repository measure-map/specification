"""Validate the fixtures in tests/valid and tests/invalid against the MeasureMap schema."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from jsonschema import Draft7Validator
from referencing import Registry, Resource

ROOT = Path(__file__).parent.parent
TESTS = Path(__file__).parent
SCHEMA_FILES = ["measure.schema.json", "measuremap.schema.json"]
ID_PATTERN = re.compile(
    r"https://measure-map\.github\.io/specification/schema/(\d+\.\d+\.\d+)/([a-z]+\.schema\.json)"
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


SCHEMAS = {name: load(ROOT / name) for name in SCHEMA_FILES}
# Resolve "$ref"s from the local files rather than from the published URLs.
REGISTRY = Registry().with_resources(
    (schema["$id"], Resource.from_contents(schema)) for schema in SCHEMAS.values()
)
VALIDATOR = Draft7Validator(SCHEMAS["measuremap.schema.json"], registry=REGISTRY)


def fixtures(kind: str) -> list[Path]:
    return sorted((TESTS / kind).glob("*.json"))


@pytest.mark.parametrize("name", SCHEMA_FILES)
def test_schema_is_valid_draft7(name):
    Draft7Validator.check_schema(SCHEMAS[name])


def test_ids_name_their_file_and_share_one_version():
    versions = set()
    for name, schema in SCHEMAS.items():
        match = ID_PATTERN.fullmatch(schema["$id"])
        assert match, f"{name}: unexpected $id {schema['$id']!r}"
        assert match.group(2) == name
        versions.add(match.group(1))
    assert len(versions) == 1, f"schemas disagree on their version: {sorted(versions)}"


def test_ids_match_the_release_version():
    version = (ROOT / "version.txt").read_text(encoding="utf-8").strip()
    assert load(ROOT / ".release-please-manifest.json") == {".": version}
    for name, schema in SCHEMAS.items():
        assert ID_PATTERN.fullmatch(schema["$id"]).group(1) == version, name


@pytest.mark.parametrize("path", fixtures("valid"), ids=lambda p: p.stem)
def test_valid(path):
    errors = [error.message for error in VALIDATOR.iter_errors(load(path))]
    assert not errors


@pytest.mark.parametrize("path", fixtures("invalid"), ids=lambda p: p.stem)
def test_invalid(path):
    assert not VALIDATOR.is_valid(load(path))
