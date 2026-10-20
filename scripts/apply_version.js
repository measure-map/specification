// Writes the version from version.txt into the $id of both schemas.
// release-please bumps version.txt in its release pull request; the release workflow then runs
// this script, followed by build_spec.js, so that the $ids and specification.md match it.
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const version = fs.readFileSync(path.join(root, "version.txt"), "utf8").trim();
if (!/^\d+\.\d+\.\d+$/.test(version)) throw new Error(`version.txt holds no version: '${version}'`);

for (const file of ["measure.schema.json", "measuremap.schema.json"]) {
  const filePath = path.join(root, file);
  const content = fs.readFileSync(filePath, "utf8");
  const updated = content.replace(
    /("\$id": "https:\/\/measure-map\.github\.io\/specification\/schema\/)[^/]+(\/)/,
    `$1${version}$2`
  );
  if (!updated.includes(`/schema/${version}/${file}"`)) throw new Error(`no $id found in ${file}`);
  fs.writeFileSync(filePath, updated);
}
