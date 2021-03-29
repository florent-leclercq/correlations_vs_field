# correlations_vs_field #

[![arXiv](https://img.shields.io/badge/astro--ph.CO-arxiv%3A2103.04158-B31B1B.svg?style=flat)](https://arxiv.org/abs/2103.04158)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/florent-leclercq/correlations_vs_field/blob/main/LICENSE)
[![Website florent-leclercq.eu](https://img.shields.io/website-up-down-green-red/http/florent-leclercq.eu.svg)](http://florent-leclercq.eu/)

Correlation functions versus field-level inference in cosmology: example with log-normal fields

## Documentation ##

This is a companion repository to Leclercq & Heavens 2021, *On the accuracy and precision of correlation functions and field-level inference in cosmology*, <a href="http://arxiv.org/pdf/2103.04158" class="document" target="blank">arXiv:2103.04158</a>.

### Main code: two-point correlation function versus field-level inference ###

The code contains a python library for log-normal fields, [libLN.py](libLN.py) and two example configuration files: [config_10.py](config_10.py) (alpha=1.0, beta=0.5) and [config_02.py](config_02.py) (alpha=0.2, beta=0.5). The main part of the code is split into several Jupyter notebooks:
* [Inference_Summaries.ipynb](Inference_Summaries.ipynb): likelihood-based analysis of the two-point correlation function (section 3 in Leclercq & Heavens 2021)
* [Inference_SBI.ipynb](Inference_SBI.ipynb): simulation-based inference using the two-point correlation function (section 4 in Leclercq & Heavens 2021)
* Inference_DA_*.ipynb: field-level inference with data assimilation (section 5 in Leclercq & Heavens 2021)
* [Plots.ipynb](Plots.ipynb): code to produce the plots of the paper, and some more

The raw data (pools of simulations for simulation-based inference and Markov Chains for data assimilation) are not stored in this repository due to their large size. They are available upon reasonable request to the corresponding author.

In addition to usual python packages such as numpy, scipy, matplotlib, pickle, the code has the following dependencies:
* [pydelfi](https://github.com/justinalsing/pydelfi) and [ELFI](https://github.com/elfi-dev/elfi) for simulation-based inference ([Inference_SBI.ipynb](Inference_SBI.ipynb))
* [pymc3](https://docs.pymc.io) for data assimilation (Inference_DA_*.ipynb)

### Simulation-based inference using cosmic web summaries ###

In the current branch ([tweb](https://github.com/florent-leclercq/correlations_vs_field/tree/tweb)), the [libLN.py](libLN.py) library contains additional functions to compute summary statistics of log-normal fields based on the cosmic web:
* the volume filling fractions of the three different structure types (clusters, filaments, and voids) defined using the 2D equivalent of the T-web procedure (see <a href="https://arxiv.org/abs/astro-ph/0610280" class="document" target="blank">Hahn <i>et al.</i> 2007</a>, <a href="https://arxiv.org/abs/1502.02690" class="document" target="blank">Leclercq <i>et al.</i> 2015</a>),
* and the number counts of clusters and voids, as defined above.

The code contains two additional notebooks:
* [Inference_SBI_tweb.ipynb](Inference_SBI_tweb.ipynb): simulation-based inference using the cosmic web summaries defined above,
* [Inference_SBI_combined.ipynb](Inference_SBI_combined.ipynb): joint simulation-based inference using the two-point correlation function and cosmic web summaries,

and the notebook [Plots.ipynb](Plots.ipynb) additionally contains the code necessary to produce the figure below:

![posterior_tweb](https://github.com/florent-leclercq/correlations_vs_field/blob/tweb/posterior_tweb.png?raw=true)

## Contributors ##

* Florent Leclercq, florent.leclercq@polytechnique.org
* Alan Heavens

## Reference ##


To acknowledge the use of this software, please cite the paper <a href="http://arxiv.org/pdf/2103.04158" class="document" target="blank">Leclercq & Heavens (2021)</a>: 

*On the accuracy and precision of correlation functions and field-level inference in cosmology*<br/>
F. Leclercq, A. Heavens<br/>
<a href="http://arxiv.org/abs/2103.04158" target="blank">arXiv:2103.04158</a> [<a href="http://arxiv.org/abs/2103.04158" target="blank">astro-ph.CO</a>] [<a href="https://ui.adsabs.harvard.edu/?#abs/2021arXiv210304158L" target="blank">ADS</a>] [<a href="http://arxiv.org/pdf/2103.04158" class="document" target="blank">pdf</a>]

    @ARTICLE{correlations_vs_field,
        author = {{Leclercq}, Florent and {Heavens}, Alan},
        title = "{On the accuracy and precision of correlation functions and field-level inference in cosmology}",
        journal = {arXiv e-prints},
        keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics, Astrophysics - Instrumentation and Methods for Astrophysics, Statistics - Applications},
        year = 2021,
        month = mar,
        eid = {arXiv:2103.04158},
        pages = {arXiv:2103.04158},
        archivePrefix = {arXiv},
        eprint = {2103.04158},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv210304158L},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }

## License ##

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. By downloading and using pySELFI, you agree to the [LICENSE](LICENSE), distributed with the source code in a text file of the same name.
