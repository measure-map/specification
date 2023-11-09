# Aligning symbolic music with Measure maps

Aligning versions of the same source material has been a persistent challenge in the field of digital libraries for musicology, and a barrier to progress. The growing number of publicly accessible symbolic datasets (of scores, analyses, and more) now increasingly cover multiple versions of the same works. As creators/curators/representatives of many such datasets and encoding standards, we came together in this project to coordinate platform-neutral interoperabilility for combining and comparing different sources, reliably and automatically. Here, we outline the main challenges and propose solutions centred on the **measure map**: a lightweight format for representing symbolic bar information alone. We offer new code for producing this representation from various formats, diagnosing differences, and even solving for those differences by modifying sources in-place. While we cannot solve for every possible discrepancy, we do provide corpus-scale demonstration; and while we focus on symbolic data, we consider the measure map also a useful basis for aligning audio, manuscripts and any source for which bar-relative location data provides a useful point of reference.

## Reference

Mark Gotham et al., The ‘Measure Map’: an inter-operable standard for aligning symbolic music, International Conference on Digital Libraries for Musicology (DLfM 2023), 91-99, https://doi.org/10.1145/3625135.3625136

Formal specification: https://github.com/measure-map/specification/blob/main/specification.md

## Codes

The MM codes provide functionality for:

- validating MMs against a formal schema: https://github.com/measure-map/specification
- producing MMs directly from everything parseable by music21 (MusicXML, krn, ...) and the ms3 parser (mscx, mscz): https://github.com/measure-map/pyMeasureMap
- integrating MMs into the Dezrann workflow:
https://gitlab.com/algomus.fr/dezrann/dezrann-corpus

- compression / expansion of MMs
- diagnosis of differences between two MMs, yielding human-and machine-readable instructions for adjusting one to fit
- implementation of the diagnosis instructions to make in-place changes on one score to align and fit with the another (currently music21-application only)


## Corpus-wide examples

We provide curated measure maps for several corpora. We also align and include the Mozart and Lieder corpora on [Dezrann](http://www.dezrann.net) with scores and annotations.

### Bach Chorales

- Scores, measure maps, and analyses (371 chorales from 3 sources): https://github.com/measure-map/aligned_bach_chorales

### OpenScore Lieder

- Scores and analyses: https://github.com/MarkGotham/When-in-Rome/tree/master/Corpus/OpenScore-LiederCorpus
- Measure maps: ??? 
- Dezrann corpus: http://dezrann.net/explore/openscore-lieder

### Mozart Piano Sonatas

- Scores: https://github.com/DCMLab/mozart_piano_sonatas/tree/main/MS3
- Measure maps: https://gitlab.com/algomus.fr/symbolic-texture-dataset/-/tree/measuremap/measuremap/verbose
- Analyses: https://gitlab.com/algomus.fr/symbolic-texture-dataset/-/tree/dez_augmented/dez_augmented
- Dezrann corpus: http://dezrann.net/explore/mozart-piano-sonatas
