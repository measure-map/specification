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

### Measure

_A single measure (UK: bar) or measure-like unit of a music score._

Type: `object`

<i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json</i>

&#36;schema: [http://json-schema.org/draft-07/schema](http://json-schema.org/draft-07/schema)

<b id="httpsraw.githubusercontent.commeasure-mapspecificationmainmeasure.schema.json">&#36;id: https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json</b>

This schema <u>does not</u> accept additional properties.

**_Properties_**

 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/ID">ID</b>
	 - _Any unique string to identify this object._
	 - Type: `string`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/ID">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/ID</i>
	 - Example values: 
		 1. _"1"_
		 2. _"m20"_
		 3. _"https://dme.mozarteum.at/movi/navigator/155/001/01/20/nma"_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/count">count</b>
	 - _A simple count of measure units in the described source, using natural numbers starting with 1._
	 - Type: `integer`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/count">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/count</i>
	 - Range:  &ge; 1
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/qstamp">qstamp</b>
	 - _The symbolic time to have elapsed since the start of the source, measured in quarter notes._
	 - Type: `number`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/qstamp">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/qstamp</i>
	 - Example values: 
		 1. `0`
		 2. `16.5`
		 3. `20.66667`
	 - Range:  &ge; 0
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/number">number</b>
	 - _A number assigned to this measure, which typically follows musical convention, for instance starting with natural numbers (1, 2, 3...), except in the case of anacruses which start instead on (0, 1, 2...)._
	 - Type: `integer`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/number">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/number</i>
	 - Range:  &ge; 0
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/name">name</b>
	 - _A label for the measure. Typically used for distinguishing between measures with the same number (as in '16a', '16b', '16c') or rehearsal marks._
	 - Type: `string`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/name">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/name</i>
	 - Example values: 
		 1. _"1"_
		 2. _"16a"_
		 3. _"H"_
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/time_signature">time_signature</b>
	 - _A label for the time signature. Typically this takes the form of `<int>/<int>' but can be an arbitrary string as long or 'null' as long as actual_length is specified._
	 - Types: `string`, `null`
	 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/time_signature">path: #https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/time_signature</i>
	 - Example values: 
		 1. _"3/8"_
		 2. _"C"_
		 3. `null`
 - <b id="#https://raw.githubusercontent.com/measure-map/specification/main/measure.schema.json/properties/nominal_length">nominal_length</b>
	 - _The default duration that corresponds to the given 'time_signature', in quarter notes._
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

 - **_Items_**
 - <i id="https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json/items">path: #https://raw.githubusercontent.com/measure-map/specification/main/measuremap.schema.json/items</i>
 - &#36;ref: [measure.schema.json](#measure.schema.json)

