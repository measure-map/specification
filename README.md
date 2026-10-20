[![Latest release](https://img.shields.io/github/v/release/measure-map/specification?label=schema)](https://github.com/measure-map/specification/releases/latest)

# Aligning symbolic music with Measure maps

Aligning versions of the same source material has been a persistent challenge in the field of digital libraries for musicology, and a barrier to progress. The growing number of publicly accessible symbolic datasets (of scores, analyses, and more) now increasingly cover multiple versions of the same works. As creators/curators/representatives of many such datasets and encoding standards, we came together in this project to coordinate platform-neutral interoperability for combining and comparing different sources, reliably and automatically. Here, we outline the main challenges and propose solutions centred on the **measure map**: a lightweight format for representing symbolic bar information alone. We offer new code for producing this representation from various formats, diagnosing differences, and even solving for those differences by modifying sources in-place. While we cannot solve for every possible discrepancy, we do provide corpus-scale demonstration; and while we focus on symbolic data, we consider the measure map also a useful basis for aligning audio, manuscripts and any source for which bar-relative location data provides a useful point of reference.

## Reference

[Gotham, M.](https://github.com/MarkGotham), [Hentschel, J.](https://github.com/johentsch), [Couturier, L.](https://github.com/pythouille), Dykeaylen, N., Rohrmeier, M., & [Giraud, M.](https://github.com/magiraud) (2023). The ‘Measure Map’: An inter-operable standard for aligning symbolic music. *Proceedings of the 10th International Conference on Digital Libraries for Musicology*, 91–99. https://doi.org/10.1145/3625135.3625136

Formal specification: https://github.com/measure-map/specification/blob/main/specification.md

## Versioning

The schemas follow [Semantic Versioning](https://semver.org/), applied to the MeasureMaps they accept:

- **MAJOR**: a MeasureMap that was valid becomes invalid, or a field changes its meaning.
- **MINOR**: a backwards-compatible addition, e.g. a new optional field. Every MeasureMap that was valid stays valid. Because the schemas do not accept additional properties, a MeasureMap that uses the addition is rejected by earlier versions.
- **PATCH**: changes to descriptions, examples, or documentation that leave the set of valid MeasureMaps unchanged, and bug fixes that make a schema enforce what its documentation already states.

Every release is published under a fixed URL that never changes, and that URL is the schema's `$id`:

- `https://measure-map.github.io/specification/schema/<version>/measure.schema.json`
- `https://measure-map.github.io/specification/schema/<version>/measuremap.schema.json`

`schema/latest/` holds a copy of the most recent release for convenience; do not use it as an identifier. Changes are listed in [CHANGELOG.md](CHANGELOG.md).

### Releasing

Releases are automated with [release-please](https://github.com/googleapis/release-please). It reads the [Conventional Commits](https://www.conventionalcommits.org/) on `main` to work out the next version:

- `fix:` gives a PATCH release and `feat:` a MINOR release.
- A `!` after the type (`feat!:`, `fix!:`) or a `BREAKING CHANGE:` footer gives a MAJOR release. Use it for every change that makes a valid MeasureMap invalid, except the bug fixes covered by PATCH.
- Other types (`docs:`, `test:`, `ci:`, `chore:`, …) do not trigger a release.

When squash-merging, the pull request title becomes the commit message, so it must follow the same format.

On `main`, `version.txt` and both `$id`s hold the version of the latest release. release-please keeps a release pull request open that bumps `version.txt` and adds the changelog entry. The release workflow then updates the `$id`s and `specification.md` in the same pull request and runs the tests. Merging that pull request tags the release, creates the GitHub Release, and publishes all released versions to GitHub Pages.

## File names and editor support

MeasureMap files use the suffix `.mm.json`, e.g. `317.mm.json`. pyMeasureMap writes this suffix by default.

The schema is registered in the [JSON Schema Store](https://www.schemastore.org/) (entry "MeasureMap" in [`src/api/json/catalog.json`](https://github.com/SchemaStore/schemastore/blob/master/src/api/json/catalog.json), added in [SchemaStore/schemastore#6527](https://github.com/SchemaStore/schemastore/pull/6527)). Editors and language servers that use the Store's catalog therefore validate and autocomplete `*.mm.json` files without further configuration. The entry's `url` points to `schema/latest/measuremap.schema.json`, so editors pick up every new release automatically.

### Updating the SchemaStore entry after a release

The entry also lists every release under `versions`. After each release, add the new version there with a pull request to [SchemaStore/schemastore](https://github.com/SchemaStore/schemastore). The example below is for 1.1.0, using a clone of a personal fork with `upstream` pointing to SchemaStore:

1. Start a branch from the current upstream catalog:
   ```bash
   git fetch upstream
   ```
   ```bash
   git switch -c measuremap-1.1.0 upstream/master
   ```
2. In `src/api/json/catalog.json`, find the entry with `"name": "MeasureMap"` and add a line to `versions`:
   ```json
   "1.1.0": "https://measure-map.github.io/specification/schema/1.1.0/measuremap.schema.json"
   ```
   Leave `url` unchanged.
3. Commit, push to the fork, and open the pull request:
   ```bash
   git commit -am "Add MeasureMap 1.1.0 to the catalog"
   ```
   ```bash
   git push -u origin measuremap-1.1.0
   ```
   ```bash
   gh pr create --repo SchemaStore/schemastore --base master --title "Add MeasureMap 1.1.0 to the catalog" --body "Lists the new MeasureMap release in versions."
   ```

Change `fileMatch` or `url` only if the file name convention or the publishing location changes.

## License

The specification is licensed under the [MIT License](LICENSE).

## Codes

The MM codes provide functionality for:

- validating MMs against a formal schema: https://github.com/measure-map/specification
- producing MMs directly from everything parseable by music21 (MusicXML, krn, ...) and the ms3 parser (mscx, mscz): https://github.com/measure-map/pyMeasureMap
- integrating MMs into the Dezrann workflow:
https://gitlab.com/algomus.fr/dezrann/dezrann-corpus

- compression / expansion of MMs: https://github.com/measure-map/pyMeasureMap
- diagnosis of differences between two MMs, yielding human- and machine-readable instructions for adjusting one to fit: https://github.com/measure-map/pyMeasureMap
- implementation of the diagnosis instructions to make in-place changes on one score to align and fit with another (currently music21-application only): https://github.com/MarkGotham/bar-measure


## Corpus-wide examples

We provide curated measure maps for several corpora. We also align and include the Mozart and Lieder corpora on [Dezrann](http://www.dezrann.net) with scores and annotations.

### Bach Chorales

- Scores, measure maps, and analyses (371 chorales from 3 sources): https://github.com/measure-map/aligned_bach_chorales

### OpenScore Lieder

- Scores and analyses: https://github.com/MarkGotham/When-in-Rome/tree/master/Corpus/OpenScore-LiederCorpus
- Dezrann corpus: http://dezrann.net/explore/openscore-lieder

### Mozart Piano Sonatas

- Scores: https://github.com/DCMLab/mozart_piano_sonatas/tree/main/MS3
- Measure maps: https://gitlab.com/algomus.fr/symbolic-texture-dataset/-/tree/measuremap/measuremap/verbose
- Analyses: https://gitlab.com/algomus.fr/symbolic-texture-dataset/-/tree/dez_augmented/dez_augmented
- Dezrann corpus: http://dezrann.net/explore/mozart-piano-sonatas
