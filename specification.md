# MeasureMap Specification

## Specification

The MeasureMap specification is currently defined in the form of the following things:

1. `measure.schema.json`: a [JSON Schema](https://json-schema.org/) describing a single entry of a MeasureMap, here 
   called a `Measure` object.
2. `measuremap.schema.json`: a JSON Schema describing a MeasureMap object, which is an array of Measure objects.
3. The rules by which to compute the default successor to a Measure object, which define how a MeasureMap is 
   compressed and decompressed. 

The following documentation was generated directly from the `schema.json` files using the online tool 
[json-schema-md-doc](https://brianwendt.github.io/json-schema-md-doc/).

# Measure

_A single measure (UK: bar) or measure-like unit of a music score._

Type: `object`

<i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json</i>

&#36;schema: [http://json-schema.org/draft-07/schema](http://json-schema.org/draft-07/schema)

<b id="httpsraw.githubusercontent.commeasure-mapspecificationmainmeasure.schema.json">&#36;id: https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json</b>

This schema <u>does not</u> accept additional properties.

**_Properties_**

 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/ID">ID</b>
	 - _Any unique string to identify this Measure object. Unique, here, means that the string cannot be used as ID for another object that forms part of the same MeasureMap. The 'next' array may use these IDs to refer to other Measures. Additionally, IDs can prove useful in cross-relating between MeasureMaps relating to different editions of the same piece, e.g. by assigning identical IDs for measures that are identical across the two. The ID could be, for instance, human-readable form (e.g., the 'count' value converted to a string) or a random string (often the case in MEI scores)._
	 - Type: `string`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/ID">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/ID</i>
	 - Example values: 
		 1. _"1"_
		 2. _"m20"_
		 3. _"var1bar6qs234"_
		 4. _"https://dme.mozarteum.at/movi/navigator/155/001/01/20/nma"_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/count">count</b>
	 - _Position of this Measure object in the MeasureMap, using natural numbers starting with 1. This serves primarily as an index, and does not attempt detailed musical conventions. In the simplest case (e.g., a score with no anacrusis or other irregularities) this count matches the (most musical) number field below._
	 - Type: `integer`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/count">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/count</i>
	 - Range:  &ge; 1
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/qstamp">qstamp</b>
	 - _The symbolic time to have elapsed since the beginning of the source, measured in quarter notes._
	 - Type: `number`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/qstamp">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/qstamp</i>
	 - Example values: 
		 1. `0`
		 2. `16.5`
		 3. `20.66667`
	 - Range:  &ge; 0
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/number">number</b>
	 - _A number assigned to this measure based on a given set of rules or conventions. One wide-spread convention, for instance, is that a piece starts with measure number 0 if it has an anacrusis and with number 1 otherwise._
	 - Type: `integer`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/number">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/number</i>
	 - Range:  &ge; 0
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/name">name</b>
	 - _A label for the Measure. Typically used for distinguishing between Measures with the same number, e.g. for first and second endings (as in '16a', '16b') or split logical measures (as in '16-1', '16-2')._
	 - Type: `string`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/name">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/name</i>
	 - Example values: 
		 1. _"1"_
		 2. _"16a"_
		 3. _"28-1"_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/time_signature">time_signature</b>
	 - _A label for the time signature. Typically this takes the form <int>/<int>, as in ‘3/8’, but can be any text (e.g., ‘C’, ‘common time’, ‘unmeasured’ ‘cadenza’) as long as actual_length is specified._
	 - Type: `string`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/time_signature">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/time_signature</i>
	 - Example values: 
		 1. _"3/8"_
		 2. _"C"_
		 3. _"cadenza"_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/nominal_length">nominal_length</b>
	 - _The default duration that corresponds to the given 'time_signature', in quarter notes. Can be derived from 'time_signature' if it takes the form of an '<int>/<int>'-encoded fraction. Can take the value 'null' if the time signature has no corresponding duration (e.g. 'cadenza')._
	 - Types: `number`, `null`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/nominal_length">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/nominal_length</i>
	 - Example values: 
		 1. `1.5`
		 2. `4`
		 3. `6`
		 4. `null`
	 - Range:  &ge; 0
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/actual_length">actual_length</b>
	 - _The actual duration of the measure, in quarter notes._
	 - Type: `number`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/actual_length">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/actual_length</i>
	 - Example values: 
		 1. `0.25`
		 2. `4`
		 3. `6`
	 - Exclusive Range:  > 0
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/start_repeat">start_repeat</b>
	 - _Typical usage is with the bool type, with 'true' indicating a start repeat at the beginning of the measure._
	 - Types: `boolean`, `number`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/start_repeat">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/start_repeat</i>
	 - Default: _false_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/end_repeat">end_repeat</b>
	 - _Typical usage is with the bool type, with 'true' indicating an end repeat at the end of the measure._
	 - Types: `boolean`, `number`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/end_repeat">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/end_repeat</i>
	 - Default: _false_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/next">next</b>
	 - _The 'ID' strings or 'count' integers that correspond to all measures that can follow this one. The corresponding field needs to be present in the MeasureMap._
	 - Type: `array`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/next">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/next</i>
		 - **_Items_**
		 - Types: `string`, `integer`
		 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/next/items">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/next/items</i>
	

### MeasureMap

_An array of Measure objects that represents the measure (bar) units of a music score._

Type: `array`

<i id="https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json">path: #https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json</i>

&#36;schema: [http://json-schema.org/draft-07/schema](http://json-schema.org/draft-07/schema)

<b id="httpsraw.githubusercontent.commeasure-mapspecificationmainmeasuremap.schema.json">&#36;id: https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json</b>

Item Count:  &ge; 2
 - **_Items_**
 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json/items">path: #https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json/items</i>
 - &#36;ref: [measure.schema.json](#measure.schema.json)

