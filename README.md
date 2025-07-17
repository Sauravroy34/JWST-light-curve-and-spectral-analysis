# Detecting Carbon Dioxide in WASP-39b's Atmosphere

WASP-39b, also known as Bocaprins, is a hot Jupiter exoplanet orbiting the star WASP-39 in the constellation Virgo, about 700 light-years from Earth. Discovered in February 2011 by the WASP project, it stands out for its atmosphere, which contains significant amounts of water, carbon dioxide, and sulfur dioxide. This README explains how we detect exoplanets like WASP-39b and analyze their atmospheres, focusing on the detection of carbon dioxide.

## Finding Exoplanets

Exoplanets can be detected using methods like direct imaging, radial velocity, and transit photometry. Among these, transit photometry is the most widely used. This method measures the slight drop in a star’s brightness when a planet passes (transits) in front of it. The depth of this dip reveals the planet’s radius, calculated using the formula:

**Transit Dip = (R_p / R_s)²**

where *R_p* is the planet’s radius and *R_s* is the star’s radius. The resulting graph, called a light curve, shows this dip, confirming the presence of a planet.

### Light Curve of WASP-39b

![Light Curve](https://github.com/user-attachments/assets/30050418-5098-4b9f-be09-e05b338853c9)

The light curve above shows WASP-39b’s transit, analyzed using a Poisson regressor to identify the general trend. For more details on light curves, check this [tutorial](https://avanderburg.github.io/tutorial/tutorial.html).

## Transmission Spectroscopy

When a planet transits, some starlight passes through its atmosphere. Different wavelengths of light are absorbed by atmospheric molecules, causing variations in the transit depth. Plotting these variations against wavelength produces a transmission spectrum, which reveals details about the atmosphere’s composition. For a clear explanation, watch this [video](https://www.youtube.com/watch?v=ZnLg4YFMfDQ&ab_channel=MartianColonist).

### Transmission Spectrum of WASP-39b

![Transmission Spectrum](https://github.com/user-attachments/assets/b6178a43-ae39-41d8-9c1d-05b857406a28)

The spectrum above shows how WASP-39b’s atmosphere affects light at different wavelengths.

## Detecting Atmospheric Composition

To determine the atmospheric composition, we use atmospheric retrieval. This involves comparing observed data to model spectra generated with known compositions. The model that best fits the data indicates the likely atmospheric makeup. For more insights, refer to this [video](https://www.youtube.com/watch?v=ZnLg4YFMfDQ&ab_channel=MartianColonist).

![Model Fit](https://github.com/user-attachments/assets/5efc277a-e584-465d-a986-0e71490eb463)

## Composition of WASP-39b’s Atmosphere

As a hot Jupiter, WASP-39b is expected to contain gases like methane and carbon dioxide. Analysis confirms the presence of water, sulfur dioxide, methane, and carbon dioxide. A distinct bump in the transmission spectrum between 4–5 µm confirms carbon dioxide.

![Molecular Contributions](https://github.com/user-attachments/assets/e8355d1c-d8f0-4439-9119-03fb3b6278e4)

## Pressure-Temperature Profile

The retrieval process assumes a [Guillot pressure-temperature profile](https://www.aanda.org/articles/aa/pdf/2010/12/aa13396-09.pdf) to model the atmosphere’s temperature structure.

![Pressure-Temperature Profile](https://github.com/user-attachments/assets/dcdc5ea5-c144-445e-8c7c-2e1c59e9e020)

## Molecular Abundance

The abundance of molecules like water, methane, carbon dioxide, and sulfur dioxide varies with atmospheric pressure, as shown below.

![Pressure vs. Abundance](https://github.com/user-attachments/assets/c709a606-6ba8-4fbd-9932-38365baae326)

The transmission spectrum highlights specific absorption features for each molecule.

![Chemical Lines](https://github.com/user-attachments/assets/af1bfc59-19cb-4ed1-849d-48ad3108ddeb)
