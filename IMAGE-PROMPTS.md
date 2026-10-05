# Image Prompts — Round Rock Elite Water Softener

24 AI image prompts (Gemini, Midjourney, DALL·E, Flux or similar). Each prompt is self-contained: paste it as is.

## How to use

1. Generate each image and **save it in `public/` with exactly the filename shown** (e.g. `hero-softener.png`, or .jpg/.webp). Exact names mean no hand-matching afterwards.
2. Tell Claude the images are ready. It converts them to WebP with `sharp`, moves them to `src/assets/images/`, and wires each into its page through `astro:assets`.
3. Optionally run `scripts/brand_images.py` afterwards to bake the logo badge into the photos.

## Rules these prompts follow

- **No faces.** Technicians are shown from behind or as hands only (PROVISION.md), which also avoids implying real staff.
- **No text, logos or brand names.** AI-generated lettering is unreliable and we have no tenant or brand relationships yet. Equipment is deliberately generic and unbranded.
- **Local but honest.** Texas-style homes (slab foundations, garage installs, limestone and brick). No invented business claims, awards, vehicles with names, or real addresses.
- **Brand-matched colour.** Teal and copper accents echo the logo. Do not recolour the whole image.

Check each result for: stray text or logos, extra fingers or hands, plumbing that makes no sense (pipes going nowhere, a softener with two brine tanks), and visible faces. Regenerate if any appear.

## A. Homepage images (3)

### `hero-softener`
- **Size:** 7:6 (landscape, ~700x600)  
- **Used on:** Homepage hero, right column

```
a generic, unbranded residential water softener: a tall slim teal-blue resin tank next to a squat grey brine tank with a closed lid, a digital control head on top, copper and white PEX pipe connections, freshly installed against the white wall of a tidy Texas home garage with a painted concrete slab floor, white wall, and a storage shelf. A water heater and copper supply lines are visible behind it. Soft light from a garage window. The softener is the clear subject, centred, with breathing room around it. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 7:6.
```

### `best-technicians`
- **Size:** 7:6 (~600x512)  
- **Used on:** Homepage 'Why We're the Best' section, left column

```
Two installers seen from behind, kneeling in a tidy Texas home garage with a painted concrete slab floor, white wall, and a storage shelf and discussing a water softener installation with a clipboard and a tape measure; a technician in a plain dark-teal work shirt and work gloves with no logos. a generic, unbranded residential water softener: a tall slim teal-blue resin tank next to a squat grey brine tank with a closed lid, a digital control head on top, copper and white PEX pipe connections stands in front of them. Warm, trustworthy, working-in-a-real-home feel. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 7:6.
```

### `hard-water-tile`
- **Size:** 3:2 (~600x400)  
- **Used on:** Homepage 'Hard Water Effects' section

```
Macro close-up of a chrome kitchen faucet and sink basin covered in chalky white limescale and water spots, with a smudged drinking glass beside it. Bright natural window light, honest and slightly gritty, not staged-clean. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 3:2.
```

## B. Page header images (21)

All headers are **5:4 landscape (about 1500x1200 px)**. They are cropped to the right-hand column of each page hero, so keep the subject centred.

### `water-quality-header`
- **Used on:** Water Quality page

```
A homeowner's hand holding a clear glass of tap water up to a bright kitchen window, with a digital TDS water test meter and a small hardness test kit on the counter beside it. Light stone countertop. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `hard-water-header`
- **Used on:** Hard Water page

```
A glass shower door and chrome showerhead in a bright, modern bathroom with heavy white mineral spotting and limescale streaks on the glass and fixtures. Natural light from a frosted window. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `installation-header`
- **Used on:** Installation page

```
An installer, shown from behind, connecting copper and PEX bypass plumbing to a generic, unbranded residential water softener: a tall slim teal-blue resin tank next to a squat grey brine tank with a closed lid, a digital control head on top, copper and white PEX pipe connections in a tidy Texas home garage with a painted concrete slab floor, white wall, and a storage shelf; a technician in a plain dark-teal work shirt and work gloves with no logos. Pipe wrench and tubing cutter on a drop cloth in the foreground. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `comparison-header`
- **Used on:** Comparison page

```
Two water treatment systems side by side in a clean garage, to compare: on the left a generic salt-based softener with a grey brine tank, on the right a slim salt-free conditioner cylinder with no brine tank. Even, neutral lighting, both clearly visible, nothing labelled. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `faq-header`
- **Used on:** FAQ page

```
A homeowner couple seen from behind at a kitchen island, looking at a tablet and a notepad together while a glass of water and a small stack of papers sit on the counter. Warm, relaxed, curious mood. Texas Hill Country limestone-and-oak kitchen. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `quote-header`
- **Used on:** Quote page

```
A technician's hands, in work gloves, holding a clipboard with a blank estimate sheet and a tape measure, in front of a water softener in a garage. Friendly, professional, close-up on the hands and clipboard; no readable text. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `neighbourhood-header`
- **Used on:** Neighbourhoods page

