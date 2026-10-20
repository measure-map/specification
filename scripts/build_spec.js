// Regenerates the schema documentation in specification.md from the schema files.
// Everything above the first generated heading ("### Measure") is kept as written.
const fs = require("fs");
const path = require("path");
const { JSONSchemaMarkdown } = require("json-schema-md-doc");

const root = path.join(__dirname, "..");
const specPath = path.join(root, "specification.md");
const schemas = ["measure.schema.json", "measuremap.schema.json"];
const firstGeneratedHeading = "### Measure\n";
const footer = /\n*_Generated with \[json-schema-md-doc\]\([^)]*\)_\s*$/;

const spec = fs.readFileSync(specPath, "utf8").replace(/\r\n/g, "\n");
const start = spec.indexOf(firstGeneratedHeading);
if (start < 0) throw new Error(`'${firstGeneratedHeading.trim()}' not found in specification.md`);

const sections = schemas.map((file) => {
  const doccer = new JSONSchemaMarkdown();
  doccer.load(JSON.parse(fs.readFileSync(path.join(root, file), "utf8")));
  return doccer.generate().replace(/^# /, "### ").replace(footer, "\n");
});

fs.writeFileSync(specPath, spec.slice(0, start) + sections.join("\n"));