```
A wide, sunny view of a Round Rock, Texas suburban street: light-limestone and brick two-storey homes with two-car garages, young live oaks and cedar elms, manicured lawns, a clear blue sky. Golden afternoon light, no people, no signs, no visible house numbers. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `products-header`
- **Used on:** Products page

```
a generic, unbranded residential water softener: a tall slim teal-blue resin tank next to a squat grey brine tank with a closed lid, a digital control head on top, copper and white PEX pipe connections and a slim whole-home filter canister standing side by side against a white garage wall, shot at slight three-quarter angle like a clean product photograph, soft studio-quality natural light. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `repair-header`
- **Used on:** Repair page

```
A technician, from behind, kneeling to service a generic, unbranded residential water softener: a tall slim teal-blue resin tank next to a squat grey brine tank with a closed lid, a digital control head on top, copper and white PEX pipe connections: the control head's cover is off showing the circuit board and valve, a small toolkit open on the floor; a technician in a plain dark-teal work shirt and work gloves with no logos. Concentrated, skilled, close and hands-on. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `resin-bed-replacement-header`
- **Used on:** Resin Bed Replacement page

```
Close-up of gloved hands pouring fresh, amber-tan resin beads from a bag into the open top of a softener resin tank, with a few beads scattered on a drop cloth. Bright garage light, tactile and detailed. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `brine-tank-cleaning-header`
- **Used on:** Brine Tank Cleaning page

```
A technician's gloved hands lifting the lid of a grey brine tank to clean it, with a wet-dry vacuum and a bucket nearby; a clear view of the salt and the inside of the tank. Garage setting, practical and clean. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `whole-home-filtration-header`
- **Used on:** Whole Home Filtration page

```
A whole-home water filtration setup mounted on a garage wall: a large carbon filter canister and a sediment pre-filter in a row with clear copper pipe runs, clean and organised, with a softener partly visible at the edge. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `reverse-osmosis-header`
- **Used on:** Reverse Osmosis page

```
A modern under-sink reverse osmosis system, under a kitchen sink with the cabinet doors open: a row of white filter cartridges, a small storage tank and neat tubing, plus a separate slim chrome RO faucet visible on the sink. Bright, tidy and modern. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `salt-based-installation-header`
- **Used on:** Salt-Based Installation page

```
A completed salt-based installation: a generic, unbranded residential water softener: a tall slim teal-blue resin tank next to a squat grey brine tank with a closed lid, a digital control head on top, copper and white PEX pipe connections, with several white bags of water softener salt stacked beside the brine tank, in a tidy Texas home garage with a painted concrete slab floor, white wall, and a storage shelf. Clean, finished, ready-to-use. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `salt-free-installation-header`
- **Used on:** Salt-Free Installation page

```
A slim salt-free water conditioner cylinder installed on a garage wall with copper pipe fittings and a bypass valve, with no brine tank and no drain line in view. Minimal, uncluttered, modern. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `water-softener-sizing-header`
- **Used on:** Sizing Guide page

```
A technician's hands, in work gloves, holding a clipboard with a blank grid sheet and a calculator, beside a water softener's control head with a small digital display showing a number. Overhead-angle close-up, no readable text. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `new-construction-installation-header`
- **Used on:** New Construction page

```
The interior of a new-build Texas home under construction: exposed wall studs, a framed utility closet, and white and red PEX plumbing runs with a stub-out ready for a water softener. Daylight through an open doorway, sawdust on the slab floor, builder's level on a sawhorse. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `control-head-repair-header`
- **Used on:** Control Head Repair page

```
Extreme close-up of a water softener's electronic control head with its front cover removed, showing the circuit board, small motor and valve body, held by a gloved hand with a small screwdriver. Sharp macro detail. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `free-water-test-header`
- **Used on:** Free Water Test page

```
A technician, from behind or hands-only, at a home kitchen sink holding a small vial of tap water with a colour-change test reagent, a hardness test kit and a TDS meter laid out on the counter. Bright and clinical but friendly. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `about-header`
- **Used on:** About page

```
Two technicians seen from behind in dark-teal work shirts, loading equipment into the back of a plain white service van with no lettering, on a sunny suburban street. Warm, local, dependable mood. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

### `contact-header`
- **Used on:** Contact page

```
A technician, seen from behind, standing at the front door of a Texas limestone-and-brick home with a tool bag at their feet, in a dark-teal work shirt, about to ring the doorbell. Warm morning light. Photorealistic editorial photograph, natural daylight, shallow depth of field, clean modern composition, muted deep-teal and warm copper colour accents, crisp detail. Absolutely no text, lettering, logos, watermarks or brand names anywhere in the image. No visible faces: any person is shown from behind, from the shoulders down, or as hands only. Aspect ratio 5:4.
```

## Not included

- **About page placeholders** (before/after, team, founders, happy homeowner): skipped on purpose. They would present invented people and results as real. Add them when a tenant supplies real photos.
- **Social image and logo files** are already done (`public/og-default.jpg`, `logo-mark.png`, `logo-full.png`).
